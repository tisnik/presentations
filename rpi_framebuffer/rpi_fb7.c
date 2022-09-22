/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 7: rozdil mezi formatem RGBA a BGRA
 *                               pri vykreslovani pixelu. */

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <linux/fb.h>



/*
 * Datova struktura, do niz se ulozi informace o framebufferu.
 * Blizsi informace o teto strukture je mozne nalezt v hlavickovem souboru
 * dostupnem v adresari "/usr/include/linux/fb.h"
 */
typedef struct fb_var_screeninfo FramebufferInfo;



/*
 * Druha datova struktura popisujici zbyvajici vlastnosti framebufferu.
 * Blizsi informace o teto strukture je mozne nalezt v hlavickovem souboru
 * dostupnem v adresari "/usr/include/linux/fb.h"
 */
typedef struct fb_fix_screeninfo ModeInfo;



/*
 * Precteni vsech relevantnich informaci zjistenych o framebufferu. Pro korektni
 * funkci je zapotrebi, aby mel uzivatel pristup k zarizeni /dev/fb0
 * (postacuje byt ve skupine 'video' ci pouziti su/sudo)
 */
int readFramebufferInfo(int framebufferDevice,
                        FramebufferInfo * framebufferInfoPtr,
                        ModeInfo * modeInfoPtr)
{
    /* Pokud operace ioctl probehne v poradku, vrati se 0 */
    if (ioctl(framebufferDevice, FBIOGET_VSCREENINFO, framebufferInfoPtr)) {
        perror("Nelze precist informace o framebufferu");
        return 0;
    }

    /* Pokud operace ioctl probehne v poradku, vrati se 0 */
    if (ioctl(framebufferDevice, FBIOGET_FSCREENINFO, modeInfoPtr)) {
        perror("Nelze precist informace o rezimu");
        return 0;
    }
    return 1;
}



/*
 * Funkce putpixel platna pro nezname graficke rezimy.
 */
void putpixelNull(const int x, const int y,
                  const char r, const char g, const char b,
                  char *pixels, const int line_length)
{
}



/*
 * Funkce putpixel platna pouze pro graficke rezimy true-color
 * s formatem 8-8-8-8 (popr. muze byt alfa kanal ignorovan).
 * Funkcni napriklad pro graficke karty Intel.
 */
void putpixelBGRA(const int x, const int y,
                  const char r, const char g, const char b,
                  char *pixels, const int line_length)
{
    /* vypocet adresy zapisu dat */
    unsigned int index = (x << 2) + y * line_length;
    /* << 2 nahrazuje nasobeni ctyrmi */

    /* vlastni provedeni zapisu */
    *(pixels + index) = b;
    index++;
    *(pixels + index) = g;
    index++;
    *(pixels + index) = r;
}



/*
 * Funkce putpixel platna pouze pro graficke rezimy true-color
 * s formatem 8-8-8-8 (popr. muze byt alfa kanal ignorovan).
 * Funkcni pro Raspberry Pi s poradim bajtu R,G,B,A.
 */
void putpixelRGBA(const int x, const int y,
                  const char r, const char g, const char b,
                  char *pixels, const int line_length)
{
    putpixelBGRA(x, y, b, g, r, pixels, line_length);
}



/*
 * Funkce putpixel platna pouze pro graficke rezimy hi-color
 * s formatem 5-6-5.
 */
void putpixel565(const int x, const int y,
                 const char r, const char g, const char b,
                 char *pixels, const int line_length)
{
#define RED_OFFSET     11
#define GREEN_OFFSET    5
#define BLUE_OFFSET     0
#define RED_LOST_BITS   3
#define GREEN_LOST_BITS 2
#define BLUE_LOST_BITS  3
    /* vypocet barvy pixelu, v zavorce nejdrive snizime bitovou sirku
     * rezervovanou pro jednotlive barvove slozky a posleze bity, ktere
     * reprezentuji barvovou slozku posuneme do spravne pozice ve slove */
    unsigned int pixel_value = (r >> RED_LOST_BITS) << RED_OFFSET |
        (g >> GREEN_LOST_BITS) << GREEN_OFFSET |
        (b >> BLUE_LOST_BITS) << BLUE_OFFSET;

    /* prevod na dvojici bajtu */
    unsigned char byte1 = pixel_value & 0xff;
    unsigned char byte2 = pixel_value >> 8;

    /* vypocet adresy zapisu dat */
    unsigned int index = (x << 1) + y * line_length;
    /* << 1 nahrazuje nasobeni dvema */

    /* vlastni provedeni zapisu */
    *(pixels + index) = byte1;
    index++;
    *(pixels + index) = byte2;
}



/*
 * Novy datovy typ - ukazatel na (libovolnou) funkci putpixel.
 */
typedef void (*PutpixelFunction)(const int, const int,
                                 const char, const char, const char,
                                 char *, const int);



/*
 * Funkce, ktera vraci korektni funkci pro operaci putpixel().
 */
