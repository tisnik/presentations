/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 12: vykreslovani usecek s antialiasingem. */
/*                                (neoptimalizovana varianta) */

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
 * Plati pro format 565
 */
#define RED_OFFSET     11
#define GREEN_OFFSET    5
#define BLUE_OFFSET     0
#define RED_LOST_BITS   3
#define GREEN_LOST_BITS 2
#define BLUE_LOST_BITS  3
#define RED_MASK        0x1F    /* 0001 1111 */
#define GREEN_MASK      0x3F    /* 0011 1111 */
#define BLUE_MASK       0x1F    /* 0001 1111 */



/*
 * Funkce putpixel platna pouze pro graficke rezimy hi-color
 * s formatem 5-6-5.
 */
void putpixel565(const int x, const int y,
                 const char r, const char g, const char b,
                 char *pixels, const int line_length)
{
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
        /* framebuffer s bitovou hloubkou 16bpp */
        if (bits_per_pixel == 16) {
            return putpixel565;
        }
        /* framebuffery s bitovou hloubkou 32bpp */
        if (bits_per_pixel == 32) {
            /* rozlisujeme podle pozice cervene slozky */
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
 * Nekolik maker pouzitych v algoritmech pro vykreslovani usecek.
 */
#define ABS(x) ((x)<0 ? -(x) : (x))
#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))



/*
 * Specialni pripad: vodorovna usecka.
 */
void horizontalLine(const int x1, const int x2, const int y,
                    char *pixels, const int line_length,
                    PutpixelFunction putpixel)
{
    int x;
    int from_x = MIN(x1, x2);
    int to_x = MAX(x1, x2);
    for (x = from_x; x <= to_x; x++) {
        putpixel(x, y, 0xff, 0xff, 0xff, pixels, line_length);
    }
}



/*
 * Specialni pripad: svisla usecka.
 */
void verticalLine(const int x, const int y1, const int y2,
                  char *pixels, const int line_length,
                  PutpixelFunction putpixel)
{
    int y;
    int from_y = MIN(y1, y2);
    int to_y = MAX(y1, y2);
    for (y = from_y; y <= to_y; y++) {
        putpixel(x, y, 0xff, 0xff, 0xff, pixels, line_length);
    }
}



/*
 * Funkce pro vykresleni usecky Bresenhamovym algoritmem.
 * (tj. bez antialiasingu)
 */
void line(const int x1, const int y1, const int x2, const int y2,
          char *pixels, const int line_length, PutpixelFunction putpixel)
{
    /* specialni pripad - svisla usecka */
    if (x1 == x2) {
        verticalLine(x1, y1, y2, pixels, line_length, putpixel);
        return;
    }

    /* specialni pripad - vodorovna usecka */
    if (y1 == y2) {
        horizontalLine(x1, x2, y1, pixels, line_length, putpixel);
        return;
    }

    /* mame smulu a musime pouzit plnou verzi algoritmu */

    /* zrcadleni algoritmu pro dalsi oktanty */
    int x = x1;
    int y = y1;

    /* konstanty pouzite pri vykreslovani */
    int dx = ABS(x2 - x1), sx = x1 < x2 ? 1 : -1;
    int dy = ABS(y2 - y1), sy = y1 < y2 ? 1 : -1;
    int err = (dx > dy ? dx : -dy) / 2, e2;

    while (1) {
        putpixel(x, y, 0xff, 0xff, 0xff, pixels, line_length);
        /* test, zda se jiz doslo k poslednimu bodu */
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
 * Funkce pro vykresleni usecky s aplikaci antialiasingu.
 */
void lineAA(const int x1, const int y1, const int x2, const int y2,
            char *pixels, const int line_length, PutpixelFunction putpixel)
{
    /* specialni pripad - svisla usecka */
    if (x1 == x2) {
        verticalLine(x1, y1, y2, pixels, line_length, putpixel);
        return;
    }

    /* specialni pripad - vodorovna usecka */
    if (y1 == y2) {
        horizontalLine(x1, x2, y1, pixels, line_length, putpixel);
        return;
    }

    /* mame smulu a musime pouzit plnou verzi algoritmu */

    /* konstanty pouzite pri vykreslovani */
    int dx = x2 - x1;
    int dy = y2 - y1;
    double s, p, e = 255.0;
    int x, y, xdelta, ydelta, xpdelta, ypdelta, xp, yp;
    int i, imin, imax;

    /* pomocne promenne - pocatecni a koncove body */
    int xx1 = x1 < x2 ? x1 : x2;
    int xx2 = x1 < x2 ? x2 : x1;
    int yy1 = x1 < x2 ? y1 : y2;
    int yy2 = x1 < x2 ? y2 : y1;

    /* nastaveni pro sklony mensi nez 45 stupnu */
    if (ABS(dx) > ABS(dy)) {
        s = (double) dy / (double) dx;
        imin = xx1;
        imax = xx2;
        x = xx1;
        y = yy1;
        xdelta = 1;
        ydelta = 0;
        xpdelta = 0;
        xp = 0;
        if (yy2 > yy1) {
            ypdelta = 1;
            yp = 1;
        } else {
            s = -s;
            ypdelta = -1;
            yp = -1;
        }
    }
    /* nastaveni pro sklony vetsi nez 45 stupnu */
    else {
        s = (double) dx / (double) dy;
        xdelta = 0;
        ydelta = 1;
        ypdelta = 0;
        yp = 0;
        if (yy2 > yy1) {
            imin = yy1;
            imax = yy2;
            x = xx1;
            y = yy1;
            xpdelta = 1;
            xp = 1;
        } else {
            s = -s;
            imin = yy2;
            imax = yy1;
            x = xx2;
            y = yy2;
            xpdelta = -1;
            xp = -1;
        }
    }
    /* vlastni vykreslovaci smycka (zde bez optimalizaci!) */
    p = s * 256.0;
    for (i = imin; i <= imax; i++) {
        int c1 = (int) e;
        int c2 = 255 - c1;
        putpixel(x + xp, y + yp, c2, c2, c2, pixels, line_length);
        putpixel(x, y, c1, c1, c1, pixels, line_length);
        e = e - p;
        x += xdelta;
        y += ydelta;
        if (e < 0.0) {
            e += 256.0;
            x += xpdelta;
            y += ypdelta;
        }
    }
}



/*
 * Ulozeni obsahu framebufferu do souboru s rastrovym obrazkem.
 */
void saveFramebuffer(const char *filename,
                     FramebufferInfo * framebufferInfoPtr, char *pixels)
{
    const int bpp = framebufferInfoPtr->bits_per_pixel;
    const int xres = framebufferInfoPtr->xres;
    const int yres = framebufferInfoPtr->yres;

    FILE *fout = fopen(filename, "wb");
    int i;
    char *adr = pixels;

    if (!fout) {
        perror("Unable to open output file");
        return;
    }

    /* hlavicka souboru s rastrovym obrazkem */
    fprintf(fout, "P6\n");
    fprintf(fout, "%d\n%d\n255\n", xres, yres);

    switch (bpp) {
    case 16:                   /* 16bitova barvova hloubka, predpokladejme format 565 */
        for (i = 0; i < xres * yres; i++) {
            /* nejprve se prectou dva bajty z framebufferu */
            unsigned char b1 = *(adr + 1);
            unsigned char b2 = *(adr);
            /* posleze se prevedou na 16bitove slovo */
            unsigned int color = (b1 << 8) + b2;
            /* a zase ziskame zpetnym prevodem hodnoty barvovych slozek */
            /* 1) nejprve je 16bitove slovo posunuto doprava tak, aby se ve spodnich bitech nachazela prislusna slozka */
            /* 2) posleze se provede maskovani spodnich peti ci sesti bitu, vysledkem je 16bitove slovo s nulovymi 10 ci 9 bity */
            /* 3) nasledne se onech 5 ci 6 bitu posune doleva, aby vznikla osmibitova hodnota barvy */
            unsigned char r =
                ((color >> RED_OFFSET) & RED_MASK) << RED_LOST_BITS;
            unsigned char g =
                ((color >> GREEN_OFFSET) & GREEN_MASK) << GREEN_LOST_BITS;
            unsigned char b =
                ((color >> BLUE_OFFSET) & BLUE_MASK) << BLUE_LOST_BITS;
            /* zapis barvovych slozek */
            putc(r, fout);
            putc(g, fout);
            putc(b, fout);
            adr += 2;           /* posun na dalsi pixel ve framebufferu */
        }
        break;
    case 24:                   /* 24bitova barvova hloubka - lze nahradit jedinym zapisem, pokud nebudete prehazovat barvy! */
        for (i = 0; i < xres * yres; i++) {
            fwrite(adr + 2, 1, 1, fout);
            fwrite(adr + 1, 1, 1, fout);
            fwrite(adr + 0, 1, 1, fout);
            adr += 3;           /* posun na dalsi pixel ve framebufferu */
        }
        break;
    case 32:                   /* 32bitova barvova hloubka */
        for (i = 0; i < xres * yres; i++) {
            fwrite(adr + 2, 1, 1, fout);
            fwrite(adr + 1, 1, 1, fout);
            fwrite(adr + 0, 1, 1, fout);
            adr += 4;           /* posledni bajt se busi preskocit, neuklada se */
        }
        break;
    }
    fclose(fout);
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
        /* nejprve vymazeme cely framebuffer */
        memset(pixels, 0, buffer_length);

        /* vykreslime nekolik usecek s ruznym sklonem (vzdy bude mit jeden "schod") */
        for (i = 0; i <= 350; i += 10) {
            /* bez antialiasingu */
            line(0, i, i * 2, i + 1, pixels, pitch, putpixel);
            /* s antialiasingem */
            lineAA(0, 400 + i, i * 2, 400 + 1 + i, pixels, pitch,
                   putpixel);
        }
        /* ulozeni framebufferu */
        saveFramebuffer("rpi_fb12.ppm", framebufferInfoPtr, pixels);
        /* cekani na stisk klavesy */
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
