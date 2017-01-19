//---------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 2
// Autor: Pavel Tisnovsky
//
// Program otevre jedno hlavni okno a vykresli do nej klasicky RGB
// trojuhelnik a dalsi tvary. Potom se provede precteni barev fragmentu
// z framebufferu a jejich ulozeni do externiho souboru, ktery je typu TGA.
// Ulozeni souboru probehne pri stlaceni klavesy 'S' (Save)
//---------------------------------------------------------------------

#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <GL/glut.h>                            // hlavickovy soubor funkci GLUTu a OpenGL
#include <stdio.h>
#include <stdlib.h>

#define WINDOW_TITLE    "Fraktaly 2"            // titulek okna
#define WINDOW_WIDTH    256                     // pocatecni velikost okna
#define WINDOW_HEIGHT   256
#define FILE_NAME       "fraktaly2.tga"         // jmeno souboru pro ulozeni pixmapy



//---------------------------------------------------------------------
// Funkce pro ulozeni pixmapy z framebufferu do souboru typu TGA (Targa)
//---------------------------------------------------------------------
void saveFramebuffer(const char *fileName)
{
    FILE *fout;
    unsigned int i, j, k;
    int width=glutGet(GLUT_WINDOW_WIDTH);       // sirka pixmapy (pro zmenu hlavicky)
    int height=glutGet(GLUT_WINDOW_HEIGHT);     // vyska pixmapy
    unsigned char tgaHeader[18]={
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
    unsigned char *parray=(unsigned char *)malloc(height*width*3);
    printf("w: %d h: %d\n", width, height);
    if (!parray) return;
    glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE, parray);
    memcpy(tgaHeader+12, &width, 2);            // do hlavicky TGA zapsat velikost obrazku
    memcpy(tgaHeader+14, &height, 2);
    fout=fopen(fileName, "wb");
    if (fout) {
        fwrite(tgaHeader, 18, 1, fout);         // zapsat hlavicku TGA do souboru
        for (j=height; j; j--) {                // radky zapisovat v opacnem poradi
            unsigned int yoff=(j-1)*3*width;    // y-ovy offset v poli
            unsigned int xoff=0;                // x-ovy offset v poli
            for (i=0; i<width; i++) {           // pro kazdy pixel na radku
                for (k=0; k<3; k++) {           // prohodit barvy RGB na BGR
                    fputc(parray[xoff+yoff+2-k], fout); // a zapsat do souboru
                }
                xoff+=3;
            }
        }
        fclose(fout);
    }
    free(parray);
}



//-----------------------------------------------------------------------------
// Funkce volana pro inicializaci vykreslovani
//-----------------------------------------------------------------------------
void onInit(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);       // barva pozadi
    glPixelStorei(GL_PACK_ALIGNMENT, 1);
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
    int i;
    glClear(GL_COLOR_BUFFER_BIT);               // vymazani vsech bitovych rovin barvoveho bufferu

    glBegin(GL_TRIANGLES);                      // vykresleni klasickeho RGB trojuhelniku
        glColor3f(1.0f, 0.0f, 0.0f);
        glVertex2i(0, 0);
        glColor3f(0.0f, 1.0f, 0.0f);
        glVertex2i(255, 0);
        glColor3f(0.0f, 0.0f, 1.0f);
        glVertex2i(127, 222);
    glEnd();

    glColor3f(1.0f, 0.0f, 0.0f);                // aby bylo otestovano korektni ulozeni rastrovych
    glPointSize(10.0f);                         // dat do souboru (orientace pixmapy a poradi barevnych slozek),
    glEnable(GL_POINT_SMOOTH);                  // vykreslime jeste cerveny bod o velikosti 10 pixelu
    glBegin(GL_POINTS);                         // do leveho horniho rohu.
        glVertex2i(7, 248);
    glEnd();

    glColor3f(1.0,1.0,1.0);                     // bila barva
    glBegin(GL_LINES);                          // vykresleni linkoveho vzorku
        for (i=0; i<256; i+=15) {
            glVertex2i(i, 255);
            glVertex2i(0, i);
        }
    glEnd();

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
    switch (key) {
        case 27: exit(0);
            break;                              // pokud byla stlacena klavesa ESC, konec programu
        case 's':
        case 'S':
            saveFramebuffer(FILE_NAME);         // ulozeni pixmapy
            break;
        default:
            break;
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
    glutInitDisplayMode(GLUT_RGB || GLUT_SINGLE);
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

