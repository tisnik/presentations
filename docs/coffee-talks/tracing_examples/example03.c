#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* jmeno souboru s vyslednou bitmapou */
#define FILE_NAME       "result.bmp"

/* rozmery bitmapy */
#define BITMAP_WIDTH    640
#define BITMAP_HEIGHT   480

/* struktura popisujici bitmapu */
typedef struct {
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} bitmap;

bitmap *pix;

/* sirka a vyska zakladniho obrazce v komplexni rovine */
#define WIDTH   2.0
#define HEIGHT  1.5

/* maximalni pocet iteraci */
#define MAXITER 1000

/* parametry vykreslovaneho fraktalu */
const double pcx = 1.491783;
const double pcy = 0.156788;
const double dist_est = 0.01;



/* ------------------------------------------------------------------ */
/* Funkce pro vytvoreni bitmapy o zadane velikosti                    */
/* ------------------------------------------------------------------ */
bitmap *createBitmap(const unsigned int width, const unsigned int height)
{
    bitmap *p = (bitmap *) malloc(sizeof(bitmap));      /* alokace struktury bitmapy */
    if (!p)
        return NULL;
    p->width = width;           /* naplneni struktury */
    p->height = height;
    p->pixels = (unsigned char *) malloc(3 * width * height);
    if (!p->pixels) {           /* alokace pole pro pixely */
        free(p);                /* alokace se nepovedla */
        return NULL;
    } else {
        memset(p->pixels, 0, 3 * width * height);       /* smazani bitmapy */
    }
    return p;
}



/* ------------------------------------------------------------------ */
/* Funkce pro zruseni bitmapy                                         */
/* ------------------------------------------------------------------ */
void destroybitmap(bitmap * p)
{
    if (p->pixels)
        free(p->pixels);        /* uvolnit vlastni bitmapu */
    if (p)
        free(p);                /* i okolni strukturu */
}



/* ------------------------------------------------------------------ */
/* Vymazani bitmapy                                                   */
/* ------------------------------------------------------------------ */
void clearBitmap(const bitmap * p)
{
    if (!p)
        return;
    if (!p->pixels)
        return;
    memset(p->pixels, 0, 3 * p->width * p->height);
}



/* ------------------------------------------------------------------ */
/* Ulozeni bitmapy do externiho souboru typu BMP                      */
/* ------------------------------------------------------------------ */
void saveBitmap(const bitmap * p, const char *fileName)
{
    unsigned char bmp_header[] = {      /* popis struktury hlavicky BMP: */
        0x42, 0x4d,             /* magic number */
        0x46, 0x00, 0x00, 0x00, /* size of header=70 bytes */
        0x00, 0x00,             /* unused */
        0x00, 0x00,             /* unused */
        0x36, 0x00, 0x00, 0x00, /* 54 bytes - offset to data */
        0x28, 0x00, 0x00, 0x00, /* 40 bytes - bytes in DIB header */
        0x00, 0x00, 0x00, 0x00, /* width of bitmap */
        0x00, 0x00, 0x00, 0x00, /* height of bitmap */
        0x01, 0x0,              /* 1 pixel plane */
        0x18, 0x00,             /* 24 bpp */
        0x00, 0x00, 0x00, 0x00, /* no compression */
        0x00, 0x00, 0x00, 0x00, /* size of pixel array */
        0x13, 0x0b, 0x00, 0x00, /* 2835 pixels/meter */
        0x13, 0x0b, 0x00, 0x00, /* 2835 pixels/meter */
        0x00, 0x00, 0x00, 0x00, /* color palette */
        0x00, 0x00, 0x00, 0x00, /* important colors */
    };
    FILE *fout;
    int width, height;

    width = p->width;
    height = p->height;

    bmp_header[18] = width & 0xff;
    bmp_header[19] = (width >> 8) & 0xff;
    bmp_header[20] = (width >> 16) & 0xff;
    bmp_header[21] = (width >> 24) & 0xff;
    bmp_header[22] = height & 0xff;
    bmp_header[23] = (height >> 8) & 0xff;
    bmp_header[24] = (height >> 16) & 0xff;
    bmp_header[25] = (height >> 24) & 0xff;

    fout = fopen(fileName, "wb");
    if (!fout)
        return;
    fwrite(bmp_header, sizeof(bmp_header), 1, fout);
    printf("%d pixels written\n", width * height);
    fwrite(p->pixels, 3 * width * height, 1, fout);
    fclose(fout);
}



