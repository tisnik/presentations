#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

/* jmeno souboru s vyslednou bitmapou */
#define FILE_NAME       "random.bmp"

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
/* Naplneni bitmapy nahodnym vzorkem                                  */
/* ------------------------------------------------------------------ */
void fillBitmap(const bitmap * p)
{
    int randomDataDevice = open("/dev/urandom", O_RDONLY);
    size_t i;
    unsigned char *pixels_ptr = p->pixels;
    for (i = 0; i < p->height; i++) {
        /* nacteni celeho radku */
        ssize_t result = read(randomDataDevice, pixels_ptr, 3 * p->width);
        if (result >= 0) {
            /* posun ukazatele na dalsi radek */
            pixels_ptr += result;
        } else {
            perror("urandom read failed");
            close(randomDataDevice);
            return;
        }
    }
    close(randomDataDevice);
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
    fillBitmap(pix);

    saveBitmap(pix, FILE_NAME);

    puts("done!\n");
    return 0;                   /* navratova hodnota */
}



/* ------------------------------------------------------------------ */
/* finito                                                             */
/* ------------------------------------------------------------------ */
