//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
//
// Autor: Pavel Tisnovsky
//
// Prvni demonstracni priklad na vypocet Markus-Lyapunovych fraktalu
//-----------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define PIXMAP_WIDTH    800                     // sirka pixmapy
#define PIXMAP_HEIGHT   600                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

pixmap *pix;



//-----------------------------------------------------------------------------
// Funkce pro vytvoreni pixmapy o zadane velikosti
//-----------------------------------------------------------------------------
pixmap * createPixmap(const unsigned int width, const unsigned int height)
{
    pixmap *p=(pixmap *)malloc(sizeof(pixmap)); // alokace struktury pixmapy
    if (!p) return NULL;
    p->width=width;                             // naplneni struktury
    p->height=height;
    p->pixels=(unsigned char *)malloc(3*width*height);
    if (!p->pixels) {                           // alokace pole pro pixely
        free(p);                                // alokace se nepovedla
        return NULL;
    }
    else {
        memset(p->pixels, 0, 3*width*height);   // smazani pixmapy
    }
    return p;
}



//-----------------------------------------------------------------------------
// Funkce pro zruseni pixmapy
//-----------------------------------------------------------------------------
void destroyPixmap(pixmap *p)
{
    if (p->pixels) free(p->pixels);             // uvolnit vlastni pixmapu
    if (p) free(p);                             // i okolni strukturu
}



//-----------------------------------------------------------------------------
// Vymazani pixmapy
//-----------------------------------------------------------------------------
void clearPixmap(const pixmap *p)
{
    if (!p) return;
    if (!p->pixels) return;
    memset(p->pixels, 0, 3*p->width*p->height);
}



//-----------------------------------------------------------------------------
// Ulozeni pixmapy do externiho souboru typu TGA (Targa)
//-----------------------------------------------------------------------------
void savePixmap(const pixmap *p, const char *fileName)
{
    FILE *fout;
    unsigned int i, j, k;
    unsigned char tgaHeader[18]={               // hlavicka formatu typu TGA
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
    if (!p || !p->pixels) return;
    memcpy(tgaHeader+12, &(p->width), 2);       // do hlavicky TGA zapsat velikost obrazku
    memcpy(tgaHeader+14, &(p->height), 2);
    fout=fopen(fileName, "wb");
    if (fout) {
        fwrite(tgaHeader, 18, 1, fout);         // zapsat hlavicku TGA do souboru
        for (j=p->height; j; j--) {             // radky zapisovat v opacnem poradi
            unsigned int yoff=(j-1)*3*p->width; // y-ovy offset v poli
            unsigned int xoff=0;                // x-ovy offset v poli
            for (i=0; i<p->width; i++) {        // pro kazdy pixel na radku
                for (k=0; k<3; k++) {           // prohodit barvy RGB na BGR
                    fputc(p->pixels[xoff+yoff+2-k], fout); // a zapsat do souboru
                }
                xoff+=3;                        // posun na dalsi pixel
            }
        }
        fclose(fout);
    }
}



//-----------------------------------------------------------------------------
// Zmena barvy pixelu na zadanych souradnicich
//-----------------------------------------------------------------------------
void putpixel(pixmap *p,
              const unsigned int x,             // pozice pixelu v pixmape
              const unsigned int y,
              const unsigned char r,            // barva pixelu
              const unsigned char g,
              const unsigned char b)
{
    int pos;
    // zde se vyuziva zkraceneho vyhodnoceni vyrazu - pokud plati !p, nic se dale netestuje
    if (!p || !p->pixels || x>=p->width || y>=p->height) return;
    pos=3*(x+y*p->width);
    p->pixels[pos++]=r;                         // nastaveni barvy pixelu
    p->pixels[pos++]=g;
    p->pixels[pos]=b;
}



//-----------------------------------------------------------------------------
// Vypocet Markus-Lyapunovych fraktalu
//-----------------------------------------------------------------------------
void recalcLyapunov(pixmap *pix,                // pracovni pixmapa
                    int    maxiter,             // maximalni pocet iteraci
                    double xmin,                // meze fraktalu v rovine
                    double ymin,
                    double xmax,
                    double ymax)
{
    int x, y, i, j;                             // pocitadla smycek
    double startx, starty;
    double z, r=0.0;
    double total;

    starty=ymin;
    // pro vsechny radky pixmapy
    for (y=0; y<pix->height; y++) {
        startx=xmin;
        printf("%d\t", y);
        // pro vsechny pixely na radku
        for (x=0; x<pix->width; x++) {
            startx+=(xmax-xmin)/pix->width;     // pocatecni hodnota prvni funkce
            z=0.5;
            total=0.0;
            j=0;                                // pocitadlo pro pristup k retezci
            // iteracni smycka
            for (i=0; i<maxiter; i++) {
                switch (i%2) {                  // vyber iteracni funkce
                    case 0:
                        z=(starty*z)*(1.0-z);
                        r=starty;
                        break;
                    case 1:
                        z=(startx*z)*(1.0-z);
                        r=startx;
                        break;
                }
                j++;
                if (i>maxiter/2) {              // ve druhe polovine cyklu se pocita Lyapunuv exponent
                    if (fabs(r-2.0*r*z)>0.0)
                        total+=log(fabs(r-2.0*r*z))/log(2.0);
                }
                if (z>500.0) break;
            }
            total=150.0*total/maxiter;          // vypocet exponentu s vynasobenim konstantou 150
            if (total<0) {                      // obarvit pouze pixely se zapornym exponentem
                if (total<-255) total=-255;
                total=-total/255;               // dalsi tri radky - gamma korekce
                total=pow(total, 0.5);
                total*=255.0;
                putpixel(pix, x, y, total, total, total);
            }
            else                                // "chaoticke" pixely jsou cerne
                putpixel(pix, x, y, 0, 0, 0);
        }
        // prechod na dalsi radek
        starty+=(ymax-ymin)/pix->height;
    }

}



//-----------------------------------------------------------------------------
// Hlavni funkce konzolove aplikace
//-----------------------------------------------------------------------------
int main(int argc, char **argv)
{
    puts("\n*** lyapunov ***\n");
    puts("processing:\n");

    // vytvoreni a prvotni smazani pixmapy
    pix=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
    clearPixmap(pix);

    recalcLyapunov(pix, 500, -8.0, -6.0, 8.0, 6.0);
    savePixmap(pix, "lyapunov1.tga");
    puts("\ndone!\n");

    return 0;
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

