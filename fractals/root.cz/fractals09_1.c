//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 9.1
// Autor: Pavel Tisnovsky
//
// Vykresleni Lorenzova atraktoru v prostoru
// Otoceni a posun objektu se provadi pomoci mysi:
// leve tlacitko  - otaceni
// prave tlacitko - posun
//
// Ukonceni aplikace se provede klavesou [Esc].
//-----------------------------------------------------------------------------

#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <GL/glut.h>                            // hlavickovy soubor funkci GLUTu a OpenGL
#include <GL/glu.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define WINDOW_TITLE    "Fraktaly 9.1"          // titulek okna
#define WINDOW_WIDTH    512                     // pocatecni velikost okna
#define WINDOW_HEIGHT   384

double a=5.0;                                   // parametry fraktalu
double b=15.0;
double c=1.0;
double dt=0.02;
int    maxiter=6000;                            // maximalni pocet iteraci
double scale=0.1;                               // meritko fraktalu
int    xnew=0, xold=0, ynew=0, yold=0, stav=0;  // stav mysi
int    znew=0, zold=0;
int    x2=0, y2=0, z2=0;



//-----------------------------------------------------------------------------
// Prekresleni dynamickeho systemu
//-----------------------------------------------------------------------------
void recalcLorenz(    double a,                 // parametry fraktalu
                      double b,
                      double c,
                      double dt,                // pouzito pri numericke integraci
                      int    maxiter,           // maximalni pocet iteraci
                      double scale)             // meritko obrazce
{
    double x=0.1, y=0, z=0;                     // pozice bodu
    double x2, y2, z2;
    int iter=maxiter;

    glColor3f(1.0f, 1.0f, 1.0f);
    glBegin(GL_LINE_STRIP);
    while (iter--) {                            // iteracni smycka
        glColor3f(x/10.0,y/10.0,z/10.0);
        x2 = x+(-a*x*dt)+(a*y*dt);
        y2 = y+(b*x*dt)-(y*dt)-(z*x*dt);
        z2 = z+(-c*z*dt)+(x*y*dt);
        x=x2;
        y=y2;
        z=z2;
        glVertex3d(x*scale, y*scale, z*scale);
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
// Vypis informaci o vykreslovanem fraktalu
//-----------------------------------------------------------------------------
void drawInfo(double a, double b, double c, double dt, int maxiter, double scale, double panx, double pany)
{
    char str[100];
    sprintf(str, "[1][2]  a = %5.3f", a);
    drawString(10,112, 1.0, 1.0, 0.0, str);
    sprintf(str, "[3][4]  b = %5.3f", b);
    drawString(10, 96, 1.0, 1.0, 0.2, str);
    sprintf(str, "[5][6]  c = %5.3f", c);
    drawString(10, 80, 1.0, 1.0, 0.4, str);
    sprintf(str, "[7][8]  dt = %5.3f", dt);
    drawString(10, 64, 0.8, 1.0, 0.6, str);
    sprintf(str, "[<][>]  maxiter = %d", maxiter);
    drawString(10, 48, 0.6, 1.0, 0.8, str);
    sprintf(str, "[PgUp][PgDn]  scale = %3.0f ", scale);
    drawString(10, 32, 0.4, 1.0, 1.0, str);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
}



//-----------------------------------------------------------------------------
// Nastaveni souradneho systemu v zavislosti na velikosti okna
//-----------------------------------------------------------------------------
void onResize(int w, int h)                     // argumenty w a h reprezentuji novou velikost okna
{
    glViewport(0, 0, w, h);                     // viditelna oblast pres cele okno
    glMatrixMode(GL_PROJECTION);                // zacatek modifikace projekcni matice
    glLoadIdentity();                           // vymazani projekcni matice (=identita)
    if (h==0)                                   // nastaveni perspektivni projekce
        gluPerspective ( 80, (float)w, 1.0, 5000.0 );
    else
        gluPerspective ( 80, (float)w /(float) h, 1.0, 5000.0 );
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
}



//-----------------------------------------------------------------------------
// Tato callback funkce je zavolana pri kazdem prekresleni okna
//-----------------------------------------------------------------------------
void onDisplay(void)
{
    glClear(GL_COLOR_BUFFER_BIT);               // vymazani vsech bitovych rovin barvoveho bufferu
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
        glLoadIdentity();
        glTranslatef(0.0f, 0.0f, -4.0);         // rotace o posun objektu
        glTranslatef(0.0f, 0.0f, znew);
        glRotatef(ynew, 1.0f, 0.0f, 0.0f);
        glRotatef(xnew, 0.0f, 1.0f, 0.0f);
        recalcLorenz(a, b, c, dt, maxiter, scale); // prepocet fraktalu
    glPopMatrix();
    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
        glLoadIdentity();
        glOrtho(0, 512, 0, 384, -1, 1);
        glRasterPos2i(0, 0);                    // nastaveni souradnic leveho spodniho rohu pixmapy
        drawInfo(a, b, c, dt, maxiter, scale, xnew, ynew);
    glPopMatrix();
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
        case 'q': exit(0);                                              break;// totez co klavesa ESC
        case '1': a-=0.1;                          glutPostRedisplay(); break;
        case '2': a+=0.1;                          glutPostRedisplay(); break;
        case '3': b-=0.1;                          glutPostRedisplay(); break;
        case '4': b+=0.1;                          glutPostRedisplay(); break;
        case '5': c-=0.01;                         glutPostRedisplay(); break;
        case '6': c+=0.01;                         glutPostRedisplay(); break;
        case '7': dt-=0.001;                       glutPostRedisplay(); break;
        case '8': dt+=0.001;                       glutPostRedisplay(); break;
        case '<':
        case ',': if (maxiter>100) maxiter-=100;   glutPostRedisplay(); break; // zmena poctu iteraci
        case '>':
        case '.': if (maxiter<100000) maxiter+=100;glutPostRedisplay(); break;
        default:                                                        break;
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
        case GLUT_KEY_PAGE_UP:   scale++; glutPostRedisplay();  break;
        case GLUT_KEY_PAGE_DOWN: if (scale>1) scale--; glutPostRedisplay(); break;
        default:                                                break;
    }
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



//-----------------------------------------------------------------------------
// Funkce volana pri stisku tlacitek mysi
//-----------------------------------------------------------------------------
void onMouse(int button, int state, int x, int y)
{
    if (button==GLUT_LEFT_BUTTON) {
        if (state==GLUT_DOWN) {                 // pri stlaceni
            stav=1;                             // nastaveni pro funkci motion
            x2=x;                               // zapamatovat pozici kurzoru mysi
            y2=y;
        }
        else {                                  // GLUT_UP
            stav=0;                             // normalni stav
            xold=xnew;                          // zapamatovat novy pocatek
            yold=ynew;
        }
    }
    if (button==GLUT_RIGHT_BUTTON) {
        if (state==GLUT_DOWN) {                 // pri stlaceni
            stav=2;                             // nastaveni pro funkci motion
            z2=y;                               // zapamatovat pozici kurzoru mysi
        }
        else {
            stav=0;
            zold=znew;                          // zapamatovat novy pocatek
        }
    }
    glutPostRedisplay();                        // prekresleni sceny
}



//-----------------------------------------------------------------------------
// funkce volana jestlize se mys pohybuje a je stlaceno nektere tlacitko
//-----------------------------------------------------------------------------
void onMotion(int x, int y)
{
    if (stav==1) {                              // stav presunu
        xnew=xold+x-x2;                         // vypocitat novou pozici
        ynew=yold+y-y2;
        glutPostRedisplay();                    // a prekreslit scenu
    }
    if (stav==2) {                              // stav presunu
        znew=zold+y-z2;                         // vypocitat novou pozici
        glutPostRedisplay();                    // a prekreslit scenu
    }
}



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
    glutMouseFunc(onMouse);
    glutMotionFunc(onMotion);                   // funkce volane pro udalosti mysi
    onInit();                                   // inicializace vykreslovani
    glutMainLoop();                             // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                   // navratova hodnota vracena operacnimu systemu
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

