//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 48.1
// Autor: Pavel Tisnovsky
//
// Vykresleni animace plasmy pomoci alternativni metody - deleni ctverce na dve
// poloviny a zvysovani/snizovani intenzit pixelu v obou polovinach. Animace je
// provedena prubeznym prekryvanim dvou obrazku s plasmou. Animace je mozne
// spustit a opetovne zastavit klavesou [S]. Pomoci klaves [1]-[4] se nastavuje
// faktor michani pro zdrojovou cast a pomoci klaves [5]-[8] faktor michani
// pro cast cilovou.
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
#include <limits.h>

#define WINDOW_TITLE    "Fraktaly 48.1"         // titulek okna
#define WINDOW_WIDTH    512+10                  // pocatecni velikost okna
#define WINDOW_HEIGHT   512+10

#define PIXMAP_WIDTH    512                     // sirka pixmapy
#define PIXMAP_HEIGHT   512                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

int blendSrc[]={
    GL_ZERO,
    GL_ONE,
    GL_DST_COLOR,
    GL_ONE_MINUS_DST_COLOR
};

int blendDst[]={
    GL_ZERO,
    GL_ONE,
    GL_SRC_COLOR,
    GL_ONE_MINUS_SRC_COLOR
};

pixmap *pix1;
pixmap *pix2;
int    maxiter=2000;
int    t=0;
int    stop=0;
int    src=2;
int    dst=2;



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
// Pridani poloroviny do pracovni bitmapy pomoci modifikovaneho Bresenhamova
// algoritmu pro rasterizaci usecky
//-----------------------------------------------------------------------------
void addHalfPlane(int bitmap[PIXMAP_HEIGHT][PIXMAP_WIDTH], int x1, int y1, int x2, int y2)
{
    int x, y;
    int i, j, deltax, deltay, numpixels;
    int d, dinc1, dinc2, xinc1, xinc2, yinc1, yinc2;
    int dir;

    dir=rand()%2;                           // smer "kladne" a "zaporne" poloroviny

    // otestovat mezni stavy
    if (x1<0 || x2<0 || y1<0 || y2<0) return;
    if (x1>=PIXMAP_WIDTH || x2>=PIXMAP_WIDTH || y1>=PIXMAP_HEIGHT || y2>=PIXMAP_HEIGHT) return;

    deltax=abs(x2-x1);                      // pouzito pro predikci v Bresenhamove algoritmu
    deltay=abs(y2-y1);

    if (deltax>=deltay) {                   // uhel je mensi nez +-45 stupnu
        numpixels=deltax;                   // celkovy pocet pixelu na usecce
        d=(deltay<<1)-deltax;               // predikce
        dinc1=deltay<<1;                    // zmena predikce v kazdem kroku
        dinc2=(deltay-deltax)<<1;
        xinc1=xinc2=1;
        yinc1=0;
        yinc2=1;
    }
    else {                                  // uhel je vetsi nez +-45 stupnu
        numpixels=deltay;                   // celkovy pocet pixelu na usecce
        d=(deltax<<1)-deltay;               // predikce
        dinc1=deltax<<1;                    // zmena predikce v kazdem kroku
        dinc2=(deltax-deltay)<<1;
        xinc1=0;
        yinc1=yinc2=1;
        xinc2=1;
    }
    if (x2<x1) {                            // opacna orientace usecky:
        xinc1=-xinc1;                       // prohozeni x-ovych souradnic
        xinc2=-xinc2;
    }
    if (y2<y1) {                            // opacna orientace usecky:
        yinc1=-yinc1;                       // prohozeni y-ovych souradnic
        yinc2=-yinc2;
    }
    x=x1;                                   // nastaveni pocatecniho pixelu
    y=y1;
    for (i=0; i<numpixels; i++) {           // pro vsechny pixely na usecce
        if (deltax>=deltay) {               // mene nez 45 stupnu - vertikalni cary
            if (dir) {
                for (j=0; j<=y; j++)
                    bitmap[j][x]--;         // snizeni intenzity pixelu
                for (j=y; j<PIXMAP_HEIGHT; j++)
                    bitmap[j][x]++;         // zvyseni intenzity pixelu
            }
            else {
                for (j=0; j<=y; j++)
                    bitmap[j][x]++;         // zvyseni intenzity pixelu
                for (j=y; j<PIXMAP_HEIGHT; j++)
                    bitmap[j][x]--;         // snizeni intenzity pixelu
            }
        }
        else {                              // vice nez 45 stupnu - horizontalni cary
            if (dir) {
                for (j=0; j<=x; j++)
                    bitmap[y][j]--;         // snizeni intenzity pixelu
                for (j=x; j<PIXMAP_WIDTH; j++)
                    bitmap[y][j]++;         // zvyseni intenzity pixelu
            }
            else {
                for (j=0; j<=x; j++)
                    bitmap[y][j]++;         // zvyseni intenzity pixelu
                for (j=x; j<PIXMAP_WIDTH; j++)
                    bitmap[y][j]--;         // snizeni intenzity pixelu
            }
        }
        if (d<0) {                          // posun na dalsi pixel
            d+=dinc1;                       // podle predikce
            x+=xinc1;
            y+=yinc1;
        }
        else {
            d+=dinc2;
            x+=xinc2;
            y+=yinc2;
        }
    }
}



