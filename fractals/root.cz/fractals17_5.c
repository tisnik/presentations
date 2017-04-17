//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Ukazkovy priklad cislo 17.5
// Autor: Pavel Tisnovsky
//
// Vytvareni animace Mandelbrotovy mnoziny s moznosti zmeny perturbace.
// Tento program vytvori serii 24bitovych obrazku, ktere budou obsahovat snimky
// animace "pruletu" Mandelbrotovou mnozinou.
// Po zpracovani externimi programy lze vytvorit ruzne formaty animaci, 
// napr. AVI, MPEG nebo FLI/FLC.
//-----------------------------------------------------------------------------

#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define FILE_NAME       "175_"                  // zacatek jmena souboru pro ulozeni pixmapy

#define PIXMAP_WIDTH    352                     // sirka pixmapy
#define PIXMAP_HEIGHT   288                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

pixmap *pix;

// sirka a vyska zakladniho obrazce v komplexni rovine
#define WIDTH   2.0
#define HEIGHT  1.5

#define MAXITER 128
#define FRAMES  300



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
// Ulozeni pixmapy do externiho souboru
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
// Prekresleni Mandelbrotovy mnoziny
//-----------------------------------------------------------------------------
void recalcMandelbrot( pixmap *pix,             // pixmapa pro vykreslovani
                  int    maxiter,               // maximalni pocet iteraci
                  double pcx,                   // hodnota komplexni konstanty C
                  double pcy)
{
    double zx, zy, zx2, zy2;                    // slozky komplexni promenne Z a Z^2
    double cx, cy;                              // slozky komplexni konstanty C
    double cx0, cy0;

    int    x, y;                                // pocitadla sloupcu a radku v pixmape
    int    iter;                                // pocitadlo iteraci
    unsigned char r, g, b;

    cy0=-1.5;
    for (y=0; y<pix->height; y++) {             // pro vsechny radky v pixmape
        cx0=-2.0;
        for (x=0; x<pix->width; x++) {          // pro vsechny pixely na radku
            cx=cx0;                             // nastavit pocatecni hodnotu Z(0)
            cy=cy0;
            zx=0; zy=0;
            for (iter=0; iter<maxiter; iter++) {// iteracni smycka
                zx2=zx*zx;                      // zkraceny vypocet druhe mocniny slozek Z
                zy2=zy*zy;
                if (zx2+zy2>4.0) break;         // kontrola prekroceni meze divergence
                if (iter>1)                     // rozsirujici podminka ukonceni smycky
                    if (fabs(zx+pcx)<0.01 || fabs(zy+pcy)<0.01)
                        break;
                zy=2.0*zx*zy+cy;                // vypocet Z(n+1)
                zx=zx2-zy2+cx;
            }
            r=127+127.0*sin(iter/30.0);
            g=iter*30;
            b=127-127.0*sin(iter/30.0);
            if (iter==maxiter)
                putpixel(pix, x, y, 0, 0, 0);   // body uvnitr mnoziny jsou cerne
            else
                putpixel(pix, x, y, r, g, b);
            cx0+=(4.0)/pix->width;              // posun na dalsi bod na radku
        }
        cy0+=(3.0)/pix->height;                 // posun na dalsi radek
    }
}



//-----------------------------------------------------------------------------
// Hlavni funkce konzolove aplikace
//-----------------------------------------------------------------------------
int main(int argc, char **argv)
{
    int    i;
    char   name[50];
    double pcx;
    double pcy;
    double amp=1.5;

    puts("\nfractals17_5\n");
    puts("processing:");

    // vytvoreni a prvotni smazani pixmapy
    pix=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
    clearPixmap(pix);

    // zmena perturbace a vytvareni animaci
    for (i=0; i<FRAMES; i++) {
        sprintf(name, "%s%03d%s", FILE_NAME, i, ".tga");
        printf("%3d\t", i);
        pcx=amp*cos(10.0*3.1415*i/FRAMES);      // spirala koncici v bode 0+0i
        pcy=amp*sin(10.0*3.1415*i/FRAMES);
        amp=1.5-1.5*i/FRAMES;
        recalcMandelbrot(pix, MAXITER, pcx, pcy);
        savePixmap(pix, name);
    }
    puts("\ndone!\n");
    return 0;                                   // navratova hodnota
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

