//---------------------------------------------------------------------
// Ukazkovy priklad ke clanku fraktaly v pocitacove grafice.
// Autor: Pavel Tisnovsky
//
// Jednoduchy program, ktery slouzi pro zobrazeni souboru s ulozenymi
// trojuhelniky.
// Pro osvetleni telesa je pouzito dvou bodovych svetelnych zdroju.
// Jeden svetelny zdroj zustava umisteny pevne v prostoru, druhy se
// pohybuje soucasne s kamerou.
// Pomoci leveho tlacitka mysi lze telesem otacet, prave tlacitko slouzi
// k priblizeni nebo vzdaleni telesa.
//---------------------------------------------------------------------

#include <GL/glut.h>                            // hlavickovy soubor funkci GLUTu a OpenGL
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define SCALE 10.0                              // zmena meritka

enum {                                          // operace, ktere se mohou provadet s mysi:
    ROTATE,                                     // rotace objektu
    TRANSLATE,                                  // posun objektu
} operation=ROTATE;

int   gl_list;                                  // cislo display listu s nactenym objektem

int   xnew=0, ynew=0, znew=20;                  // soucasna pozice mysi, ze ktere se pocitaji rotace a posuvy
int   xold=0, yold=0, zold=20;                  // minula pozice mysi, ze ktere se pocitaji rotace a posuvy
int   xx, yy, zz;                               // bod, ve kterem se nachazi kurzor mysi

int   windowWidth;                              // sirka okna
int   windowHeight;                             // vyska okna

// parametry, ktere ovlivnuji osvetleni
GLfloat materialAmbient[]={0.4f, 0.4f, 0.4f, 1.0f};  // ambientni slozka barvy materialu
GLfloat materialDiffuse[]={0.8f, 0.4f, 0.4f, 1.0f};  // difuzni slozka barvy materialu
GLfloat materialSpecular[]={1.0f, 1.0f, 1.0f, 1.0f}; // barva odlesku
GLfloat materialShininess[]={50.0f};                 // faktor odlesku
GLfloat light_position1[]={1.0f, 0.0f,  1.0f, 1.0f}; // pozice prvniho svetla
GLfloat light_position2[]={0.0f, 1.0f,100.0f, 1.0f}; // pozice druheho svetla
GLfloat light_color1[]={1.0f, 1.0f, 1.0f};           // barva prvniho svetla
GLfloat light_color2[]={1.0f, 1.0f, 0.0f};           // barva druheho svetla



