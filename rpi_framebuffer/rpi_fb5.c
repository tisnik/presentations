/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 5: ziskani informaci o grafickem rezimu */
/*                               a o zpusobu kodovani jednotlivych pixelu */

#include <stdio.h>
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
 * Vypis podrobnejsich informaci o zpusobu zakodovani jedne barvove slozky
 * pixelu ve framebufferu. Zobrazene informace maji vyznam pouze ve chvili,
 * kdy se nepouzivaji graficke rezimy s barvovovu paletou.
 */
void printColorInfo(const char *message,
                    const struct fb_bitfield colorInfo)
{
    puts(message);
    printf("    sirka:  %d\n", colorInfo.length);
    printf("    offset: %d\n", colorInfo.offset);
    printf("    MSB:    %s\n", colorInfo.msb_right ? "vpravo" : "vlevo");
}



/*
 * Ziskani informace o typu framebufferu.
 */
const char *getFramebufferType(const int type)
{
    static const char *FRAMEBUFFER_TYPES[] = {
        "Packed Pixels",
        "Non interleaved planes",
        "Interleaved planes",
        "Text/attributes",
        "EGA/VGA planes"
    };
    if (type >= FB_TYPE_PACKED_PIXELS && type <= FB_TYPE_VGA_PLANES) {
        /* vypocet indexu do pole retezcu */
        return FRAMEBUFFER_TYPES[type - FB_TYPE_PACKED_PIXELS];
    }
    return "unknown";
}



/*
 * Ziskani informace rezimu zobrazovani.
 */
const char *getVideoMode(const int mode)
{
    static const char *VIDEO_MODE_TYPES[] = {
        "non interlaced",
        "interlaced",
        "non interlaced, double scan",
        "interlaced, double scan"
    };
    int index = mode & 0x03;
    return VIDEO_MODE_TYPES[index];
}



/*
 * Ziskani informace grafickem rezimu.
 */
const char *getGraphicsMode(const int mode)
{
    static const char *GRAPHIC_MODES[] = {
        "Monochr. 1=Black 0=White",
        "Monochr. 1=White 0=Black",
        "True color",
        "Pseudo color (like Atari)",
        "Direct color",
        "Pseudo color readonly"
    };
    if (mode >= FB_VISUAL_MONO01 && mode <= FB_VISUAL_STATIC_PSEUDOCOLOR) {
        /* vypocet indexu do pole retezcu */
        return GRAPHIC_MODES[mode - FB_VISUAL_MONO01];
    }
    return "unknown";
}



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

    if (ioctl(framebufferDevice, FBIOGET_FSCREENINFO, modeInfoPtr)) {
        perror("Nelze precist informace o rezimu");
        return 0;
    }
    return 1;
}



/*
 * Vypis vsech relevantnich informaci zjistenych o framebufferu.
 */
void printFramebufferInfo(int framebufferDevice,
                          FramebufferInfo * framebufferInfoPtr,
                          ModeInfo * modeInfoPtr)
{
    /* Nyni je datova struktura FramebufferInfo naplnena. */
    printf("Realne rozliseni:       %dx%d pixelu\n",
           framebufferInfoPtr->xres, framebufferInfoPtr->yres);
    printf("Virtualni rozliseni:    %dx%d pixelu\n",
           framebufferInfoPtr->xres_virtual,
           framebufferInfoPtr->yres_virtual);
    printf("Odstiny sedi:           %s\n",
           framebufferInfoPtr->grayscale ? "ano" : "ne");
    printf("Nestandardni format:    %s\n",
           framebufferInfoPtr->nonstd ? "ano" : "ne");
    printf("Rezim zobrazovani:      %d == %s\n", framebufferInfoPtr->vmode,
           getVideoMode(framebufferInfoPtr->vmode));

    printf("Bitu na pixel:          %d bitu\n",
           framebufferInfoPtr->bits_per_pixel);
    printColorInfo("Cervena barvova slozka (RED):",
                   framebufferInfoPtr->red);
    printColorInfo("Zelena barvova slozka (GREEN):",
                   framebufferInfoPtr->green);
    printColorInfo("Modra barvova slozka (BLUE):",
                   framebufferInfoPtr->blue);
    printColorInfo("Alfa kanal (ALPHA):", framebufferInfoPtr->transp);

    putchar('\n');

    /* Nyni je datova struktura modeInfo naplnena. */
    printf("Identifikace:            %s\n", modeInfoPtr->id);
    printf("Delka obrazoveho radku:  %d bajtu\n",
           modeInfoPtr->line_length);
    printf("Velikost framebufferu:   %d bajtu\n", modeInfoPtr->smem_len);
    printf("Organizace framebufferu: %d == %s\n", modeInfoPtr->type,
           getFramebufferType(modeInfoPtr->type));
    printf("Graficky rezim:          %d == %s\n", modeInfoPtr->visual,
           getGraphicsMode(modeInfoPtr->visual));
}



/* Vstupni bod do demonstracniho prikladu... :) */
int main(int argc, char **argv)
{
    FramebufferInfo framebufferInfo;
    ModeInfo modeInfo;
    int framebufferDevice = 0;

    /* Ze zarizeni potrebujeme pouze cist. */
    framebufferDevice = open("/dev/fb0", O_RDONLY);

    /* Pokud otevreni probehlo uspesne, nacteme
     * a nasledne vypiseme informaci o framebufferu.*/
    if (framebufferDevice != -1) {
        /* Precteni informaci o framebufferu a test, zda se vse podarilo */
        if (readFramebufferInfo
            (framebufferDevice, &framebufferInfo, &modeInfo)) {
            printFramebufferInfo(framebufferDevice, &framebufferInfo,
                                 &modeInfo);
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
