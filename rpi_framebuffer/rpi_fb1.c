/* Framebuffer na jednodeskovem mikropocitaci Raspberry Pi */
/* Autor: Pavel Tisnovsky, 2016 */

/* Demonstracni priklad cislo 1: otevreni zarizeni /dev/fb0  */
/*                               a precteni zakladnich informaci o framebufferu */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/fb.h>

/* Datova struktura, do niz se ulozi informace o framebufferu. */
typedef struct fb_var_screeninfo FramebufferInfo;

void printFramebufferInfo(int framebufferDevice)
{
    FramebufferInfo framebufferInfo;
    /* Pokud operace ioctl probehne v poradku, vrati se 0 */
    if (ioctl(framebufferDevice, FBIOGET_VSCREENINFO, &framebufferInfo)) {
        perror("Nelze precist informace o framebufferu");
        return;
    }
    /* Nyni je datova struktura FramebufferInfo naplnena. */
    printf("Realne rozliseni:    %dx%d\n", framebufferInfo.xres,
           framebufferInfo.yres);
    printf("Virtualni rozliseni: %dx%d\n", framebufferInfo.xres_virtual,
           framebufferInfo.yres_virtual);
    printf("Bitu na pixel:       %d\n", framebufferInfo.bits_per_pixel);
}

int main(int argc, char **argv)
{
    int framebufferDevice = 0;

    /* Ze zarizeni potrebujeme pouze cist. */
    framebufferDevice = open("/dev/fb0", O_RDONLY);

    /* Pokud otevreni probehlo uspesne, nacteme
     * a nasledne vypiseme informaci o framebufferu.*/
    if (framebufferDevice != -1) {
        printFramebufferInfo(framebufferDevice);
        close(framebufferDevice);
        return 0;
    }
    /* Otevreni se nezadarilo, vypiseme chybove hlaseni. */
    else {
        perror("Nelze otevrit ovladac /dev/fb0");
        return 1;
    }
}
