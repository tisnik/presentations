//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Demonstracni priklad 54.2
// Autor: Pavel Tisnovsky
//
// Vykresleni Hilbertovy krivky pomoci paralelniho prepisovani retezcu.
// Po prekladu a spusteni programu se nejprve provede nekolikere rozepsani
// gramatiky. Vysledny retezec je posleze pouzit pro vykresleni L-systemu
// za pomoci zelvi grafiky (turtle graphics).
// Zmena velikosti fraktalu se provadi stiskem klaves [PageUp] a [PageDown],
// posun fraktalu je mozne provest kurzorovymi klavesami (sipkami).
// Zmena poctu prepisu symbolu se provadi pomoci klaves [1]-[3], pricemz
// po stlaceni klavesy [1] je proveden pouze jeden prepis axiomu.
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

#define WINDOW_TITLE    "Fraktaly 54.2"         // titulek okna
#define WINDOW_WIDTH    400                     // pocatecni velikost okna
#define WINDOW_HEIGHT   470

#define MAX_LENGTH     500000                   // maximalni delka retezce

double xpos=0.0;                                // pozice fraktalu v okne
double ypos=0.87*WINDOW_WIDTH/3;
char   retx[MAX_LENGTH];                        // pocatecni symbol
int    itersCount=1;                            // pocet aplikaci prepisovaciho pravidla

char  *rules[]={                                // jednotliva prepisovaci pravidla
    "X=-YF+XFX+FY-",
    "Y=+XF-YFY-FX+",
    NULL
};

char   axiom[]="X";                            // axiom - prvotni naplneni vysledneho retezce

double step=10;;                                // krok zelvy
double x, y, alpha;                             // souradnice a natoceni zelvy
double delta=3.1415927/2.0;



//-----------------------------------------------------------------------------
// Aplikace prepisovacich pravidel na retezec
//-----------------------------------------------------------------------------
void applyRules(
        char *rules[],                          // pole prepisovacich pravidel
        char *axiom,                            // axiom - prvotni naplneni retezce
        char *ret,                              // retezec, do ktereho se ma ulozit vysledek
        int maxiters)                           // maximalni pocet iteraci (aplikaci pravidel)
{
    int rulesCount;                             // pocet pravidel
    int rule;                                   // prave aplikovane pravidlo
    char *leftSide;                             // pole levych casti prepisovacich pravidel
    char **rightSideSrc;                        // pole pravych casti prepisovacich pravidel
    char **rightSideDest;
    int i, j, k, iter;                          // pocitadla smycek a indexy znaku

    // zjistit celkovy pocet prepisovacich pravidel
    for (rulesCount=0; rules[rulesCount]; rulesCount++)
        ;
    // nyni mame v promenne rulesCount ulozen pocet prepisovacich pravidel
    printf("celkovy pocet pravidel=%d\n", rulesCount);

    // alokace pameti pro levou stranu prepisovacich pravidel
    // a inicializace pole znaku
    leftSide=(char *)malloc(rulesCount*sizeof(char));
    for (i=0; i<rulesCount; i++)
        leftSide[i]=rules[i][0];

    // alokace pameti pro pravou stranu prepisovacich pravidel
    // a inicializace pravych stran
    rightSideSrc=(char **)malloc(rulesCount*sizeof(char *));
    rightSideDest=(char **)malloc(rulesCount*sizeof(char *));
    for (i=0; i<rulesCount; i++) {
        rightSideSrc[i]=(char *)malloc(MAX_LENGTH);
        rightSideDest[i]=(char *)malloc(MAX_LENGTH);
        strcpy(rightSideSrc[i], rules[i]+2); // podretezec za znakem '='
    }

    // nastaveni axiomu
    strcpy(ret, axiom);

    // hlavni iteracni smycka
    for (iter=0; iter<=maxiters; iter++) {
        printf("iteration=%d\n", iter);
        // pro vsechna pravidla
        for (rule=0; rule<rulesCount; rule++) {
            // vypis pravidla pred prepisem
            //printf("%c\t%s\t", leftSide[rule], rightSideSrc[rule]);
            // projit celym retezcem a zpracovat jednotlive znaky
            for (i=0, j=0; rightSideSrc[rule][i]; i++) {
                int left;
                int found=0;
                // pro kazdy znak zjistit, zda pro nej neexistuje prepisovaci pravidlo
                // a pokud ano, provest prepis
                for (left=0; left<rulesCount; left++) {
                    if (leftSide[left]==rightSideSrc[rule][i]) {
                        for (k=0; rightSideSrc[left][k]; k++)          // provest prepis
                            rightSideDest[rule][j++]=rightSideSrc[left][k];
                        found=1;
                    }
                }
                // zadne pravidlo pro dany znak jsme nenasli, proto se znak
                // pouze zkopiruje
                if (!found) {
                    rightSideDest[rule][j]=rightSideSrc[rule][i];
                    j++;
                }
            }
            // ukonceni retezce
            rightSideDest[rule][j]=0;
            // vypis pravidla po prepisu
            //printf("%s\n", rightSideDest[rule]);
        }
        // "paralelni" prepis novych retezcu na misto stavajicich
        // (lezi mimo predchozi smycku!)
        for (rule=0; rule<rulesCount; rule++)
            strcpy(rightSideSrc[rule], rightSideDest[rule]);
    }

    // prepis vysledku
    strcpy(ret, rightSideSrc[1]);
    printf("Celkova delka retezce: %d\n", strlen(ret));
    // a doplneni posledniho posunu zelvy
    //strcat(ret, "F");
    //puts("");
    // vypis retezce v podobe, kdy jsou vypsany pouze znaky ovladajici zelvu
    //for (i=0; i<strlen(ret); i++)
    //    if (ret[i]=='F' || ret[i]=='+' || ret[i]=='-') putchar(ret[i]);
}



//-----------------------------------------------------------------------------
// Inicializace L-systemu
//-----------------------------------------------------------------------------
void initLSystem(int maxiters)
{
    // aplikace prepisovacich pravidel
    applyRules(rules, axiom, retx, maxiters);
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
    x-=step*cos(alpha);                         // posun v zadanem smeru
    y-=step*sin(alpha);
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
    initLSystem(itersCount);
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
    recalcLsys(retx, xpos, ypos);               // prekresleni L-systemu
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
    if (key>='1' && key<='3') {
        itersCount=key-'1';
        // zmena kroku v zavislosti na poctu prepisu
        //step=WINDOW_WIDTH/(pow(5, itersCount));
        initLSystem(itersCount);
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
        case GLUT_KEY_PAGE_UP:   step+=0.5; glutPostRedisplay(); break;
        case GLUT_KEY_PAGE_DOWN: step-=0.5; glutPostRedisplay(); break;
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