//---------------------------------------------------------------------
// Nacteni obsahu souboru do display listu
//---------------------------------------------------------------------
void loadObject(char *fileName) {
#define MIN 1e-10
#define MAX 1e+10
    // makra pro zjisteni maxima a minima
#define SET_MIN(a, min) if ((a)<(min)) (min)=(a)
#define SET_MAX(a, max) if ((a)>(max)) (max)=(a)

    float x1, y1, z1, x2, y2, z2, x3, y3, z3;
    float xmin=MAX, xmax=MIN, ymin=MAX, ymax=MIN, zmin=MAX, zmax=MIN;
    float x0, y0, z0;
    int   line=0;
    FILE *fin=fopen(fileName, "r");

    gl_list=glGenLists(1);                      // zjistime si pro jistotu cislo volneho listu
    glNewList(gl_list, GL_COMPILE);

    // nacist cely soubor a zjistit meze objektu
    while (fscanf(fin, "%f %f %f %f %f %f %f %f %f\n", &x1, &y1, &z1,
                &x2, &y2, &z2,
                &x3, &y3, &z3)==9) {
        SET_MIN(x1, xmin);    SET_MIN(x2, xmin);    SET_MIN(x3, xmin);
        SET_MAX(x1, xmax);    SET_MAX(x2, xmax);    SET_MAX(x3, xmax);
        SET_MIN(y1, ymin);    SET_MIN(y2, ymin);    SET_MIN(y3, ymin);
        SET_MAX(y1, ymax);    SET_MAX(y2, ymax);    SET_MAX(y3, ymax);
        SET_MIN(z1, zmin);    SET_MIN(z2, zmin);    SET_MIN(z3, zmin);
        SET_MAX(z1, zmax);    SET_MAX(z2, zmax);    SET_MAX(z3, zmax);
    }
    printf("Boundary:   [%f, %f, %f] - [%f, %f, %f]\n", xmin, ymin, zmin, xmax, ymax, zmax);

    // vypocet stredu objektu
    x0=(xmax+xmin)/2.0;
    y0=(ymax+ymin)/2.0;
    z0=(zmax+zmin)/2.0;
    printf("Center:     [%f, %f, %f]\n", x0, y0, z0);

    fseek(fin, 0L, SEEK_SET);
    // znovunacteni vsech radku ze souboru
    while (fscanf(fin, "%f %f %f %f %f %f %f %f %f\n", &x1, &y1, &z1,
                &x2, &y2, &z2,
                &x3, &y3, &z3)==9) {
        float nx, ny, nz;
        float vx1, vy1, vz1;
        float vx2, vy2, vz2;
        float d;

        // posun objektu do stredu [0,0,0]
        x1-=x0;    x2-=x0;    x3-=x0;
        y1-=y0;    y2-=y0;    y3-=y0;
        z1-=z0;    z2-=z0;    z3-=z0;

        // zmena meritka pro velke objekty
        x1/=SCALE;
        y1/=SCALE;
        z1/=SCALE;
        x2/=SCALE;
        y2/=SCALE;
        z2/=SCALE;
        x3/=SCALE;
        y3/=SCALE;
        z3/=SCALE;

        // vypocet dvou vektoru na plosce
        vx1=x2-x1;
        vy1=y2-y1;
        vz1=z2-z1;
        vx2=x3-x1;
        vy2=y3-y1;
        vz2=z3-z1;

        // vypocet normaloveho vektoru plosky
        nx=vy1*vz2-vy2*vz1;
        ny=vx2*vz1-vx1*vz2;
        nz=vx1*vy2-vx2*vy1;

        // normalizace normaloveho vektoru
        d=sqrt(nx*nx+ny*ny+nz*nz);
        if (d>1e-10) {
            nx/=d;
            ny/=d;
            nz/=d;
        }
        else {
            nx=1.0; ny=0.0; nz=0.0;
        }
        
        // zapis trojuhelniku do display listu
        glBegin(GL_TRIANGLE_STRIP);
            glNormal3f(nx, ny, nz);
            glVertex3f(x1, y1, z1);
            glVertex3f(x2, y2, z2);
            glVertex3f(x3, y3, z3);
        glEnd();
        line++;
    }
    fclose(fin);
    printf("Triangles:  %d\n", line);
    glEndList();                                // konec zadavani display listu

//    znew=zold=-zmax;
}



