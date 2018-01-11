//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Demonstracni priklad 55.2
// Autor: Pavel Tisnovsky
//
// Vykresleni fraktalnich stromu a keru pomoci stochastickych L-systemu.
// Po prekladu a spusteni programu se nejprve provede nekolikere rozepsani
// gramatiky. Vysledny retezec je posleze pouzit pro vykresleni L-systemu
// za pomoci zelvi grafiky (turtle graphics).
// Zmena velikosti fraktalu se provadi stiskem klaves [PageUp] a [PageDown],
// posun fraktalu je mozne provest kurzorovymi klavesami (sipkami).
// Zmena poctu prepisu symbolu se provadi pomoci klaves [1]-[9], pricemz
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

#define WINDOW_TITLE    "Fraktaly 55.2"         // titulek okna
#define WINDOW_WIDTH    400                     // pocatecni velikost okna
#define WINDOW_HEIGHT   470

#define MAX_LENGTH     900000                   // maximalni delka retezce
#define PI             3.1415927

double xpos=WINDOW_WIDTH/2;                     // pozice fraktalu v okne
double ypos=10;
char   retx[MAX_LENGTH];                        // pocatecni symbol
int    itersCount=1;                            // pocet aplikaci prepisovaciho pravidla

// axiomy pro sedm vybranych L-systemu
char *axioms[]={
    "+++FX",
    "++++Z",
    "F",
    "F",
    "++++F",
    "++++F",
    "++++FX",
};

// zmeny natoceni zelvy pro vybrane L-systemy
double deltas[]={
    PI/6.0,
    PI/8.0,
    PI/7.0,
    PI/9.0,
    PI/8.0,
    PI/8.0,
    PI/8.0,
};

// prepisovaci pravidla pro vybrane L-systemy
char *rules[][4]={
    {
        "X=[-FX]+FX",
        NULL,
    },
    {
        "Z=ZFX[+Z][-Z]",
        "X=X[-FFF][+FFF]FX",
        NULL,
    },
    {
        "F=F[+F]F[-F]F",
        NULL,
    },
    {
        "F=F[+F]F[-F][F]",
        NULL,
    },
    {
        "F=FF-[-F+F+F]+[+F-F-F]",
        NULL,
    },
    {
        "F=FF-[F+F+F]+[+F-F-F]",
        NULL,
    },
    {
        "F=FF-[XY]+[XY]",
        "X=+FY",
        "Y=-FX",
        NULL
    },
};

double step=10;                                 // krok zelvy
double x, y, alpha;                             // souradnice a natoceni zelvy
int currentSystem=0;

double stepDelta=0.0;
double angleDelta=0.0;

typedef struct t_state {                        // datova struktura popisujici stav zelvy
    double x;
    double y;
    double alpha;
    struct t_state *next;
} t_state;

t_state *sp;                                    // ukazatel na vrchol zasobniku



//-----------------------------------------------------------------------------
// Inicializace zasobniku
//-----------------------------------------------------------------------------
void stack_init(void)
{
    sp=NULL;
}



//-----------------------------------------------------------------------------
// Vlozeni stavu zelvy na zasobnik
//-----------------------------------------------------------------------------
void stack_push(double x, double y, double alpha)
{
    t_state *st=(t_state *)malloc(sizeof(t_state));
    st->x=x;
    st->y=y;
    st->alpha=alpha;
    st->next=sp;
    sp=st;
}



//-----------------------------------------------------------------------------
// Vyjmuti stavu zelvy z vrcholu zasobniku
//-----------------------------------------------------------------------------
void stack_pop(double *x, double *y, double *alpha)
{
    if (sp!=NULL) {
        t_state *next=sp->next;
        *x=sp->x;
        *y=sp->y;
        *alpha=sp->alpha;
        free(sp);
        sp=next;
    }
    else {
        *x=0;
        *y=0;
        *alpha=0;
    }
}



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
    char *leftSide;                             // pole levych casti prepisovacich pravidel
    char **rightSideSrc;                        // pole pravych casti prepisovacich pravidel
    int i, j, k, iter;                          // pocitadla smycek a indexy znaku
    char src[MAX_LENGTH];

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
    for (i=0; i<rulesCount; i++) {
        rightSideSrc[i]=(char *)malloc(MAX_LENGTH);
        strcpy(rightSideSrc[i], rules[i]+2); // podretezec za znakem '='
    }

    // nastaveni axiomu
    strcpy(ret, axiom);

    // hlavni iteracni smycka
    for (iter=0; iter<=maxiters; iter++) {
        j=0;
        printf("iteration=%d\n", iter);
        strcpy(src, ret);
        char *ch;
        // projit celym retezcem
        for (ch=src; *ch; ch++) {
            int left;
            int found=0;
            // pro kazdy znak zjistit, zda pro nej neexistuje prepisovaci pravidlo
            // a pokud ano, provest prepis
            for (left=0; left<rulesCount; left++) {
                if (leftSide[left]==*ch) {
                    //printf("%c -> %s\n", *ch, rightSideSrc[left]);
                    for (k=0; rightSideSrc[left][k]; k++, j++)          // provest prepis
                        ret[j]=rightSideSrc[left][k];
                    found=1;
                }
            }
            // zadne pravidlo pro dany znak jsme nenasli, proto se znak
            // pouze zkopiruje
            if (!found) {
                //printf("%c -> %c\n", *ch, *ch);
                ret[j]=*ch;
                j++;
            }
        }
        ret[j]=0;
    }
}



