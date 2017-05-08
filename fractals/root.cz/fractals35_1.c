//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Autor: Pavel Tisnovsky
//
// Vykresleni jednoducheho obrazce (Sierpinskeho trojuhelniku) pomoci
// linearizovanych systemu iterovanych funkci L-IFS. Po spusteni programu se
// ve spodni casti okna zobrazi kratka napoveda s klavesovymi zkratkami.
// Pixmapu s vykreslenym fraktalem je mozne ulozit do souboru ve formatu TGA
// pomoci klavesove zkratky [S]. Zmena typu IFS se provadi stiskem klaves [0]-[9].
// Ukonceni aplikace se provede klavesou [Esc] nebo klavesou [Q].
//-----------------------------------------------------------------------------

#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <GL/glut.h>                            // hlavickovy soubor funkci GLUTu a OpenGL
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define WINDOW_TITLE    "Fraktaly 35.1"         // titulek okna
#define WINDOW_WIDTH    640                     // pocatecni velikost okna
#define WINDOW_HEIGHT   480
#define FILE_NAME       "fraktaly351.tga"       // jmeno souboru pro ulozeni pixmapy

#define PIXMAP_WIDTH    512                     // sirka pixmapy
#define PIXMAP_HEIGHT   384                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

typedef enum {                                  // typy vykreslovacich rezimu
    IterPutPixel,
    IterAddPixel,
    TransfPutPixel,
    TransfAddPixel
} DrawType;

pixmap *pixIFS;                                 // pixmapa pro obrazek IFS fraktalu

int    maxiter=1000;                            // maximalni pocet iteraci
int    rf=1, gf=1, bf=1;                        // priznaky barvovych slozek
int    deltar=1, deltag=1, deltab=1;            // prirustky barvovych slozek
double scale=1.0;                               // meritko fraktalu
double xpos=0.0;                                // posun fraktalu
double ypos=0.0;                                // posun fraktalu
double ksi=0.5;                                 // konstanta ksi ovlivnujici tvar fraktalu
int    redraw=1;
DrawType    drawType=IterPutPixel;



//-----------------------------------------------------------------------------
// Funkce pro vytvoreni pixmapy o zadane velikosti
//-----------------------------------------------------------------------------
pixmap * createPixmap(const unsigned int width, const unsigned int height)
{
    pixmap *p=(pixmap *)malloc(sizeof(pixmap)); // alokace struktury pixmapy
    if (!p) return NULL;
    p->width=width;                             // naplneni struktury
    p->height=height;
    p->pixels=(unsigned char *)malloc(3*width*height);
    if (!p->pixels) {                           // alokace pole pro pixely
        free(p);                                // alokace se nepovedla
        return NULL;
    }
    else {
        memset(p->pixels, 0, 3*width*height);   // smazani pixmapy
    }
    return p;
}



//-----------------------------------------------------------------------------
// Funkce pro zruseni pixmapy
//-----------------------------------------------------------------------------
void destroyPixmap(pixmap *p)
{
    if (p->pixels) free(p->pixels);             // uvolnit vlastni pixmapu
    if (p) free(p);                             // i okolni strukturu
}



//-----------------------------------------------------------------------------
// Vymazani pixmapy
//-----------------------------------------------------------------------------
void clearPixmap(const pixmap *p)
{
    if (!p) return;
    if (!p->pixels) return;
    memset(p->pixels, 0, 3*p->width*p->height);
}



//-----------------------------------------------------------------------------
// Funkce pro vykresleni pixmapy do barvoveho bufferu
//-----------------------------------------------------------------------------
void drawPixmap(const pixmap *p)
{
    if (!p || !p->pixels) return;
    glDrawPixels(                               // vykresleni pixmapy
            p->width, p->height,                // sirka a vyska pixmapy
            GL_RGB,                             // format dat pixelu
            GL_UNSIGNED_BYTE,                   // datovy typ kazde barevne slozky
            p->pixels);                         // ukazatel na pamet s barvami pixelu
}



