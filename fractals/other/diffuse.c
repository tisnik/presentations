#include <stdio.h>
#include <stdlib.h>
#include <allegro.h>
#include <math.h>

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
    float xb,yb;
    int x,y,i,j,d=0;
    int pts=0;
    float alfa;

    allegro_init();
    install_keyboard();
    set_gfx_mode(GFX_VESA1,800,600,0,0);

    putpixel(screen,400,300,15);
    for (d=0;d<300;d++) {
        j=0;
        while (j<100) {
            alfa=random();
            xb=400.0+d*cos(alfa)-7.0;
            yb=300.0+d*sin(alfa)-7.0;
            for (i=0;i<200;i++) {
                x=random()%14;
                y=random()%14;
                if (okoli(x+xb,y+yb)) {
                    putpixel(screen,x+xb,y+yb,/*(d/10)%8+9*/15);
                    j++;
                    break;
                }
            }
        }
    }
    readkey();
    remove_keyboard();
    allegro_exit();
}