//---------------------------------------------------------------------
// Funkce pro inicializaci vykreslovani
//---------------------------------------------------------------------
void onInit(char *fileName)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi obrazku
    glClearDepth(1.0f);                         // implicitni hloubka ulozena v pameti hloubky
    glEnable(GL_DEPTH_TEST);                    // povoleni funkce pro testovani hodnot v pameti hloubky
    glDepthFunc(GL_LESS);                       // funkce pro testovani fragmentu
    glShadeModel(GL_SMOOTH);                    // nastaveni stinovaciho rezimu
    glPolygonMode(GL_FRONT, GL_FILL);           // nastaveni rezimu vykresleni modelu
    glPolygonMode(GL_BACK, GL_FILL);            // jak pro predni tak pro zadni steny
    glDisable(GL_CULL_FACE);                    // zadne hrany ani steny se nebudou odstranovat
    glMaterialfv(GL_FRONT, GL_AMBIENT, materialAmbient);    // nastaveni ambientni slozky barvy materialu
    glMaterialfv(GL_FRONT, GL_DIFFUSE, materialDiffuse);    // nastaveni difuzni slozky barvy materialu
    glMaterialfv(GL_FRONT, GL_SPECULAR, materialSpecular);  // nastaveni barvy odlesku
    glMaterialfv(GL_FRONT, GL_SHININESS, materialShininess);// nastaveni faktoru odlesku
    glLightfv(GL_LIGHT0, GL_POSITION, light_position1);     // nastaveni pozice prvniho svetla
    glLightfv(GL_LIGHT1, GL_POSITION, light_position2);     // nastaveni pozice druheho svetla
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color1);         // nastaveni barvy prvniho svetla
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_color2);         // nastaveni barvy druheho svetla
    glEnable(GL_LIGHTING);                      // globalni povoleni stinovani
    glEnable(GL_LIGHT0);                        // povoleni prvniho svetla
    glEnable(GL_LIGHT1);                        // povoleni prvniho svetla
    loadObject(fileName);
}



//---------------------------------------------------------------------
// Nastaveni souradneho systemu v zavislosti na velikosti okna
//---------------------------------------------------------------------
void onResize(int w, int h)                     // argumenty w a h reprezentuji novou velikost okna
{
    glViewport(0, 0, w, h);                     // viditelna oblast pres cele okno
    windowWidth=w;                              // zapamatovat si velikost okna
    windowHeight=h;
}



//---------------------------------------------------------------------
// Nastaveni perspektivni projekce
//---------------------------------------------------------------------
void setPerspectiveProjection(void)
{
    glMatrixMode(GL_PROJECTION);                // zacatek modifikace projekcni matice
    glLoadIdentity();                           // vymazani projekcni matice (=identita)
    gluPerspective(70.0, (double)windowWidth/(double)windowHeight, 0.1f, 10000.0f);// nastaveni perspektivni kamery
    glMatrixMode(GL_MODELVIEW);                 // bude se menit modelova matice
    glLoadIdentity();                           // nahrat jednotkovou matici
}



//--------------------------------------------------------------------
// Vykresleni objektu
//--------------------------------------------------------------------
void drawObjectNormal(void)
{
    glCallList(gl_list);                        // vykresleni naseho objektu
}



//--------------------------------------------------------------------
// Tato funkce je volana pri kazdem prekresleni okna
//--------------------------------------------------------------------
void onDisplay(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);// vymazani barvoveho bufferu i pameti hloubky
    setPerspectiveProjection();                 // nastaveni perspektivni kamery
    glTranslatef(0.0f, 0.0f, -50.0f);           // posun objektu dale od kamery
    glTranslatef(0.0f, 0.0f, znew);             // priblizeni ci vzdaleni objektu podle pohybu kurzoru mysi
    glRotatef(ynew, 1.0f, 0.0f, 0.0f);          // rotace objektu podle pohybu kurzoru mysi
    glRotatef(xnew, 0.0f, 1.0f, 0.0f);
    //glPushMatrix();                             // ulozeni matice na zasobnik a zmena pozice druheho svetla
    //glLightfv(GL_LIGHT1, GL_POSITION, light_position2);
    //glPopMatrix();
    drawObjectNormal();                         // vykresleni objektu
    glFlush();                                  // provedeni a vykresleni vsech zmen
    glutSwapBuffers();                          // a prohozeni predniho a zadniho bufferu
}



//---------------------------------------------------------------------
// Tato funkce je volana pri stlaceni ASCII klavesy
//---------------------------------------------------------------------
void onKeyboard(unsigned char key, int x, int y)
{
    if (key>='A' && key<='Z')                   // uprava velkych pismen na mala
        key+='a'-'A';                           // pro zjednoduseni prikazu switch

    switch (key) {
        case 27:    exit(0);            break;  // ukonceni aplikace
        case 'q':   exit(0);            break;  // ukonceni aplikace
                    // nastaveni rezimu vykreslovani plosek
        case '1':   glPolygonMode(GL_FRONT_AND_BACK, GL_POINT); glutPostRedisplay(); break;
        case '2':   glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);  glutPostRedisplay(); break;
        case '3':   glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);  glutPostRedisplay(); break;
        default:                        break;
    }
}



