#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <allegro.h>

#define MAXITER 10

void mandel4(double parcz,double parcw)
{
    double  zx, zy, zz, zw;
    double  zx1,zy1,zz1,zw1;
    double  zx2,zy2,zz2,zw2;
    double  cx ,cy ,cz=parcz, cw=parcw;
    int     x,y,i;

    cx=-2.0;
    cy=-1.5;
//    cz=parcz;
//    cw=parcw;

    for (y=0;y<200;y++) {
        cx=-2.0;
        for (x=0;x<320;x++) {
            i=0;
            zx=0.0;zy=0.0;zz=0.0;zw=0.0;
            do {
               zx2=zx*zx;
               zy2=zy*zy;
               zz2=zz*zz;
               zw2=zw*zw;

               zx1=zx2-zy2-zz2-zw2;
               zy1=2.0*zx*zy;
               zz1=2.0*zx*zz;
               zw2=2.0*zx*zw;

               zx=zx1+cx;
               zy=zy1+cy;
               zz=zz1+cz;
               zw=zw1+cw;

               i++;
            } while ((i<MAXITER) && (zx2+zy2+zz2+zw2)<4.0);
            _putpixel(screen,x,y,i);
            cx+=4.0/320.0;
        }
        cy+=3.0/200.0;
    }
}

void params(double parcz,double parcw)
{
  char str[80];

  sprintf(str,"%6.3f   %6.3f",parcz,parcw);
  textout(screen,font,str,0,0,15);
}

int main(void)
{
   int key;
   double pcz=0.0;
   double pcw=0.0;


   allegro_init();
   install_keyboard();
   set_gfx_mode(GFX_VGA,320,200,0,0);
   text_mode(0);

   mandel4(pcz,pcw);
   params(pcz,pcw);

   do {
      key=readkey() & 0xff;
      if (key==']') {pcz+=0.1; params(pcz,pcw);}
      if (key=='[') {pcz-=0.1; params(pcz,pcw);}
      if (key==',') {pcw-=0.1; params(pcz,pcw);}
      if (key=='.') {pcw+=0.1; params(pcz,pcw);}
      if (key==' ') {
          mandel4(pcz,pcw);
          params(pcz,pcw);
      }
   } while (key!=27);

   remove_keyboard();
   return 0;
}

END_OF_MAIN();
