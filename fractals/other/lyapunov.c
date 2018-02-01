#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <allegro.h>
#include <values.h>

#define ITER 100

void main(void)
{
    int x,y,i;
    double startx,starty;
    double z,r;
    double total;

    allegro_init();
    install_keyboard();
    set_gfx_mode(GFX_VGA,320,200,0,0);

    startx=-5;
    starty=-5;
    for (y=0;y<200;y++) {
        startx=-5;
        for (x=0;x<320;x++) {
            startx+=10.0/320.0;
            z=0.5;
            total=0.0;
            for (i=0;i<100;i++) {
//                printf("> %d\t%f\t%f\t%f\n",i%4,z,startx,starty);
                switch (i%4) {
                    case 0:
                        z=(starty*z)*(1.0-z);
                        r=starty;
                        break;
                    case 1:
                        z=(startx*z)*(1.0-z);
                        r=startx;
                        break;
                    case 2:
                        z=(startx*z)*(1.0-sin(z));
                        r=startx;
                        break;
                    case 3:
                        z=(starty*z)*(1.0-cos(z*z));
                        r=starty;
                        break;
                    default:
                        z=z;
                        r=0;
                }
                if (z>500) i=100;
//                printf("< %d\t%f\n\n",i%4,z);

                if (fabs(r-2.0*r*z)>0)
                    total+=log(fabs(r-2.0*r*z))/log(2);
            }
            total=total/30;
            if (total<0) {
                putpixel(screen,x,y,-total);
            }
        }
        starty+=10.0/200.0;
    }


    readkey();
    remove_keyboard();
    allegro_exit();
}

