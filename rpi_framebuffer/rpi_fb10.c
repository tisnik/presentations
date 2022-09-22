/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 9: vykreslovani usecek: rychlejsi varianta
 *                               nepouzivajici funkci putpixel. */

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <linux/fb.h>
#include <linux/types.h>



#define ABS(x) ((x)<0 ? -(x) : (x))

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
 * Funkce line() platna pro nezname graficke rezimy.
 */
void lineNull(const int x1, const int y1, const int x2, const int y2,
              const unsigned char r, const unsigned char g,
              const unsigned char b, char *pixels, const int line_length)
{
}



/*
 * Funkce line platna pouze pro graficke rezimy true-color
 * s formatem 8-8-8-8 (popr. muze byt alfa kanal ignorovan).
 * Funkcni naproklad pro graficke karty Intel.
 */
void lineBGRA(const int x1, const int y1, const int x2, const int y2,
              const unsigned char r, const unsigned char g,
              const unsigned char b, char *pixels, const int line_length)
{
    /* vypocet adresy zapisu dat */
    /* pocitame v 32bitovych slovech, tj. line_length je nutne podelit ctyrmi */
    unsigned int index = x1 + (y1 * line_length >> 2);
    /* >> 2 nahrazuje deleni ctyrmi */

    /* vlastni provedeni vykresleni usecky */
    int x = x1;
    int y = y1;
    /* zrcadleni algoritmu pro dalsi oktanty */
    int dx = ABS(x2 - x1), sx = x1 < x2 ? 1 : -1;
    int dy = ABS(y2 - y1), sy = y1 < y2 ? 1 : -1;
    int err = (dx > dy ? dx : -dy) / 2, e2;

    /* uplna barva v jednom slove */
    __u32 color = (r << 16) | (g << 8) | b;
    __u32 *pixels32 = (__u32 *) pixels;

    /* pri posunu po x-ove ose se index musi zvysit ci snizit o 4 (bajty) tj. o 1 32-bitove slovo */
    int offsetX = x1 < x2 ? 1 : -1;
    /* pri posunu po y-ove ose se index musi zvysit ci snizit o delku radku (ve slovech) */
    int offsetY = y1 < y2 ? (line_length >> 2) : -(line_length >> 2);

    while (1) {
        /* vlastni provedeni zapisu barvy pixelu */
        *(pixels32 + index) = color;

        if (x == x2 && y == y2) {
            break;
        }
        e2 = err;
        if (e2 > -dx) {
            /* prepocet kumulovane chyby */
            err -= dy;
            /* posun na predchozi ci dalsi pixel na radku */
            x += sx;
            index += offsetX;
        }
        if (e2 < dy) {
            /* prepocet kumulovane chyby */
            err += dx;
            /* posun na predchozi ci nasledujici radek */
            y += sy;
            index += offsetY;
        }
    }
}



/*
 * Funkce line platna pouze pro graficke rezimy true-color
 * s formatem 8-8-8-8 (popr. muze byt alfa kanal ignorovan).
 * Funkcni pro Raspberry Pi s poradim bajtu R,G,B,A.
 */
void lineRGBA(const int x1, const int y1, const int x2, const int y2,
              const unsigned char r, const unsigned char g,
              const unsigned char b, char *pixels, const int line_length)
{
    lineBGRA(x1, y1, x2, y2, b, g, r, pixels, line_length);
}



/*
 * Funkce line platna pouze pro graficke rezimy hi-color
 * s formatem 5-6-5.
 */
void line565(const int x1, const int y1, const int x2, const int y2,
             const unsigned char r, const unsigned char g,
             const unsigned char b, char *pixels, const int line_length)
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
    unsigned int index = (x1 << 1) + y1 * line_length;
    /* << 1 nahrazuje nasobeni dvema */

    /* vykresleni usecky */
    int x = x1;
    int y = y1;
    /* zrcadleni algoritmu pro dalsi oktanty */
    int dx = ABS(x2 - x1), sx = x1 < x2 ? 1 : -1;
    int dy = ABS(y2 - y1), sy = y1 < y2 ? 1 : -1;
    int err = (dx > dy ? dx : -dy) / 2, e2;

    /* pri posunu po x-ove ose se index musi zvysit ci snizit o 2 (bajty) */
    int offsetX = x1 < x2 ? 2 : -2;
    /* pri posunu po y-ove ose se index musi zvysit ci snizit o delku radku (v bajtech) */
    int offsetY = y1 < y2 ? line_length : -line_length;

    while (1) {
        /* vlastni provedeni zapisu barvy pixelu */
        *(pixels + index) = byte1;
        *(pixels + index + 1) = byte2;

        if (x == x2 && y == y2) {
            break;
        }
        e2 = err;
        if (e2 > -dx) {
            /* prepocet kumulovane chyby */
            err -= dy;
            /* posun na predchozi ci dalsi pixel na radku */
            x += sx;
            index += offsetX;
        }
        if (e2 < dy) {
            /* prepocet kumulovane chyby */
            err += dx;
            /* posun na predchozi ci nasledujici radek */
            y += sy;
            index += offsetY;
        }
    }
}



/*
 * Novy datovy typ - ukazatel na (libovolnou) funkci line.
 */
typedef void (*LineFunction)(const int, const int, const int, const int,
                             const unsigned char, const unsigned char,
                             const unsigned char, char *, const int);




/*
 * Funkce, ktera vraci korektni funkci pro operaci line().
 */
LineFunction getProperLineFunction(int bits_per_pixel, int type,
                                   int visual, int redOffset)
{
    /* umime rozeznat pouze format bez bitovych rovin a bez palety */
    if (type == FB_TYPE_PACKED_PIXELS && visual == FB_VISUAL_TRUECOLOR) {
        if (bits_per_pixel == 16) {
            return line565;
        }
        if (bits_per_pixel == 32) {
            if (redOffset == 16) {
                return lineBGRA;
            } else {
                return lineRGBA;
            }
        }
    }
    return lineNull;
}



/*
 * Vykresleni testovaciho obrazku s vyuzitim funkce line.
 */
void drawTestImage(int framebufferDevice,
                   FramebufferInfo * framebufferInfoPtr,
                   ModeInfo * modeInfoPtr)
{
#define OFFSET 300
    /* casto pouzivane konstanty */
    const int buffer_length = modeInfoPtr->smem_len;
    const int pitch = modeInfoPtr->line_length;

    /* ziskame spravnou verzi funkce line */
    LineFunction line =
        getProperLineFunction(framebufferInfoPtr->bits_per_pixel,
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
            b = 255 - i;
            line(i * 3, 0, i * 3, 100, r, g, b, pixels, pitch);
            r = 255;
            g = i;
            b = 255 - i;
            line(i * 4, 150, i * 5, 250, r, g, b, pixels, pitch);
        }
        for (i = 0; i <= 300; i += 10) {
            line(0, 300 + i, i, 300 + 300, 255, 255, 255, pixels, pitch);

            line(300, 300, 600, 300 + i, 128, 128, 255, pixels, pitch);
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
