//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Demonstracni priklad 53.2
// Autor: Pavel Tisnovsky
//
// Vykresleni snehove vlocky Helge von Kocha (Koch Snowflake) pomoci L-systemu.
// Po prekladu a spusteni programu se nejprve provede nekolikere rozepsani
// gramatiky. Vysledny retezec je posleze pouzit pro vykresleni L-systemu
// za pomoci zelvi grafiky (turtle graphics).
// Zmena velikosti fraktalu se provadi stiskem klaves [PageUp] a [PageDown],
// posun fraktalu je mozne provest kurzorovymi klavesami (sipkami).
// Zmena poctu prepisu symbolu 'F' se provadi pomoci klaves [1]-[5].
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

#define WINDOW_TITLE    "Fraktaly 53.2"         // titulek okna
#define WINDOW_WIDTH    400                     // pocatecni velikost okna
#define WINDOW_HEIGHT   470

#define MAX_LENGTH      16384                   // maximalni delka retezce

#define START_SYMBOL    "F++F++F"               // startovaci symbol

double xpos=0.0;                                // pozice fraktalu v okne
double ypos=0.87*WINDOW_WIDTH/3;
char   ret[MAX_LENGTH]=START_SYMBOL;            // pocatecni symbol
const char prepstr[]="F-F++F-F";                // prepisovaci pravidlo
int    rulesCount=1;                            // pocet aplikaci prepisovaciho pravidla

double step=WINDOW_WIDTH/3;                     // krok zelvy
double x, y, alpha;                             // souradnice a natoceni zelvy
double delta=3.1415927/3.0;



//-----------------------------------------------------------------------------
// Aplikace prepisovaciho pravidla na retezec
//-----------------------------------------------------------------------------
void applyRule(void)
{
    int i, j, k;                                // pocitadla smycek a indexy znaku
    char src[MAX_LENGTH];                       // zdrojovy retezec
    char dest[MAX_LENGTH];                      // cilovy retezec
    int fcount=0;                               // pocet prepisu
    strcpy(src, ret);
    puts(src);                                  // kontrolni vypis pred prepisem
    for (i=0, j=0; src[i]; i++) {               // projit celym retezcem
        if (src[i]=='F') {                      // tento symbol se ma prepsat
            for (k=0; prepstr[k]; k++)          // provest prepis
                dest[j++]=prepstr[k];
        }
        else {                                  // ostatni symboly kopirovat
            dest[j]=src[i];
            j++;
        }
    }
    dest[j]=0;

    for (j=0; dest[j]; j++)
        if (dest[j]=='F') fcount++;
    puts(dest);                                 // kontrolni vypis po prepisu
    printf("fcount=%d\n", fcount);
    strcpy(ret, dest);
}



//-----------------------------------------------------------------------------
// Inicializace L-systemu
//-----------------------------------------------------------------------------
void initLSystem(void)
{
    int i;
    // pocatecni symbol
    strcpy(ret, START_SYMBOL);
    // aplikace prepisovaciho pravidla
    for (i=0; i<rulesCount; i++)
        applyRule();
}



//-----------------------------------------------------------------------------
// Nastaveni zelvy do pocatecni (domaci) pozice
//-----------------------------------------------------------------------------
void logo_home(double xpos, double ypos)
{
    x=xpos;
    y=ypos;
    alpha=0.0;
}



//-----------------------------------------------------------------------------
// Posun zelvy dopredu s kreslenim
//-----------------------------------------------------------------------------
void logo_forward(void)
{
    glBegin(GL_LINES);
    glVertex2d(x,y);
    x+=step*cos(alpha);                         // posun v zadanem smeru
    y+=step*sin(alpha);
    glVertex2d(x,y);
    glEnd();
}



//-----------------------------------------------------------------------------
// Posun zelvy dozadu s kreslenim
//-----------------------------------------------------------------------------
void logo_backward(void)
{
    glBegin(GL_LINES);
    glVertex2d(x,y);
    x+=step*cos(alpha);                         // posun v zadanem smeru
    y+=step*sin(alpha);
    glVertex2d(x,y);
    glEnd();
}



//-----------------------------------------------------------------------------
// Posun zelvy dopredu bez kresleni
//-----------------------------------------------------------------------------
void logo_move(void)
{
    x+=step*cos(alpha);                         // posun v zadanem smeru
    y+=step*sin(alpha);
}



//-----------------------------------------------------------------------------
// Otoceni zelvy doleva
//-----------------------------------------------------------------------------
void logo_left(void)
{
    alpha+=delta;                               // zmena uhlu
}



//-----------------------------------------------------------------------------
// Otoceni zelvy doprava
//-----------------------------------------------------------------------------
void logo_right(void)
{
    alpha-=delta;                               // zmena uhlu
}



//-----------------------------------------------------------------------------
// Prekresleni L-systemu
//-----------------------------------------------------------------------------
void recalcLsys(const char *ret,                // ridici retezec
                double xpos,                    // posun obrazce
                double ypos)
{   
    int i;
    logo_home(xpos, ypos);                      // inicializace zelvy
    for (i=0; ret[i]; i++) {                    // projit celym retezcem
        switch (ret[i]) {                       // a reagovat na prikazy
            case 'F':                           // posun v zadanem smeru
                logo_forward();
                break;
            case 'B':                           // zpetny posun v zadanem smeru
                logo_backward();
                break;
            case 'G':                           // posun v zadanem smeru bez kresleni
                logo_move();
                break;
            case '+':                           // zmena uhlu
                logo_left();
                break;
            case '-':                           // zmena uhlu
                logo_right();
                break;
            default:
                break;
        }
    }
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);      // mod ulozeni pixelu
    initLSystem();
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
    recalcLsys(ret, xpos, ypos);                // prekresleni L-systemu
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
    // zmena poctu prepsani retezce
    if (key>='1' && key<='5') {
        rulesCount=key-'1'+1;
        // zmena kroku v zavislosti na poctu prepisu
        step=WINDOW_WIDTH/(pow(3, rulesCount));
        initLSystem();
        glutPostRedisplay();
        return;
    }
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
// Tato callback funkce je zavolana pri stlaceni non-ASCII klavesy
//-----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void onSpecial(int key, int x, int y)
{
    // posun fraktalu a zmena meritka
    switch (key) {
        case GLUT_KEY_LEFT:      xpos-=5;   glutPostRedisplay(); break;
        case GLUT_KEY_RIGHT:     xpos+=5;   glutPostRedisplay(); break;
        case GLUT_KEY_UP:        ypos+=5;   glutPostRedisplay(); break;
        case GLUT_KEY_DOWN:      ypos-=5;   glutPostRedisplay(); break;
        case GLUT_KEY_PAGE_UP:   step+=0.1; glutPostRedisplay(); break;
        case GLUT_KEY_PAGE_DOWN: step-=0.1; glutPostRedisplay(); break;
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

