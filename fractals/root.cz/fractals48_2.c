//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 48.2
// Autor: Pavel Tisnovsky
//
// Pouziti spektralni syntezy pro vytvoreni jednorozmerne stochasticke krivky
// s fraktalni charakteristikou. Pomoci klaves [A] a [S] je mozne menit pocet
// koeficientu Fourierovy transformace, klavesy [Z] a [X] slouzi k urceni
// Hurstova koeficientu a tim i fraktalni dimenze vytvorene krivky.
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

#define WINDOW_TITLE    "Fraktaly 48.2"         // titulek okna
#define WINDOW_WIDTH    640                     // pocatecni velikost okna
#define WINDOW_HEIGHT   480

int width, height;                              // velikost okna
float h=0.5;                                    // Hurstuv exponent
int   n=10;                                     // pocet koeficientu spektralni syntezy



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
// Spektralni synteza v 1D
//-----------------------------------------------------------------------------
void spectralSynthesis1D(void)
{
#define PI 3.1415927
    
    float A[n/2];                           // koeficienty Ak
    float B[n/2];                           // koeficienty Bk
    float beta=2.0*h+1;                     // promenna svazana s Hurstovym koeficientem
    int   i, j, k;                          // pocitadla smycek

    srand(123456);
    glBegin(GL_LINE_STRIP);
    for (i=0; i<n/2; i++) {                 // vypocet koeficientu Ak a Bk
        float rad=pow((i+1), -beta/2.0)*randomGauss();
        float phase=2.0*PI*randomN();
        A[i]=rad*cos(phase);
        B[i]=rad*sin(phase);
        //printf("%d\t%f\t%f\n", i, A[i], B[i]); // kontrolni vypis
    }
    for (j=0; j<width; j++) {               // vykresleni funkce pres cele okno
        float x=j;
        float y=0;
        for (k=0; k<n/2; k++) {
            float t=(j-n/2)*2.0*PI/width;   // horizontalni vyrovnani na stred okna
            y+=A[k]*cos(k*t)+B[k]*sin(k*t); // koeficient pro k-tou harmonickou
        }
        glVertex2f(x, height/2.0+(height/4.0)*y); // vertikalni vyrovnani na stred zmena amplitudy
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
// Vypsani informaci o zadanych parametrech
//-----------------------------------------------------------------------------
void drawInfo(int n, float Hexp)
{
    char str[100];
    sprintf(str, "[a][s]  N: %d", n);
    drawString(10, 42, 1.0, 1.0, 0.0, str);
    sprintf(str, "[z][x]  Hurst exponent: %5.2f", Hexp);
    drawString(10, 26, 1.0, 0.8, 0.2, str);
    sprintf(str, "Fractal dimension: %5.2f", 2.0-Hexp);
    drawString(10, 10, 1.0, 0.6, 0.4, str);
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
    width=w;
    height=h;
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
    drawInfo(n, h);
    spectralSynthesis1D();                      // vytvoreni obrazce spektralni syntezou
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