//-----------------------------------------------------------------------------
// Ulozeni pixmapy do externiho souboru
//-----------------------------------------------------------------------------
void savePixmap(const pixmap *p, const char *fileName)
{
    FILE *fout;
    unsigned int i, j, k;
    unsigned char tgaHeader[18]={               // hlavicka formatu typu TGA
                        0x00,                   // typ hlavicky TGA
                        0x00,                   // nepouzivame paletu
                        0x02,                   // typ obrazku je RGB TrueColor
                        0x00, 0x00,             // delka palety je nulova
                        0x00, 0x00, 0x00,       // pozice v palete nas nezajima
                        0x00, 0x00, 0x00, 0x00, // obrazek je umisteny na pozici [0, 0]
                        0x00, 0x00, 0x00, 0x00, // sirka a vyska obrazku (dva byty na polozku)
                        0x18,                   // format je 24 bitu na pixel
                        0x20                    // orientace bitmapy v obrazku
    };
    if (!p || !p->pixels) return;
    memcpy(tgaHeader+12, &(p->width), 2);       // do hlavicky TGA zapsat velikost obrazku
    memcpy(tgaHeader+14, &(p->height), 2);
    fout=fopen(fileName, "wb");
    if (fout) {
        fwrite(tgaHeader, 18, 1, fout);         // zapsat hlavicku TGA do souboru
        for (j=p->height; j; j--) {             // radky zapisovat v opacnem poradi
            unsigned int yoff=(j-1)*3*p->width; // y-ovy offset v poli
            unsigned int xoff=0;                // x-ovy offset v poli
            for (i=0; i<p->width; i++) {        // pro kazdy pixel na radku
                for (k=0; k<3; k++) {           // prohodit barvy RGB na BGR
                    fputc(p->pixels[xoff+yoff+2-k], fout); // a zapsat do souboru
                }
                xoff+=3;                        // posun na dalsi pixel
            }
        }
        fclose(fout);
    }
}



//-----------------------------------------------------------------------------
// Zmena barvy pixelu na zadanych souradnicich
//-----------------------------------------------------------------------------
void putpixel(pixmap *p,
              const unsigned int x,             // pozice pixelu v pixmape
              const unsigned int y,
              const unsigned char r,            // barva pixelu
              const unsigned char g,
              const unsigned char b)
{
    int pos;
    // zde se vyuziva zkraceneho vyhodnoceni vyrazu - pokud plati !p, nic se dale netestuje
    if (!p || !p->pixels || x>=p->width || y>=p->height) return;
    pos=3*(x+y*p->width);
    p->pixels[pos++]=r;                         // nastaveni barvy pixelu
    p->pixels[pos++]=g;
    p->pixels[pos]=b;
}



//-----------------------------------------------------------------------------
// Prirustek barvy pixelu na zadanych souradnicich
//-----------------------------------------------------------------------------
void addpixel(pixmap *p, const unsigned int x, const unsigned int y,
                         const unsigned char dr, const unsigned char dg, const unsigned char db)
{
    int pos;
    // zde se vyuziva zkraceneho vyhodnoceni vyrazu - pokud plati !p, nic se dale netestuje
    if (!p || !p->pixels || x>=p->width || y>=p->height) return;
    pos=3*(x+y*p->width);
    if (p->pixels[pos]<256-dr) p->pixels[pos]+=dr;// nastaveni cervene slozky barvy pixelu
    pos++;
    if (p->pixels[pos]<256-dg) p->pixels[pos]+=dg;// nastaveni zelene slozky barvy pixelu
    pos++;
    if (p->pixels[pos]<256-db) p->pixels[pos]+=db;// nastaveni modre slozky barvy pixelu
}