//---------------------------------------------------------------------
// Tato funkce je volana pri stisku ci pusteni tlacitka mysi
//---------------------------------------------------------------------
void onMouseButton(int button, int state, int x, int y)
{
    if (button==GLUT_LEFT_BUTTON) {             // pri zmene stavu leveho tlacitka
        operation=ROTATE;
        if (state==GLUT_DOWN) {                 // pri stlaceni tlacitka
            xx=x;                               // zapamatovat pozici kurzoru mysi
            yy=y;
        }
        else {                                  // pri pusteni tlacitka
            xold=xnew;                          // zapamatovat novy pocatek
            yold=ynew;
        }
        glutPostRedisplay();                    // prekresleni sceny
    }
    if (button==GLUT_RIGHT_BUTTON) {
        operation=TRANSLATE;
        if (state==GLUT_DOWN) zz=y;             // pri stlaceni tlacitka zapamatovat polohu kurzoru mysi
        else zold=znew;                         // pri pusteni tlacitka zapamatovat novy pocatek
        glutPostRedisplay();                    // prekresleni sceny
    }
}



//---------------------------------------------------------------------
// Tato funkce je volana pri pohybu mysi se stlacenym tlacitkem.
// To, ktere tlacitko je stlaceno si musime predem zaznamenat do
// globalni promenne stav ve funkci onMouseButton()
//---------------------------------------------------------------------
void onMouseMotion(int x, int y)
{
    switch (operation) {
        case ROTATE:                            // stav rotace objektu
            xnew=xold+x-xx;                     // vypocitat novou pozici
            ynew=yold+y-yy;
            glutPostRedisplay();                // a prekreslit scenu
            break;
        case TRANSLATE:                         // stav priblizeni/oddaleni objektu
            znew=zold+y-zz;                     // vypocitat novou pozici
            glutPostRedisplay();                // a prekreslit scenu
            break;
    }
}



//---------------------------------------------------------------------
// Hlavni funkce konzolove aplikace
//---------------------------------------------------------------------
int main(int argc, char **argv)
{
    glutInit(&argc, argv);                      // inicializace knihovny GLUT
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);// nastaveni dvou barvovych bufferu a pameti hloubky
    glutInitWindowPosition(30, 30);             // pocatecni pozice leveho horniho rohu okna
    glutInitWindowSize(450, 450);               // pocatecni velikost okna
    glutCreateWindow("RAW Viewer");             // vytvoreni okna pro kresleni
    glutDisplayFunc(onDisplay);                 // registrace funkce volane pri prekreslovani okna
    glutReshapeFunc(onResize);                  // registrace funkce volane pri zmene velikosti okna
    glutKeyboardFunc(onKeyboard);               // registrace funkce volane pri stlaceni klavesy
    glutMouseFunc(onMouseButton);               // registrace funkce volane pri stlaceni ci pusteni tlacitka
    glutMotionFunc(onMouseMotion);              // registrace funkce volane pri pohybu mysi se stlacenym tlacitkem
    if (argc<2) {                               // kontrola, zda je zadan vstupni soubor
        puts("Usage raw_view file.raw\n");
        return 1;
    }
    onInit(argv[1]);                            // inicializace vykreslovani
    glutMainLoop();                             // nekonecna smycka, kde se volaji zaregistrovane funkce
    return 0;                                   // navratova hodnota vracena operacnimu systemu
}



//---------------------------------------------------------------------
// Konec zdrojoveho souboru
//---------------------------------------------------------------------