PutpixelFunction getProperPutpixelFunction(int bits_per_pixel, int type,
                                           int visual, int redOffset)
{
    /* umime rozeznat pouze format bez bitovych rovin a bez palety */
    if (type == FB_TYPE_PACKED_PIXELS && visual == FB_VISUAL_TRUECOLOR) {
        if (bits_per_pixel == 16) {
            return putpixel565;
        }
        if (bits_per_pixel == 32) {
            if (redOffset == 16) {
                return putpixelBGRA;
            } else {
                return putpixelRGBA;
            }
        }
    }
    return putpixelNull;
}



/*
 * Vykresleni testovaciho obrazku s vyuzitim funkce putpixel.
 */
void drawTestImage(int framebufferDevice,
                   FramebufferInfo * framebufferInfoPtr,
                   ModeInfo * modeInfoPtr)
{
#define OFFSET 300
    /* casto pouzivane konstanty */
    const int buffer_length = modeInfoPtr->smem_len;
    const int xres = framebufferInfoPtr->xres;
    const int yres = framebufferInfoPtr->yres;

    /* ziskame spravnou verzi funkce putpixel */
    PutpixelFunction putpixel =
        getProperPutpixelFunction(framebufferInfoPtr->bits_per_pixel,
                                  modeInfoPtr->type,
                                  modeInfoPtr->visual,
                                  framebufferInfoPtr->red.offset);

    /* ziskat primy pristup do framebufferu */
    char *pixels = (char *) mmap(0, buffer_length,
                                 PROT_READ | PROT_WRITE,
                                 MAP_SHARED, framebufferDevice,
                                 0);

    if (pixels != MAP_FAILED) {
        int x, y;
        int r, g, b;
        /* nejprve vymazeme cely framebuffer */
        memset(pixels, 0, buffer_length);

        /* vykreslime nekolik ctvercu o velikosti 256x256 pixelu
         * s gradientnim barevnym prechodem */
        for (y = 0; y < 256; y++) {
            for (x = 0; x < 256; x++) {
                /* prvni rada - gradientni prechody */
                if (yres > 256) {
                    /* cerveny gradient */
                    if (xres > 256) {
                        r = y;
                        g = 0;
                        b = 0;
                        putpixel(x, y, r, g, b, pixels,
                                 modeInfoPtr->line_length);
                    }
                    /* zeleny gradient */
                    if (xres > 256 + OFFSET) {
                        r = 0;
                        g = y;
                        b = 0;
                        putpixel(OFFSET + x, y, r, g, b, pixels,
                                 modeInfoPtr->line_length);
                    }
                    /* modry gradient */
                    if (xres > 256 + OFFSET * 2) {
                        r = 0;
                        g = 0;
                        b = y;
                        putpixel(OFFSET * 2 + x, y, r, g, b, pixels,
                                 modeInfoPtr->line_length);
                    }
                    /* grayscale gradient */
                    if (xres > 256 + OFFSET * 3) {
                        r = y;
                        g = y;
                        b = y;
                        putpixel(OFFSET * 3 + x, y, r, g, b, pixels,
                                 modeInfoPtr->line_length);
                    }
                }

                /* druha rada - palety */
                if (yres > 256 + OFFSET) {
                    if (xres > 256) {
                        r = x;
                        g = y;
                        b = 0;
                        putpixel(x, OFFSET + y, r, g, b, pixels,
                                 modeInfoPtr->line_length);
                    }
                    if (xres > 256 + OFFSET) {
                        r = x;
                        g = y;
                        b = 255;
                        putpixel(OFFSET + x, OFFSET + y, r, g, b, pixels,
                                 modeInfoPtr->line_length);
                    }
                    if (xres > 256 + OFFSET * 2) {
                        r = 255;
                        g = x;
                        b = y;
                        putpixel(OFFSET * 2 + x, OFFSET + y, r, g, b,
                                 pixels, modeInfoPtr->line_length);
                    }
                    if (xres > 256 + OFFSET * 3) {
                        r = y;
                        g = 255;
                        b = x;
                        putpixel(OFFSET * 3 + x, OFFSET + y, r, g, b,
                                 pixels, modeInfoPtr->line_length);
                    }
                }
            }
        }
        getchar();
        munmap(pixels, buffer_length);
    } else {
        perror("Nelze pristupovat k framebufferu");
    }
}



/* Vstupni bod do demonstracniho prikladu... :) */
int main(int argc, char **argv)
{
    FramebufferInfo framebufferInfo;
    ModeInfo modeInfo;
    int framebufferDevice = 0;

    /* Ze zarizeni potrebujeme cist i zapisovat. */
    framebufferDevice = open("/dev/fb0", O_RDWR);

    /* Pokud otevreni probehlo uspesne, nacteme
     * a nasledne vypiseme informaci o framebufferu.*/
    if (framebufferDevice != -1) {
        /* Precteni informaci o framebufferu a test, zda se vse podarilo */
        if (readFramebufferInfo
            (framebufferDevice, &framebufferInfo, &modeInfo)) {
            drawTestImage(framebufferDevice, &framebufferInfo, &modeInfo);
        }
        close(framebufferDevice);
        return 0;
    }
    /* Otevreni se nezadarilo, vypiseme tudiz pouze chybove hlaseni. */
    else {
        perror("Nelze otevrit ovladac /dev/fb0");
        return 1;
    }
}



/* finito */
