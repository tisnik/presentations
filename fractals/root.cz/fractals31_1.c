//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Autor: Pavel Tisnovsky
//
// Vykresleni jednoducheho obrazce pomoci systemu iterovanych funkci IFS.
// Pixmapu s vykreslenym fraktalem je mozne ulozit do souboru ve formatu TGA
// pomoci klavesove zkratky [S]. Zmena barvove palety se provadi klavesami [0]-[9]
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

#define WINDOW_TITLE    "Fraktaly 31.1"         // titulek okna
#define WINDOW_WIDTH    640                     // pocatecni velikost okna
#define WINDOW_HEIGHT   460
#define FILE_NAME       "fraktaly311.tga"       // jmeno souboru pro ulozeni pixmapy

#define PIXMAP_WIDTH    512                     // sirka pixmapy
#define PIXMAP_HEIGHT   384                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

pixmap *pixIFS;                                 // pixmapa pro obrazek IFS fraktalu

int    maxiter=1000;                            // maximalni pocet iteraci
double scale=30.0;                              // meritko fraktalu
double xpos=0.0;                                // posun fraktalu
double ypos=-150.0;                             // posun fraktalu
int    redraw=1;



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
    memset(p->pixels, 0xff, 3*p->width*p->height);
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



#define random(x) (rand()*(x)/RAND_MAX)



//-----------------------------------------------------------------------------
// Prekresleni systemu iterovanych funkci IFS
//-----------------------------------------------------------------------------
void recalcIFS(pixmap *pix,                     // pixmapa pro vykreslovani
                  int    maxiter,               // maximalni pocet iteraci
                  double scale,                 // meritko obrazce
                  double xpos,                  // posun obrazce
                  double ypos)
{
    float  t[4][2][3];                          // transformacni matice
    float  p[4];                                // vektor pravdepodobnosti transformaci

    int    iter=0;                              // pocitadlo iteraci
    int    threshold=10;                        // hranice poctu iteraci pro vykreslovani

    float  x, y, hlp;                           // poloha iterovaneho bodu
    float  pp;                                  // pravdepodobnost pro vyber transformace
    float  sum;                
    int    k;                                   // cislo vybrane transformace

    // transformacni matice a vektor pravdepodobnosti transformaci pro fraktalni kapradinu
    t[0][0][0]= 0.000;   t[0][0][1]= 0.000;   t[0][0][2]= 0.000;
    t[0][1][0]= 0.000;   t[0][1][1]= 0.160;   t[0][1][2]= 0.000;

    t[1][0][0]= 0.200;   t[1][0][1]=-0.260;   t[1][0][2]= 0.000;
    t[1][1][0]= 0.230;   t[1][1][1]= 0.220;   t[1][1][2]= 1.600;

    t[2][0][0]=-0.150;   t[2][0][1]= 0.280;   t[2][0][2]= 0.000;
    t[2][1][0]= 0.260;   t[2][1][1]= 0.240;   t[2][1][2]= 0.440;

    t[3][0][0]= 0.850;   t[3][0][1]= 0.040;   t[3][0][2]= 0.000;
    t[3][1][0]=-0.040;   t[3][1][1]= 0.850;   t[3][1][2]= 1.600;

    p[0]=0.01;
    p[1]=0.07;
    p[2]=0.08;
    p[3]=0.84;

    x=0;
    y=0;                                        // nastaveni pocatecni polohy bodu
    srand(0);
    xpos+=pix->width/2;                         // posun do stredu okna
    ypos+=pix->height/2;
    while (iter++<maxiter*100) {                // iteracni smycka
        pp=(float) random (255) / 255.0;        // p lezi v rozsahu 0.0-1.0
        k=0;                                    // promenna cyklu vyhledani transformace
        sum=0;
        while (sum<=pp) {                       // podle nahodneho cisla
            sum=sum+p[k];                       // vybrat transformaci
            k++;
        }                                       // k urcuje index transformace
        k--;                                    // uprava ze smycky while
        hlp=t[k][0][0]*x+t[k][0][1]*y+t[k][0][2]; // provedeni
        y  =t[k][1][0]*x+t[k][1][1]*y+t[k][1][2]; // transformace
        x  =hlp;
        if (iter > threshold)                   // je-li dosazeno hranice iteraci
            putpixel(pix, x*scale+xpos, y*scale+ypos, 0x00, 0x00, 0x00); // vykresleni pixelu
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
void drawInfo(int maxiter, double xpos, double ypos, double scale)
{
    char str[100];
    sprintf(str, "[<][>]     maxiter = %d", maxiter*10);
    drawString(11, 63, 0.5, 0.0, 0.0, str);
    sprintf(str, "[PgUp][PgDn]  scale = %4.2f ", scale);
    drawString(11, 47, 0.0, 0.5, 0.0, str);
    sprintf(str, "[Arrows]  pan = %5.3f, %5.3f", xpos, ypos);
    drawString(11, 31, 0.0, 0.0, 0.5, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(1.0f, 1.0f, 1.0f, 0.0f);       // barva pozadi
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
        clearPixmap(pixIFS);
        recalcIFS(pixIFS, maxiter, scale, xpos, ypos);// prepocet fraktalu
        redraw=0;
    }
    glRasterPos2i(0, WINDOW_HEIGHT-PIXMAP_HEIGHT); // nastaveni souradnic leveho spodniho rohu pixmapy
    drawPixmap(pixIFS);                      // vykresleni pixmapy
    glRasterPos2i(0, 0);
    drawInfo(maxiter, xpos, ypos, scale);
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
        case '<': if (maxiter>100)   maxiter-=100; redraw=1; glutPostRedisplay();  break; 
        case ',': if (maxiter>10)    maxiter-=10;  redraw=1; glutPostRedisplay();  break; // zmena poctu iteraci
        case '>': maxiter+=100; redraw=1; glutPostRedisplay();         break; 
        case '.': maxiter+=10;  redraw=1; glutPostRedisplay();         break; 
        default:                                                       break; 
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
        case GLUT_KEY_LEFT:      xpos-=5; redraw=1; glutPostRedisplay();           break;
        case GLUT_KEY_RIGHT:     xpos+=5; redraw=1; glutPostRedisplay();           break;
        case GLUT_KEY_UP:        ypos+=5; redraw=1; glutPostRedisplay();           break;
        case GLUT_KEY_DOWN:      ypos-=5; redraw=1; glutPostRedisplay();           break;
        case GLUT_KEY_PAGE_UP:   scale*=1.1; redraw=1; glutPostRedisplay();                 break;
        case GLUT_KEY_PAGE_DOWN: if (scale>1) scale/=1.1; redraw=1; glutPostRedisplay();    break;
        default:                                                                  break;
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

