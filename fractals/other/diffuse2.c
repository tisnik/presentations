#include <stdio.h>
#include <stdlib.h>
#include <allegro.h>

#define ITER 100
#define BOX 5

int okoli(int x,int y)
{
    int i=0;
    i=getpixel(screen,x-1,y-1)+
      getpixel(screen,x-1,y)+
      getpixel(screen,x-1,y+1)+
      getpixel(screen,x  ,y-1)+
      getpixel(screen,x  ,y+1)+
      getpixel(screen,x+1,y-1)+
      getpixel(screen,x+1,y)+
      getpixel(screen,x+1,y+1);
    return(i);
}

void main(void)
{
    int xb,yb;
    int x,y,i,d;
    int pts=0;

    allegro_init();
    install_keyboard();
    set_gfx_mode(GFX_VGA,320,200,0,0);

    line(screen,0,199,319,199,15);
    putpixel(screen,160,198,15);
    for (yb=188;yb>100;yb--) {
        i=1;
        for (d=0;d<20;d++)
        do {
            xb=random()%300+5;
            for (i=0;i<100;i++) {
                x=random()%10;
                y=random()%10;
                if (okoli(x+xb,y+yb)) {
                    putpixel(screen,x+xb,y+yb,15);
                    i=0;
                    break;
                }
            }
        } while (i);
    }

    readkey();
    remove_keyboard();
    allegro_exit();
}

