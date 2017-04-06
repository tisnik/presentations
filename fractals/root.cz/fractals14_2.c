//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 14.2
// Autor: Pavel Tisnovsky
//
// Vykresleni Mandelbrotovy mnoziny s moznosti zmeny pohledu na mnozinu a
// parametrizace funkci pouzitych pro vypocet barev.
// Pixmapu s vykreslenym fraktalem je mozne ulozit do souboru ve formatu TGA
// pomoci klavesove zkratky [S].
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

#define WINDOW_TITLE    "Fraktaly 14.2"         // titulek okna
#define WINDOW_WIDTH    512                     // pocatecni velikost okna
#define WINDOW_HEIGHT   384
#define FILE_NAME       "fraktaly142.tga"       // jmeno souboru pro ulozeni pixmapy

#define PIXMAP_WIDTH    512                     // sirka pixmapy
#define PIXMAP_HEIGHT   384                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

pixmap *pix;

int    palette=0;                               // barvova paleta
int    maxiter=128;                             // maximalni pocet iteraci
int    rf=1, gf=1, bf=1;                        // priznaky barvovych slozek
double scale=1.0;                               // meritko fraktalu
double xpos=0.0;                                // posun fraktalu
double ypos=0.0;                                // posun fraktalu

// sirka a vyska zakladniho obrazce v komplexni rovine
#define WIDTH   2.0
#define HEIGHT  1.5



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
// Funkce pro vypocet pozice rohu vykreslovaneho obrazku ze zadaneho stredu
// a meritka
//-----------------------------------------------------------------------------
void calcCorner(double xpos, double ypos, double scale, 
                double *xmin,  double *ymin,  double *xmax, double *ymax)
{
    *xmin=xpos-WIDTH/scale;
    *ymin=ypos-HEIGHT/scale;
    *xmax=xpos+WIDTH/scale;
    *ymax=ypos+HEIGHT/scale;
}



