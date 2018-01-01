//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 48.3
// Autor: Pavel Tisnovsky
//
// Vykresleni plasmy pomoci spektralni syntezy (2D syntezy).
// Pomoci klaves [A] a [S] je mozne menit celkovy pocet koeficientu Fourierovy
// transformace, klavesy [Z] a [X] slouzi k urceni Hurstova koeficientu a tim
// i fraktalni dimenze vytvorene krivky.
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

#define WINDOW_TITLE    "Fraktaly 48.3"         // titulek okna
#define WINDOW_WIDTH    256                     // pocatecni velikost okna
#define WINDOW_HEIGHT   356

#define PIXMAP_WIDTH    256                     // sirka pixmapy
#define PIXMAP_HEIGHT   256                     // vyska pixmapy
#define FILE_NAME       "fraktaly48_3.tga"      // jmeno souboru s ulozenym obrazkem

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

pixmap *pix;
float h=0.5;                                    // Hurstuv exponent
int   n=10;                                     // pocet koeficientu spektralni syntezy



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
// Vygenerovani nahodneho cisla v rozsahu 0..1 s pribliznym Gaussovym rozlozenim
//-----------------------------------------------------------------------------
float randomGauss(void)
{
#define N 50
    float sum=0.0;
    int   i;
    for (i=0; i<N; i++)
        sum+=(float)rand()/(float)RAND_MAX;
    return sum/N;
}



//-----------------------------------------------------------------------------
// Vygenerovani nahodneho cisla v rozsahu 0..1 s rovnomernym rozlozenim
//-----------------------------------------------------------------------------
float randomN(void)
{
    return (float)rand()/(float)RAND_MAX;
}



//-----------------------------------------------------------------------------
// Spektralni synteza v 2D
//-----------------------------------------------------------------------------
void spectralSynthesis2D(void)
{
#define PI 3.1415927
    float bitmap[PIXMAP_HEIGHT][PIXMAP_WIDTH];
    float min=1e10, max=-1e10;              // pro prepocet intenzit pixelu
    float fmin=1e10, fmax=-1e10;            // pro prepocet intenzit pixelu
    
    float A[n/2][n/2];                      // koeficienty Ak
    float B[n/2][n/2];                      // koeficienty Bk
    float beta=2.0*h+1;                     // promenna svazana s Hurstovym koeficientem
    int   i, j, k, l;                       // pocitadla smycek

    for (j=0; j<PIXMAP_HEIGHT; j++)         // vymazani pracovni bitmapy
        for (i=0; i<PIXMAP_WIDTH; i++)
            bitmap[j][i]=0.0;

    srand(123456);
    for (j=0; j<n/2; j++) {                 // vypocet koeficientu Ak a Bk
        for (i=0; i<n/2; i++) {
            float rad_i=pow((i+1), -beta/2.0)*randomGauss();
            float rad_j=pow((j+1), -beta/2.0)*randomGauss();
            float phase_i=2.0*PI*randomN();
            float phase_j=2.0*PI*randomN();
            A[j][i]=rad_i*cos(phase_i)*rad_j*cos(phase_j);
            B[j][i]=rad_i*sin(phase_i)*rad_j*sin(phase_j);
        }
    }

    for (j=0; j<PIXMAP_HEIGHT; j++) {       // generovani plasmy
        for (i=0; i<PIXMAP_WIDTH; i++) {
            float z=0;
            for (k=0; k<n/2; k++) {         // inverzni Fourierova transformace
                for (l=0; l<n/2; l++) {
                    float u=(i-n/2)*2.0*PI/PIXMAP_WIDTH;  // transormace na
                    float v=(j-n/2)*2.0*PI/PIXMAP_HEIGHT; // stred obrazku
                    z+=A[k][l]*cos(k*u+l*v)+B[k][l]*sin(k*u+l*v);
                }
            }
            bitmap[j][i]=z;
        }
    }

    // ziskani statistiky o obrazku
    for (j=0; j<PIXMAP_HEIGHT; j++)
        for (i=0; i<PIXMAP_WIDTH; i++) {
            if (max<bitmap[j][i]) max=bitmap[j][i];
            if (min>bitmap[j][i]) min=bitmap[j][i];
        }
    //printf("min=%f\nmax=%f\n", min, max);

    // zmena kontrastu a kopie bitmapy
    for (j=0; j<PIXMAP_HEIGHT; j++)
        for (i=0; i<PIXMAP_WIDTH; i++) {
            float f=bitmap[j][i];
            f-=min;
            f*=255.0/(max-min);
            if (fmin>f) fmin=f;
            if (fmax<f) fmax=f;
            putpixel(pix, i, j, (int)f, (int)f, (int)f);
        }
    //printf("fmin=%f\nfmax=%f\n", fmin, fmax);
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
void drawInfo(int n, float Hexp)
{
    char str[100];
    sprintf(str, "[a][s]  N: %d", n);
    drawString(2, 42, 1.0, 1.0, 0.0, str);
    sprintf(str, "[z][x]  Hurst exponent: %4.2f", Hexp);
    drawString(2, 26, 1.0, 0.8, 0.2, str);
    sprintf(str, "Fractal dimension: %5.2f", 3.0-Hexp);
    drawString(2, 10, 1.0, 0.6, 0.4, str);
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
    drawInfo(n, h);
    spectralSynthesis2D();                      // vytvoreni obrazce spektralni syntezou
    glDrawBuffer(GL_BACK);                      // pixmapa se bude kreslit do zadniho barvoveho bufferu
    glRasterPos2i(0, 70);
    drawPixmap(pix);                            // vykresleni pixmapy
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
    if (key>='A' && key<='Z') key+='a'-'A';
    switch (key) {
        case 'q':
        case 27:  exit(0);  break;// pokud byla stlacena klavesa ESC, konec programu
        case 'w': savePixmap(pix, FILE_NAME); break;
        case 'a': if (n>3)   n-=2;   glutPostRedisplay(); break;
        case 's': if (n<50)  n+=2;   glutPostRedisplay(); break;
        case 'z': if (h>0.1) h-=0.1; glutPostRedisplay(); break;
        case 'x': if (h<1.0) h+=0.1; glutPostRedisplay(); break;
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
    onInit();                                   // inicializace vykreslovani
    glutMainLoop();                             // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                   // navratova hodnota vracena operacnimu systemu
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

