// Morfing mezi Julia a Mandelbrot fraktalem dle hodnoty "uhlu"

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <go32.h>
#include <time.h>
#include <sys/farptr.h>
#include <sys/segments.h>

#include <allegro.h>

PALLETE pal;

void mand_jul(float uhel,float ccx,float ccy)
{
    float   zx,zy,zx2,zy2,cx,cy;
    float   cosu,sinu,ccxc,ccyc;
    int     x,y,i;

    uhel=uhel*3.1415/180.0;
    cosu=cos(uhel);
    sinu=sin(uhel);
    ccxc=ccx*cosu;
    ccyc=ccy*cosu;

    cy=-2.0;
    cx=-2.0;
    for (y=0;y<200;y++) {
        cx=-2.0;
        for (x=0;x<240;x++) {
            i=0;
            zx=cx*cosu;
            zy=cy*cosu;
            do {
                zx2=zx*zx;
                zy2=zy*zy;
                zy=2.0*zx*zy+ccyc+cy*sinu;
                zx=zx2-zy2+ccxc+cx*sinu;
                i++;
            } while (i<64 && zx2+zy2<4.0);
            putpixel(screen,x,y,i);
            cx=cx+4.0/240.0;
        }
        cy=cy+4.0/200.0;
    }
}

int main(int argc, char *argv[])
{
   int i;
   float f;
   char fname[100];

   allegro_init();
   install_keyboard();
   set_gfx_mode(GFX_VGA, 320, 200, 0, 0);
   for (i=0; i<64; i++) {
       pal[i].r=i*4;
       pal[i].g=i*2;
       pal[i].b=i;
   }
   set_palette(pal);

   i=0;
   for (f=0; f<360; f+=1.0) {
       mand_jul(f,0.0,1.0);
       sprintf(fname,"%03d",i);
       save_pcx(fname,screen,pal);
       i++;
   }

   set_gfx_mode(GFX_TEXT,80,25,0,0);
   return 0;
}