//-----------------------------------------------------------------------------
// Vykresleni Sierpinskeho trojuhelniku pomoci linearizovaneho systemu
// iterovanych funkci L-IFS
//-----------------------------------------------------------------------------
void recalcL_IFS( pixmap *pix,                      // pixmapa pro vykreslovani
                  int    maxiter,                   // maximalni pocet iteraci
                  double scale,                     // meritko obrazce
                  double xpos,                      // posun obrazce
                  double ypos,                    
                  double ksi,                       // konstanta ovlivnujici tvar fraktalu
                  int    rf, int gf, int bf,        // priznaky barvovych slozek
                  int    dr, int dg, int db,        // prirustky barvovych slozek
                  DrawType drawType)                // zpusob vykresleni
{                                                 
    int    iter=0;                                  // pocitadlo iteraci
    int    threshold=50;                            // hranice poctu iteraci pro vykreslovani
                                                  
    double x, y;                                    // poloha iterovaneho bodu
    double xn, yn;                                  // nova poloha iterovaneho bodu
    int    k;                                       // cislo vybraneho ridiciho bodu
                                                  
    unsigned char red=rf ? dr : 0;                  // realne prirustky barvovych slozek
    unsigned char green=gf ? dg : 0;
    unsigned char blue=bf ? db : 0;

    unsigned char pal[8][3]={                       // barvova paleta
        {0xff, 0x00, 0x00},
        {0x00, 0xff, 0x00},
        {0x00, 0x00, 0xff},
        {0xff, 0xff, 0x00},
        {0x00, 0xff, 0xff},
        {0xff, 0x00, 0xff},
        {0xff, 0xff, 0xff},
        {0x80, 0x80, 0x80},
    };

    double IFS_sierpinsky[][7]={                    // ridici body Sierpinskeho trojuhelniku
        { 256,  366},
        {  56,   20},
        { 456,   20}
    };

    x=0;
    y=0;                                            // nastaveni pocatecni polohy bodu
    srand(0);

    while (iter++<maxiter*100) {                    // iteracni smycka
        k=rand()%3;
        xn=x*(1.0-ksi)+ksi*IFS_sierpinsky[k][0];
        yn=y*(1.0-ksi)+ksi*IFS_sierpinsky[k][1];
        if (iter>threshold) {                       // je-li dosazeno hranice iteraci
            switch (drawType) {                     // vyber vykreslovaciho rezimu
                case IterPutPixel:
                    putpixel(pix, xn*scale+xpos, yn*scale+ypos, rf ? 0xff:0x00, gf ? 0xff:0x00, bf ? 0xff:0x00);
                    break;
                case IterAddPixel:
                    addpixel(pix, xn*scale+xpos, yn*scale+ypos, red, green, blue);
                    break;
                case TransfPutPixel:
                    putpixel(pix, xn*scale+xpos, yn*scale+ypos, pal[k&7][0], pal[k&7][1], pal[k&7][2]);
                    break;
                case TransfAddPixel:
                    addpixel(pix, xn*scale+xpos, yn*scale+ypos, (!!pal[k&7][0])*dr, (!!pal[k&7][1])*dg, (!!pal[k&7][2])*db);
                    break;
                default:
                    break;
            }
        }
        x=xn;
        y=yn;
    }
}



//-----------------------------------------------------------------------------
// Vykresleni retezce na obrazovku
//-----------------------------------------------------------------------------
void drawString(const int x, const int y,                    // umisteni retezce
                const float r, const float g, const float b, // barva pisma
                char *str)                                   // ukazatel na retezec
{
    char *c;
    glColor3f(r, g, b);
    glRasterPos2i(x, y);
    for (c=str; *c!=0; c++) {
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, *c);
    }
}



