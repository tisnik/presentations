/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 8: pomale vykreslovani usecek. */

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
 * Funkce pro vykresleni usecky.
 */
void line(const int x1, const int y1, const int x2, const int y2,
          const char r, const char g, const char b,
          char *pixels, const int line_length, PutpixelFunction putpixel)
{
#define ABS(x) ((x)<0 ? -(x) : (x))
    int x = x1;
    int y = y1;
    /* zrcadleni algoritmu pro dalsi oktanty */
    int dx = ABS(x2 - x1), sx = x1 < x2 ? 1 : -1;
    int dy = ABS(y2 - y1), sy = y1 < y2 ? 1 : -1;
    int err = (dx > dy ? dx : -dy) / 2, e2;

    while (1) {
        putpixel(x, y, r, g, b, pixels, line_length);
        if (x == x2 && y == y2) {
            break;
        }
        e2 = err;
        if (e2 > -dx) {
            /* prepocet kumulovane chyby */
            err -= dy;
            /* posun na predchozi ci dalsi pixel na radku */
            x += sx;
        }
        if (e2 < dy) {
            /* prepocet kumulovane chyby */
            err += dx;
            /* posun na predchozi ci nasledujici radek */
            y += sy;
        }
    }
}



/*
 * Vykresleni testovaciho obrazku s vyuzitim funkci line a putpixel.
 */
void drawTestImage(int framebufferDevice,
                   FramebufferInfo * framebufferInfoPtr,
                   ModeInfo * modeInfoPtr)
{
#define OFFSET 300
    /* casto pouzivane konstanty */
    const int buffer_length = modeInfoPtr->smem_len;
    const int pitch = modeInfoPtr->line_length;

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
        int i;
        int r, g, b;
        /* nejprve vymazeme cely framebuffer */
        memset(pixels, 0, buffer_length);

        /* vykreslime nekolik usecek s ruznym sklonem a barvou */
        for (i = 0; i < 256; i++) {
            r = i;
            g = i;
            b = 256 - i;
            line(i * 3, 0, i * 3, 100, r, g, b, pixels, pitch, putpixel);
            r = 255;
            g = i;
            b = 255 - i;
            line(i * 4, 150, i * 5, 250, r, g, b, pixels, pitch, putpixel);
        }
        for (i = 0; i <= 300; i += 10) {
            line(0, 300 + i, i, 300 + 300, 255, 255, 255, pixels, pitch,
                 putpixel);

            line(300, 300, 600, 300 + i, 128, 128, 255, pixels, pitch,
                 putpixel);
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