//-----------------------------------------------------------------------------
// Prekresleni Mandelbrotovy mnoziny
//-----------------------------------------------------------------------------
void recalcMandelbrot( pixmap *pix,             // pixmapa pro vykreslovani
                  int    maxiter,               // maximalni pocet iteraci
                  double scale,                 // meritko obrazce
                  double xpos,                  // posun obrazce
                  double ypos,
                  int    palette,               // barvova paleta
                  int    rf, int gf, int bf)    // priznaky barvovych slozek
{
    double zx, zy, zx2, zy2;                    // slozky komplexni promenne Z a Z^2
    double cx, cy;                              // slozky komplexni konstanty C
    double cx0, cy0;
    double xmin, ymin, xmax, ymax;              // rohy vykreslovaneho obrazce v komplexni
                                                // rovine
    int    x, y;                                // pocitadla sloupcu a radku v pixmape
    int    iter;                                // pocitadlo iteraci
    unsigned char r, g, b;

    calcCorner(xpos, ypos, scale, &xmin, &ymin, &xmax, &ymax);
    cy0=ymin;
    for (y=0; y<pix->height; y++) {             // pro vsechny radky v pixmape
        cx0=xmin;
        for (x=0; x<pix->width; x++) {          // pro vsechny pixely na radku
            cx=cx0;                             // nastavit pocatecni hodnotu Z(0)
            cy=cy0;
            zx=zy=0.0;                          // nastaveni nuloveho orbitu
            for (iter=0; iter<maxiter; iter++) {// iteracni smycka
                zx2=zx*zx;                      // zkraceny vypocet druhe mocniny slozek Z
                zy2=zy*zy;
                if (zx2+zy2>4.0) break;         // kontrola prekroceni meze divergence
                zy=2.0*zx*zy+cy;                // vypocet Z(n+1)
                zx=zx2-zy2+cx;
            }
            switch (palette) {                  // vykresleni pixelu s vybranou barvovou paletou
                case 0:
                    r=iter<<1;
                    g=iter<<1;
                    b=iter<<1;
                    break;
                case 1:
                    r=iter*10.0;
                    g=127+127.0*sin(iter/30.0);
                    b=127+127.0*sin(iter/10.0);
                    break;
                case 2:
                    r=127+127.0*sin(iter/30.0);
                    g=iter*10;
                    b=127+127.0*sin(iter/10.0);
                    break;
                case 3:
                    r=127+127.0*sin(iter/30.0);
                    g=127+127.0*sin(iter/10.0);
                    b=iter*10.0;
                    break;
                case 4:
                    r=127+127.0*sin(iter/30.0);
                    g=iter*20;
                    b=127+127.0*sin(iter/10.0);
                    break;
                case 5:
                    r=iter*5;
                    g=255-iter*7;
                    b=iter*9;
                    break;
                case 6:
                    r=127+127.0*sin(iter/30.0);
                    g=iter*20;
                    b=127-127.0*sin(iter/30.0);
                    break;
                case 7:
                    r=127-127.0*sin(iter/30.0);
                    g=iter*10;
                    b=127+127.0*sin(iter/10.0);
                    break;
                case 8:
                    r=127+127.0*sin(iter/30.0);
                    g=127-127.0*sin(iter/10.0);
                    b=iter*10;
                    break;
                case 9:
                    r=127-127.0*sin(iter/10.0);
                    g=iter*20;
                    b=127+127.0*sin(iter/20.0);
                    break;
            }
            r=r*rf;                             // uzivatelem rizene vynulovani
            g=g*gf;                             // vybranych barvovych slozek
            b=b*bf;
            putpixel(pix, x, y, r, g, b);
            cx0+=(xmax-xmin)/pix->width;        // posun na dalsi bod na radku
        }
        cy0+=(ymax-ymin)/pix->height;           // posun na dalsi radek
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
void drawInfo(int maxiter, double xpos, double ypos, double scale, int palette, int r, int g, int b)
{
    char str[100];
    sprintf(str, "[R][G][B]  colors = %d %d %d", r, g, b);
    drawString(11, 79, 0.0, 0.0, 0.0, str);     // stinovani
    drawString(10, 80, 0.6, 1.0, 0.6, str);
    sprintf(str, "[0]-[9]    palette = %d", palette);
    drawString(11, 63, 0.0, 0.0, 0.0, str);
    drawString(10, 64, 0.6, 1.0, 0.6, str);
    sprintf(str, "[<][>]     maxiter = %d", maxiter);
    drawString(11, 47, 0.0, 0.0, 0.0, str);
    drawString(10, 48, 0.6, 1.0, 0.6, str);
    sprintf(str, "[PgUp][PgDn]  scale = %4.2f ", scale);
    drawString(11, 31, 0.0, 0.0, 0.0, str);
    drawString(10, 32, 0.4, 1.0, 0.8, str);
    sprintf(str, "[Arrows]  pan = %5.3f, %5.3f", xpos, ypos);
    drawString(11, 15, 0.0, 0.0, 0.0, str);
    drawString(10, 16, 0.2, 1.0, 1.0, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu

    pix=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
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
    glRasterPos2i(0, 0);                        // nastaveni souradnic leveho spodniho rohu pixmapy
    clearPixmap(pix);                           // vymazani pracovni pixmapy (nastaveni pixelu na cernou barvu)
    recalcMandelbrot(pix, maxiter, scale, xpos, ypos, palette, rf, gf, bf);// prepocet fraktalu
    drawPixmap(pix);                            // vykresleni pixmapy
    drawInfo(maxiter, xpos, ypos, scale, palette, rf, gf, bf);
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
    if (key>='0' && key<='9') { palette=key-'0'; glutPostRedisplay(); }       // nastaveni barvove palety
    switch (key) {
        case 27:                                                              // pokud byla stlacena klavesa ESC, konec programu
        case 'q': exit(0);                                             break; // totez co klavesa ESC
        case 's': savePixmap(pix, FILE_NAME);                          break; // ulozeni pixmapy
        case '<': if (maxiter>10)   maxiter-=10; glutPostRedisplay();  break; 
        case ',': if (maxiter>1)    maxiter--;   glutPostRedisplay();  break; // zmena poctu iteraci
        case '>': if (maxiter<246)  maxiter+=10; glutPostRedisplay();  break; 
        case '.': if (maxiter<255)  maxiter++;   glutPostRedisplay();  break; 
        case 'r': rf=!rf;                        glutPostRedisplay();  break; // priznaky barvovych slozek
        case 'g': gf=!gf;                        glutPostRedisplay();  break;
        case 'b': bf=!bf;                        glutPostRedisplay();  break;
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
        case GLUT_KEY_LEFT:      xpos-=0.05/scale; glutPostRedisplay();           break;
        case GLUT_KEY_RIGHT:     xpos+=0.05/scale; glutPostRedisplay();           break;
        case GLUT_KEY_UP:        ypos+=0.05/scale; glutPostRedisplay();           break;
        case GLUT_KEY_DOWN:      ypos-=0.05/scale; glutPostRedisplay();           break;
        case GLUT_KEY_PAGE_UP:   scale*=1.1; glutPostRedisplay();                 break;
        case GLUT_KEY_PAGE_DOWN: if (scale>1) scale/=1.1; glutPostRedisplay();    break;
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