/* ------------------------------------------------------------------ */
/* Zmena barvy pixelu na zadanych souradnicich                        */
/* ------------------------------------------------------------------ */
void putpixel(bitmap * p, const unsigned int x, /* pozice pixelu v bitmape */
              const unsigned int y, const unsigned char r,      /* barva pixelu */
              const unsigned char g, const unsigned char b)
{
    int pos;
    /* zde se vyuziva zkraceneho vyhodnoceni vyrazu - pokud plati !p, nic se dale netestuje */
    if (!p || !p->pixels || x >= p->width || y >= p->height)
        return;
    pos = 3 * (x + y * p->width);
    p->pixels[pos++] = b;       /* nastaveni barvy pixelu */
    p->pixels[pos++] = g;       /* pozor: format BMP je BGR a nikoli RGB! */
    p->pixels[pos] = b;
}



/* ------------------------------------------------------------------ */
/* Prekresleni Mandelbrotovy mnoziny s perturbaci                     */
/* ------------------------------------------------------------------ */
void recalcMandelbrot(bitmap * pix,     /* bitmapa pro vykreslovani */
                      int maxiter,      /* maximalni pocet iteraci */
                      double pcx,       /* hodnota komplexni konstanty C */
                      double pcy)
{
    double zx, zy, zx2, zy2;    /* slozky komplexni promenne Z a Z^2 */
    double cx, cy;              /* slozky komplexni konstanty C */
    double cx0, cy0;

    int x, y;                   /* pocitadla sloupcu a radku v bitmape */
    int iter;                   /* pocitadlo iteraci */
    unsigned char r, g, b;

    cy0 = -1.5;
    for (y = 0; y < pix->height; y++) { /* pro vsechny radky v bitmape */
        cx0 = -2.0;
        for (x = 0; x < pix->width; x++) {      /* pro vsechny pixely na radku */
            cx = cx0;           /* nastavit pocatecni hodnotu Z(0) */
            cy = cy0;
            zx = 0;
            zy = 0;
            for (iter = 0; iter < maxiter; iter++) {    /* iteracni smycka */
                zx2 = zx * zx;  /* zkraceny vypocet druhe mocniny slozek Z */
                zy2 = zy * zy;
                if (zx2 + zy2 > 4.0)
                    break;      /* kontrola prekroceni meze divergence */
                if (iter > 1) { /* rozsirujici podminka ukonceni smycky */
                    if (fabs(zx + pcx) < dist_est
                        || fabs(zy + pcy) < dist_est) {
                        break;
                    }
                }
                zy = 2.0 * zx * zy + cy;        /* vypocet Z(n+1) */
                zx = zx2 - zy2 + cx;
            }
            /* vypocet RGB */
            r = 127 + 127.0 * sin(iter / 30.0);
            g = iter * 30;
            b = 127 - 127.0 * sin(iter / 30.0);
            if (iter == maxiter) {
                putpixel(pix, x, y, 0, 0, 0);   /* body uvnitr mnoziny jsou cerne */
            } else {
                putpixel(pix, x, y, r, g, b);
            }
            cx0 += (4.0) / pix->width;  /* posun na dalsi bod na radku */
        }
        cy0 += (3.0) / pix->height;     /* posun na dalsi radek */
    }
}



/* ------------------------------------------------------------------ */
/* Hlavni funkce konzolove aplikace                                   */
/* ------------------------------------------------------------------ */
int main(int argc, char **argv)
{
    puts("processing:");

    /* vytvoreni a prvotni smazani bitmapy */
    pix = createBitmap(BITMAP_WIDTH, BITMAP_HEIGHT);
    clearBitmap(pix);

    /* vypocet fraktalu */
    recalcMandelbrot(pix, MAXITER, pcx, pcy);
    saveBitmap(pix, FILE_NAME);

    puts("done!\n");
    return 0;                   /* navratova hodnota */
}