//-----------------------------------------------------------------------------
// Inicializace L-systemu
//-----------------------------------------------------------------------------
void initLSystem(int maxiters)
{
    // aplikace prepisovacich pravidel
    applyRules(rules[currentSystem], axioms[currentSystem], retx, maxiters);
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
// Vypocet kroku zelvy s vyuzitim RNG
//-----------------------------------------------------------------------------
double randomStep(double step, double stepDelta)
{
    return step*(1.0+stepDelta*((double)rand()/RAND_MAX-1/2.0));
}



//-----------------------------------------------------------------------------
// Vypocet zmeny uhlu zelvy s vyuzitim RNG
//-----------------------------------------------------------------------------
double randomAngle(double angle, double angleDelta)
{
    return angle*(1.0+angleDelta*((double)rand()/RAND_MAX-1/2.0));
}



//-----------------------------------------------------------------------------
// Posun zelvy dopredu s kreslenim
//-----------------------------------------------------------------------------
void logo_forward(void)
{
    double rndStep=randomStep(step, stepDelta);
    glBegin(GL_LINES);
    glVertex2d(x,y);
    x+=rndStep*cos(alpha);                         // posun v zadanem smeru
    y+=rndStep*sin(alpha);
    glVertex2d(x,y);
    glEnd();
}



//-----------------------------------------------------------------------------
// Posun zelvy dozadu s kreslenim
//-----------------------------------------------------------------------------
void logo_backward(void)
{
    double rndStep=randomStep(step, stepDelta);
    glBegin(GL_LINES);
    glVertex2d(x,y);
    x-=rndStep*cos(alpha);                         // posun v zadanem smeru
    y-=rndStep*sin(alpha);
    glVertex2d(x,y);
    glEnd();
}



//-----------------------------------------------------------------------------
// Posun zelvy dopredu bez kresleni
//-----------------------------------------------------------------------------
void logo_move(void)
{
    double rndStep=randomStep(step, stepDelta);
    x+=rndStep*cos(alpha);                         // posun v zadanem smeru
    y+=rndStep*sin(alpha);
}



//-----------------------------------------------------------------------------
// Otoceni zelvy doleva
//-----------------------------------------------------------------------------
void logo_left(void)
{
    alpha+=randomAngle(deltas[currentSystem], angleDelta);  // zmena uhlu
}



//-----------------------------------------------------------------------------
// Otoceni zelvy doprava
//-----------------------------------------------------------------------------
void logo_right(void)
{
    alpha-=randomAngle(deltas[currentSystem], angleDelta);  // zmena uhlu
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
            case '[':                           // ulozeni stavu zelvy na zasobnik
                stack_push(x, y, alpha);
                break;
            case ']':                           // vyjmuti stavu zelvy ze zasobniku
                stack_pop(&x, &y, &alpha);
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
    stack_init();
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
    if (key>='1' && key<='9') {
        itersCount=key-'1';
        initLSystem(itersCount);
        glutPostRedisplay();
        return;
    }
    switch (key) {
        case 27:                                // pokud byla stlacena klavesa ESC, konec programu
        case 'q': exit(0);               break; // totez co klavesa ESC
        case 'a': if (angleDelta>0.1) angleDelta-=0.1; initLSystem(itersCount); glutPostRedisplay(); break;
        case 's': if (angleDelta<1.0) angleDelta+=0.1; initLSystem(itersCount); glutPostRedisplay(); break;
        case 'z': if (stepDelta>0.1)  stepDelta-=0.1;  initLSystem(itersCount); glutPostRedisplay(); break;
        case 'x': if (stepDelta<1.0)  stepDelta+=0.1;  initLSystem(itersCount); glutPostRedisplay(); break;
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
    // vyber L-systemu
    if (key>=GLUT_KEY_F1 && key<=GLUT_KEY_F7) {
        currentSystem=key-GLUT_KEY_F1;
        initLSystem(itersCount);
        glutPostRedisplay();
        return;
    }
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

