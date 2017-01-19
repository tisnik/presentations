//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 5.1
// Autor: Pavel Tisnovsky
//
// Program po svem spusteni otevre hlavni okno a vykresli do nej logistickou
// funkci. Ovladani aplikace pomoci klavesnice je popsano v pate casti
// serialu o fraktalech pouzivanych v pocitacove grafice.
//-----------------------------------------------------------------------------

#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <GL/glut.h>                            // hlavickovy soubor funkci GLUTu a OpenGL
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define WINDOW_TITLE    "Fraktaly 5.1"          // titulek okna
#define WINDOW_WIDTH    512                     // pocatecni velikost okna
#define WINDOW_HEIGHT   384

double x0=0.7;                                  // uroven populace v nultem kroku
int    yp=0;                                    // posun diagramu nahoru ci dolu
double gr0=1.0;                                 // posun populacniho rustu



//-----------------------------------------------------------------------------
// Prekresleni logisticke funkce
//-----------------------------------------------------------------------------
void recalcLogistic(double x0, double gr0, int yp)
{
    int i;
    double gr=gr0;                                     // hodnota velikosti rustu
    double x=x0, y;                                    // pocatecni hodnota x0
    glColor3f(1.0f, 1.0f, 1.0f);
    glBegin(GL_LINE_STRIP);                            // zacatek vykreslovani lomene cary
    for (i=8; i<glutGet(GLUT_WINDOW_WIDTH)-16; i+=8) { // vypocet pro vybranou hodnotu Gr
        x=gr*(x-x*x);                                  // hodnota funkce v dalsim kroku
        y=yp+((1.0+x)*glutGet(GLUT_WINDOW_HEIGHT)/2.0);
        glVertex2f(i, y);                              // pripojeni dalsi casti lomene cary
    }
    glEnd();
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
// Vypis informaci o vykreslovanem diagramu
//-----------------------------------------------------------------------------
void drawInfo(double x0, double gr0, int yp)
{
    char str[100];
    sprintf(str, "[1][2]  x0 = %f", x0);
    drawString(10, 48, 1.0, 1.0, 0.0, str);
    sprintf(str, "[j][k]  yp = %d" , yp);
    drawString(10, 32, 0.6, 1.0, 0.2, str);
    sprintf(str, "[h][l]  Gr = %f ", gr0);
    drawString(10, 16, 0.2, 1.0, 0.6, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu

    recalcLogistic(x0, gr0, yp);
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
    recalcLogistic(x0, gr0, yp);                // prepocet diagramu
    drawInfo(x0, gr0, yp);                      // vypis informaci o diagramu
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
        case 27:                                                              // pokud byla stlacena klavesa ESC, konec programu
        case 'q': exit(0);                                             break; // totez co klavesa ESC
        case 'l': gr0-=0.05;                      glutPostRedisplay(); break; // zmena parametru gr0
        case 'h': gr0+=0.05;                      glutPostRedisplay(); break;
        case 'j': yp-=5;                          glutPostRedisplay(); break; // zmena parametru x0
        case 'k': yp+=5;                          glutPostRedisplay(); break;
        case '1': if (x0>0.1) x0-=0.01;           glutPostRedisplay(); break; // zmena parametru x0
        case '2': if (x0<0.9) x0+=0.01;           glutPostRedisplay(); break;
        default:                                                       break;
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
    glutCreateWindow(WINDOW_TITLE);             // vytvoreni okna pro kresleni
    glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT);// zmena velikosti okna
    glutPositionWindow(100, 100);               // pozice leveho horniho rohu okna
    glutDisplayFunc(onDisplay);                 // registrace funkce volane pri prekreslovani okna
    glutReshapeFunc(onResize);                  // registrace funkce volane pri zmene velikosti okna
    glutKeyboardFunc(onKeyboard);               // registrace funkce volani pri stlaceni klavesy
    onInit();                                   // inicializace vykreslovani
    glutMainLoop();                             // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                   // navratova hodnota vracena operacnimu systemu
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

