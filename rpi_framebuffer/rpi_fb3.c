/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 3: zapis do framebufferu */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <linux/fb.h>

/* Datova struktura, do niz se ulozi informace o framebufferu. */
typedef struct fb_var_screeninfo FramebufferInfo;

typedef struct fb_fix_screeninfo ModeInfo;

long int printFramebufferInfo(int framebufferDevice)
{
    FramebufferInfo framebufferInfo;
    ModeInfo modeInfo;

    /* Pokud operace ioctl probehne v poradku, vrati se 0 */
    if (ioctl(framebufferDevice, FBIOGET_VSCREENINFO, &framebufferInfo)) {
        perror("Nelze precist informace o framebufferu");
        return 0;
    }
    /* Nyni je datova struktura FramebufferInfo naplnena. */
    printf("Realne rozliseni:       %dx%d pixelu\n", framebufferInfo.xres,
           framebufferInfo.yres);
    printf("Virtualni rozliseni:    %dx%d pixelu\n",
           framebufferInfo.xres_virtual, framebufferInfo.yres_virtual);
    printf("Bitu na pixel:          %d bitu\n",
           framebufferInfo.bits_per_pixel);

    if (ioctl(framebufferDevice, FBIOGET_FSCREENINFO, &modeInfo)) {
        perror("Nelze precist informace o rezimu");
        return 0;
    }
    /* Nyni je datova struktura ModeInfo naplnena. */
    printf("Identifikace:           %s\n", modeInfo.id);
    printf("Delka obrazoveho radku: %d bajtu\n", modeInfo.line_length);
    printf("Velikost framebuffer:   %d bajtu\n", modeInfo.smem_len);

    return modeInfo.smem_len;
}

void draw(int framebufferDevice, long int bufferSize)
{
    char *pixels = (char *) mmap(0, bufferSize,
                                 PROT_READ | PROT_WRITE,
                                 MAP_SHARED, framebufferDevice,
                                 0);
    if (pixels != MAP_FAILED) {
        int x;
        for (x = 0; x < bufferSize; x++)
            pixels[x] = x;
        getchar();
        munmap(pixels, bufferSize);
    } else {
        perror("Nelze pristupovat k framebufferu");
    }
}

int main(int argc, char **argv)
{
    int framebufferDevice = 0;

    /* Ze zarizeni potrebujeme pouze cist. */
    framebufferDevice = open("/dev/fb0", O_RDWR);

    /* Pokud otevreni probehlo uspesne, nacteme
     * a nasledne vypiseme informaci o framebufferu.*/
    if (framebufferDevice != -1) {
        long int bufferSize = printFramebufferInfo(framebufferDevice);
        if (bufferSize) {
            draw(framebufferDevice, bufferSize);
        }
        close(framebufferDevice);
        return 0;
    }
    /* Otevreni se nezadarilo, vypiseme chybove hlaseni. */
    else {
        perror("Nelze otevrit ovladac /dev/fb0");
        return 1;
    }
}