//-----------------------------------------------------------------------------
// Prekresleni fraktalni plasmy
//-----------------------------------------------------------------------------
void recalcFractal(pixmap *pix, int randSeed)
{
    int bitmap[PIXMAP_HEIGHT][PIXMAP_WIDTH];
    int i, x, y;           
    int min=INT_MAX, max=0;                 // pro zmenu kontrastu bitmapy
    float fmin=1e10, fmax=-1e10;            // pro prepocet intenzit pixelu
    int x1, y1, x2, y2;                     // souradnice generovanych bodu

    srand(randSeed);
    for (y=0; y<PIXMAP_HEIGHT; y++)         // vymazani pracovni bitmapy
        for (x=0; x<PIXMAP_WIDTH; x++)
            bitmap[y][x]=0;

    for (i=0; i<maxiter; i++) {             // iteracni smycka
        x1=rand()%PIXMAP_WIDTH;
        y1=0;
        x2=rand()%PIXMAP_WIDTH;
        y2=PIXMAP_HEIGHT-1;
        addHalfPlane(bitmap, x1, y1, x2, y2);// usecka z horniho k dolnimu okraji
        x1=0;
        y1=rand()%PIXMAP_HEIGHT;
        x2=PIXMAP_WIDTH-1;
        y2=rand()%PIXMAP_HEIGHT;
        addHalfPlane(bitmap, x1, y1, x2, y2);// usecka z leveho k pravemu okraji
        if (!(i%100)) printf("%i\t", i);
    }
    putchar('\n');
    
    // oprava intenzity rohoveho bodu
    bitmap[PIXMAP_HEIGHT-1][PIXMAP_WIDTH-1]=bitmap[PIXMAP_HEIGHT-2][PIXMAP_WIDTH-2];

    // ziskani statistiky o obrazku
    for (y=0; y<PIXMAP_HEIGHT; y++)
        for (x=0; x<PIXMAP_WIDTH; x++) {
            if (max<bitmap[y][x]) max=bitmap[y][x];
            if (min>bitmap[y][x]) min=bitmap[y][x];
        }
    printf("min=%d\nmax=%d\n", min, max);

    // zmena kontrastu a kopie bitmapy
    for (y=0; y<PIXMAP_HEIGHT; y++)
        for (x=0; x<PIXMAP_WIDTH; x++) {
            float f=bitmap[y][x];
            f-=min;
            f*=255.0/(max-min);
            if (fmin>f) fmin=f;
            if (fmax<f) fmax=f;
            putpixel(pix, x, y, (int)f, (int)f, (int)f);
        }
    printf("fmin=%f\nfmax=%f\n", fmin, fmax);
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
// Vypsani informaci o zadanych parametrech
//-----------------------------------------------------------------------------
void drawInfo(int x1, int y1, int x2, int y2)
{
    char *srcStr[]={
        "GL_ZERO",
        "GL_ONE",
        "GL_DST_COLOR",
        "GL_ONE_MINUS_DST_COLOR"
    };
    char *dstStr[]={
        "GL_ZERO",
        "GL_ONE",
        "GL_SRC_COLOR",
        "GL_ONE_MINUS_SRC_COLOR"
    };
    char str[100];
    drawString(10, 130, 0.8, 0.2, 0.8, "[1]-[4] source");
    drawString(10, 110, 1.0, 0.0, 1.0, srcStr[src]);
    drawString(10, 90, 1.0, 0.2, 0.8, "[5]-[8] destination");
    drawString(10, 70, 1.0, 0.4, 0.6, dstStr[dst]);
    sprintf(str, "[s]  %s", stop ? "stopped":"running");
    drawString(10, 50, 1.0, 0.6, 0.4, str);
    sprintf(str, "(x1, y1)=(%d,%d)", x1, y1);
    drawString(10, 30, 1.0, 0.8, 0.2, str);
    sprintf(str, "(x2, y2)=(%d,%d)", x2, y2);
    drawString(10, 10, 1.0, 1.0, 0.0, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu

    pix1=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
    pix2=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
    recalcFractal(pix1, 123);
    recalcFractal(pix2, 456);
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
#define RADIUS 100.0
    int x1, y1, x2, y2;
    glClear(GL_COLOR_BUFFER_BIT);               // vymazani vsech bitovych rovin barvoveho bufferu
    glDrawBuffer(GL_BACK);                      // pixmapa se bude kreslit do zadniho barvoveho bufferu

    x1=RADIUS+RADIUS*cos(t/10.0);               // pozice prvni pixmapy
    y1=RADIUS+RADIUS*sin(t/7.0);
    x2=RADIUS+RADIUS*sin(t/11.0);               // pozice druhe pixmapy
    y2=RADIUS+RADIUS*cos(t/13.0);
    glEnable(GL_SCISSOR_TEST);                  // orezani vykreslovani
    glScissor(RADIUS*2, RADIUS*2, PIXMAP_WIDTH, PIXMAP_HEIGHT);
    glRasterPos2i(x1, y1);                      // nastaveni souradnic leveho spodniho rohu pixmapy
    drawPixmap(pix1);                           // vykresleni pixmapy
    glEnable(GL_BLEND);
    glBlendFunc(blendSrc[src], blendDst[dst]);  // povoleni a nastaveni michaci funkce
    glRasterPos2i(x2, y2);                      // nastaveni souradnic leveho spodniho rohu pixmapy
    drawPixmap(pix2);                           // vykresleni pixmapy
    glDisable(GL_BLEND);
    glDisable(GL_SCISSOR_TEST);
    drawInfo(x1, y1, x2, y2);
    glFlush();                                  // provedeni a vykresleni vsech zmen
    glutSwapBuffers();
}



//-----------------------------------------------------------------------------
// Tato callback funkce je zavolana pri tiku casovace
//-----------------------------------------------------------------------------
void onTimer(int value)
{
    t++;
    glutPostRedisplay();
    if (!stop)
        glutTimerFunc(100, onTimer, 0);
}



//-----------------------------------------------------------------------------
// Tato callback funkce je zavolana pri stlaceni ASCII klavesy
//-----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void onKeyboard(unsigned char key, int x, int y)
{
    if (key>='A' && key<='Z') key+='a'-'A';
    if (key>='1' && key<='4') {          // nastaveni blendingu
        src=key-'1';
        return;
    }
    if (key>='5' && key<='8') {          // nastaveni blendingu
        dst=key-'5';
        return;
    }
    switch (key) {
        case 'q':
        case 27:  exit(0);  break;// pokud byla stlacena klavesa ESC, konec programu
        case 's': stop=!stop; if (!stop) glutTimerFunc(100, onTimer, 0); break;
        default:  break; 
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
    glutTimerFunc(100, onTimer, 0);             // registrace funkce volane pri tiku casovace
    onInit();                                   // inicializace vykreslovani
    glutMainLoop();                             // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                   // navratova hodnota vracena operacnimu systemu
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