//-----------------------------------------------------------------------------
// Vypis informaci o vykreslovanem fraktalu
//-----------------------------------------------------------------------------
void drawInfo(int maxiter, double xpos, double ypos, double scale, int r, int g, int b, int deltar, int deltag, int deltab, DrawType drawType, double ksi)
{
#define drawString2(x, y, r, g, b, str) drawString((x)+1, (y), 0.0, 0.0, 0.0, (str)); drawString((x), (y)+1, (r), (g), (b), (str));
    char str[100];
    sprintf(str, "[Home][End]   ksi = %3.2f", ksi);
    drawString2( 10, 96, 0.0, 1.0, 1.0, str);
    sprintf(str, "[F1] draw:   IterPutPixel:   %s", drawType==IterPutPixel ? "set":"");
    drawString2( 10, 80, 0.2, 1.0, 0.8, str);
    sprintf(str, "[F2] draw:   IterAddPixel:   %s", drawType==IterAddPixel ? "set":"");
    drawString2( 10, 64, 0.4, 1.0, 0.6, str);
    sprintf(str, "[F3] draw:   TransfPutPixel: %s", drawType==TransfPutPixel ? "set":"");
    drawString2( 10, 48, 0.6, 1.0, 0.4, str);
    sprintf(str, "[F4] draw:   TransfAddPixel: %s", drawType==TransfAddPixel ? "set":"");
    drawString2( 10, 32, 0.8, 1.0, 0.2, str);
    sprintf(str, "[<][>][,][.] maxiter = %d", maxiter*10);
    drawString2( 10, 16, 1.0, 1.0, 0.0, str);

    sprintf(str, "[PgUp][PgDn]  scale = %4.2f ", scale);
    drawString2(320, 96, 1.0, 0.0, 1.0, str);
    sprintf(str, "[Arrows]      pan = %5.3f, %5.3f", xpos, ypos);
    drawString2(320, 80, 0.8, 0.2, 1.0, str);
    sprintf(str, "[R][G][B]     colors = %d %d %d", r, g, b);
    drawString2(320, 64, 0.6, 0.4, 1.0, str);
    sprintf(str, "[F5][F6]      delta R = %d", deltar);
    drawString2(320, 48, 0.4, 0.6, 1.0, str);
    sprintf(str, "[F7][F8]      delta G = %d", deltag);
    drawString2(320, 32, 0.2, 0.8, 1.0, str);
    sprintf(str, "[F9][F10]     delta B = %d", deltab);
    drawString2(320, 16, 0.0, 1.0, 1.0, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu
    pixIFS=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
}



//-----------------------------------------------------------------------------
// Nastaveni souradneho systemu v zavislosti na velikosti okna
//-----------------------------------------------------------------------------
void onResize(int w, int h)                     // argumenty w a h reprezentuji novou velikost okna
{
    glViewport(0, 0, w, h);                     // viditelna oblast pres cele okno
    glMatrixMode(GL_PROJECTION);                // zacatek modifikace projekcni matice
    glLoadIdentity();                           // vymazani projekcni matice (=identita)
    glOrtho(0, w, 0, h, -1, 1);                 // mapovani abstraktnich souradnic do souradnic okna
}



//-----------------------------------------------------------------------------
// Tato callback funkce je zavolana pri kazdem prekresleni okna
//-----------------------------------------------------------------------------
void onDisplay(void)
{
    glClear(GL_COLOR_BUFFER_BIT);               // vymazani vsech bitovych rovin barvoveho bufferu
    glDrawBuffer(GL_BACK);                      // pixmapa se bude kreslit do zadniho barvoveho bufferu
    if (redraw) {
        clearPixmap(pixIFS);                    // vymazani pixmapy a prepocet fraktalu
        recalcL_IFS(pixIFS, maxiter, scale, xpos, ypos, ksi, rf, gf, bf, deltar, deltag, deltab, drawType);// prepocet fraktalu
        redraw=0;
    }
    glRasterPos2i(0, WINDOW_HEIGHT-PIXMAP_HEIGHT); // nastaveni souradnic leveho spodniho rohu pixmapy
    drawPixmap(pixIFS);                         // vykresleni pixmapy
    glRasterPos2i(0, 0);
    drawInfo(maxiter, xpos, ypos, scale, rf, gf, bf, deltar, deltag, deltab, drawType, ksi);
    glFlush();                                  // provedeni a vykresleni vsech zmen
    glutSwapBuffers();
}



//-----------------------------------------------------------------------------
// Tato callback funkce je zavolana pri stlaceni ASCII klavesy
//-----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void onKeyboard(unsigned char key, int x, int y)
{
    key=(key>='A' && key<='Z') ? key-'A'+'a': key;
    switch (key) {
        case 27:                                                              // pokud byla stlacena klavesa ESC, konec programu
        case 'q': exit(0);                                             break; // totez co klavesa ESC
        case 's': savePixmap(pixIFS, FILE_NAME);                       break; // ulozeni pixmapy
        case '<': if (maxiter>1000)   maxiter-=1000; redraw=1; glutPostRedisplay();  break; 
        case ',': if (maxiter>100)    maxiter-=100;   redraw=1; glutPostRedisplay(); break; // zmena poctu iteraci
        case '>': maxiter+=1000; redraw=1; glutPostRedisplay();                      break; 
        case '.': maxiter+=100; redraw=1; glutPostRedisplay();                       break; 
        case 'r': rf=!rf;                        redraw=1; glutPostRedisplay();      break; // priznaky barvovych slozek
        case 'g': gf=!gf;                        redraw=1; glutPostRedisplay();      break;
        case 'b': bf=!bf;                        redraw=1; glutPostRedisplay();      break;
        default:                                                                     break; 
    }
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



//-----------------------------------------------------------------------------
// Tato callback funkce je zavolana pri stlaceni non-ASCII klavesy
//-----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void onSpecial(int key, int x, int y)
{
    // posun fraktalu a zmena meritka
    switch (key) {
        case GLUT_KEY_LEFT:      xpos-=5;                         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_RIGHT:     xpos+=5;                         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_UP:        ypos+=5;                         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_DOWN:      ypos-=5;                         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_PAGE_UP:   scale*=1.1;                      redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_PAGE_DOWN: if (scale>1) scale/=1.1;         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_HOME:      ksi-=0.01; if (ksi<0.0) ksi=0.0; redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_END:       ksi+=0.01; if (ksi>1.0) ksi=1.0; redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F1:        drawType=IterPutPixel ;          redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F2:        drawType=IterAddPixel;           redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F3:        drawType=TransfPutPixel;         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F4:        drawType=TransfAddPixel;         redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F5:        if (deltar>1) deltar--;          redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F6:        deltar++;                        redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F7:        if (deltag>1) deltag--;          redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F8:        deltag++;                        redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F9:        if (deltab>1) deltab--;          redraw=1; glutPostRedisplay(); break;
        case GLUT_KEY_F10:       deltab++;                        redraw=1; glutPostRedisplay(); break;
        default:                                                                                 break;
    }
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



//-----------------------------------------------------------------------------
// Hlavni funkce konzolove aplikace
//-----------------------------------------------------------------------------
int main(int argc, char **argv)
{
    glutInit(&argc, argv);                      // inicializace knihovny GLUT
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    glutCreateWindow(WINDOW_TITLE);             // vytvoreni okna pro kresleni
    glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT);// zmena velikosti okna
    glutPositionWindow(100, 100);               // pozice leveho horniho rohu okna
    glutDisplayFunc(onDisplay);                 // registrace funkce volane pri prekreslovani okna
    glutReshapeFunc(onResize);                  // registrace funkce volane pri zmene velikosti okna
    glutKeyboardFunc(onKeyboard);               // registrace funkce volane pri stlaceni klavesy
    glutSpecialFunc(onSpecial);                 // registrace funkce volane pri stlaceni specialni klavesy
    onInit();                                   // inicializace vykreslovani
    glutMainLoop();                             // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                   // navratova hodnota vracena operacnimu systemu
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

