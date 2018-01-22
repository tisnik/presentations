//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// serial na http://www.root.cz
//
// Ukazkovy priklad cislo 72.1
// Autor: Pavel Tisnovsky
//
// Program po svem spusteni otevre hlavni okno a vykresli do nej jednorozmernou
// Perlinovu sumovou funkci. Blizsi informace o ovladani tohoto programu jsou
// uvedeny v 72.casti serialu o fraktalech.
//-----------------------------------------------------------------------------

#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <GL/glut.h>                            // hlavickovy soubor funkci GLUTu a OpenGL
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define WINDOW_TITLE    "Fraktaly 72.1"         // titulek okna
#define WINDOW_WIDTH    512                     // pocatecni velikost okna
#define WINDOW_HEIGHT   384

double alpha=2.0;
double beta=2.0;
int    n=5;

// Perlin pouziva funkci random(), my ji nahradime standardni funkci rand()
#define random() rand()

#include "perlin.h"
// toto sice neni moc koser, ale neni zapotrebi premyslet na linkerem :-)
#include "perlin.c"



//-----------------------------------------------------------------------------
// Prekresleni jednorozmerne Perlinovy sumove funkce
//-----------------------------------------------------------------------------
void recalcPerlinNoise1D(double alpha, double beta, int n)
{
    int i;
    double x=-5.0, y;                           // pocatecni hodnota souradnice x
    int width=glutGet(GLUT_WINDOW_WIDTH);       // sirka okna
    int height=glutGet(GLUT_WINDOW_HEIGHT);     // vyska okna
    glColor3f(1.0f, 1.0f, 1.0f);
    glBegin(GL_LINE_STRIP);                     // zacatek vykreslovani lomene cary (polycary)
    for (i=0; i<width; i++) {
        y=PerlinNoise1D(x, alpha, beta, n);     // vypocet Perlinovy funkce
        y*=(double)height/2.0;                  // zmena amplitudy podle vysky okna
        y+=height>>1;                           // posun ve vertikalnim smeru do stredu okna
        glVertex2f(i, y);                       // pripojeni dalsi casti lomene cary
        x+=10.0/(double)width;                  // prechod na dalsi souradnici v horizontalnim smeru
    }
    glEnd();                                    // konec vykreslovani lomene cary
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
// Vypis informaci o vykreslovane sumove funkci
//-----------------------------------------------------------------------------
void drawInfo(double alpha, double beta, int n)
{
    char str[100];
    sprintf(str, "[1][2]  alpha = %4.1f", alpha);
    drawString(10, 48, 1.0, 1.0, 0.0, str);
    sprintf(str, "[3][4]  beta =  %4.1f" , beta);
    drawString(10, 32, 0.6, 1.0, 0.2, str);
    sprintf(str, "[5][6]  n = %d ", n);
    drawString(10, 16, 0.2, 1.0, 0.6, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu

    recalcPerlinNoise1D(alpha, beta, n);
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
    glDrawBuffer(GL_FRONT);                     // pixmapa se bude kreslit do predniho barvoveho bufferu
    glRasterPos2i(0, 0);                        // nastaveni souradnic leveho spodniho rohu pixmapy
    recalcPerlinNoise1D(alpha, beta, n);        // prepocet Perlinovy sumove funkce
    drawInfo(alpha, beta, n);                   // vypis informaci o diagramu
    glFlush();                                  // provedeni a vykresleni vsech zmen
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
        case 27:                                                         // pokud byla stlacena klavesa ESC, konec programu
        case 'q': exit(0);                                        break; // totez co klavesa ESC
        case 'f': glutFullScreen();                               break; // prepnuti okna na celou obrazovku
        case 'w': glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT); break; // prepnuti okna na puvodni velikost
        case '1': alpha-=0.5;    glutPostRedisplay();             break; // zmena parametru alpha
        case '2': alpha+=0.5;    glutPostRedisplay();             break;
        case '3': beta-=0.5;     glutPostRedisplay();             break; // zmena parametru beta
        case '4': beta+=0.5;     glutPostRedisplay();             break;
        case '5': if (n>0) n--;  glutPostRedisplay();             break; // zmena parametru n
        case '6': n++;           glutPostRedisplay();             break;
        default:                                                  break;
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
    glutInit(&argc, argv);                         // inicializace knihovny GLUT
    glutCreateWindow(WINDOW_TITLE);                // vytvoreni okna pro kresleni
    glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT);// zmena velikosti okna
    glutPositionWindow(100, 100);                  // pozice leveho horniho rohu okna
    glutDisplayFunc(onDisplay);                    // registrace funkce volane pri prekreslovani okna
    glutReshapeFunc(onResize);                     // registrace funkce volane pri zmene velikosti okna
    glutKeyboardFunc(onKeyboard);                  // registrace funkce volani pri stlaceni klavesy
    onInit();                                      // inicializace vykreslovani
    glutMainLoop();                                // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                      // navratova hodnota vracena operacnimu systemu
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

