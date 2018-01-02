#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <go32.h>
#include <sys/farptr.h>
#include <sys/segments.h>

#include "allegro.h"

PALLETE pal;

//            _putpixel(screen,i2,i1,color);

int main(int argc, char *argv[])
{
   float zx,zy,zx2,zy2,cx,cy;
   int x,y,i;
   int podm;
   allegro_init();
   install_keyboard(); 
   set_gfx_mode(GFX_VESA1, 640, 480, 0, 0);
   for (y=0;y<200;y++) {
     cy=(y/50.0)-2;
     for (x=0;x<200;x++) {
       cx=(x/50.0)-2;
       i=50;
       zx=0;zy=0;
       do {
         zx2=zx*zx;
         zy2=zy*zy;
         zy=2.0*zx*zy+cy;
         zx=zx2-zy2+cx;
         i--;
         podm=zx2+zy2<4.0;
       } while (i>0 && podm);
       if (i!=48 && !podm)
         putpixel(screen,x,y,7);
     }
   }
   readkey();
   return 0;
}

