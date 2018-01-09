//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Demonstracni priklad 54.3
// Autor: Pavel Tisnovsky
//
// Vykresleni Hilbertovy krivky pomoci rekurzivniho algoritmu.
// Po prekladu a spusteni programu se rekurzivne vykresli Hilbertova krivka,
// jejiz velikost je zvolena tak, aby se presne vlezla do nastavene
// velikosti okna.
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

#define WINDOW_TITLE    "Fraktaly 54.3"         // titulek okna
#define WINDOW_WIDTH    512                     // pocatecni velikost okna
#define WINDOW_HEIGHT   512

#define MAX_LENGTH     500000                   // maximalni delka retezce

// hlavicky funkci
void hilbertA(int level);
void hilbertB(int level);
void hilbertC(int level);
void hilbertD(int level);
void gotoXY(int x, int y);
void lineRel(int deltaX, int deltaY);

int    itersCount=1;                            // pocet aplikaci prepisovaciho pravidla

int    dist0=WINDOW_WIDTH;
int    dist=WINDOW_WIDTH;
int    xx, yy;                                  // pozice grafickeho kurzoru



//-----------------------------------------------------------------------------
// Vykresleni casti 'A' Hilbertovy krivky
//-----------------------------------------------------------------------------
void hilbertA(int level)
{
    if (level>0) {
        hilbertB(level-1);    lineRel(0,dist);
        hilbertA(level-1);    lineRel(dist,0);
        hilbertA(level-1);    lineRel(0,-dist);
        hilbertC(level-1);
    }
}



//-----------------------------------------------------------------------------
// Vykresleni casti 'B' Hilbertovy krivky
//-----------------------------------------------------------------------------
void hilbertB(int level)
{
    if (level > 0) {
        hilbertA(level-1);    lineRel(dist,0);
        hilbertB(level-1);    lineRel(0,dist);
        hilbertB(level-1);    lineRel(-dist,0);
        hilbertD(level-1);
    }
}



//-----------------------------------------------------------------------------
// Vykresleni casti 'C' Hilbertovy krivky
//-----------------------------------------------------------------------------
void hilbertC(int level)
{
    if (level>0) {
        hilbertD(level-1);    lineRel(-dist,0);
        hilbertC(level-1);    lineRel(0,-dist);
        hilbertC(level-1);    lineRel(dist,0);
        hilbertA(level-1);
    }
}



//-----------------------------------------------------------------------------
// Vykresleni casti 'D' Hilbertovy krivky
//-----------------------------------------------------------------------------
void hilbertD(int level) {
    if (level > 0) {
        hilbertC(level-1);    lineRel(0,-dist);
        hilbertD(level-1);    lineRel(-dist,0);
        hilbertD(level-1);    lineRel(0,dist);
        hilbertB(level-1);
    }
}



//-----------------------------------------------------------------------------
// Presun grafickeho kurzoru na souradnice [x, y]
//-----------------------------------------------------------------------------
void gotoXY(int x, int y)
{
    xx=x;
    yy=y;
}



//-----------------------------------------------------------------------------
// Presun grafickeho kurzoru o vektor [deltaX, deltaY] s kreslenim
//-----------------------------------------------------------------------------
void lineRel(int deltaX, int deltaY)
{
    glVertex2i(xx, yy);
    xx+=deltaX;
    yy+=deltaY;
    glVertex2i(xx, yy);
}



//-----------------------------------------------------------------------------
// Prekresleni Hilbertovy krivky
//-----------------------------------------------------------------------------
void recalcHilbert(void)
{
    int i;
    int level=5;
    xx=yy=0;
    dist=dist0;
    // ziskat krok pro zadany pocet iteraci
    for (i=level; i>0; i--)
        dist/=2;
    // prvni uroven kresleni
    glColor3f(1.0f, 1.0f, 1.0f);
    glBegin(GL_LINES);
        gotoXY(dist/2, dist/2);
        hilbertA(level);
    glEnd();
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu
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
    recalcHilbert();                            // prekresleni Hilbertovy krivky
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
        case 27:                                // pokud byla stlacena klavesa ESC, konec programu
        case 'q': exit(0);               break; // totez co klavesa ESC
        default:                         break; 
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

