// porovnani rychlosti vypoctu Mandelbrotovy mnoziny pri ruznem ciselnem
// zakladu (float, double, long double, fixed)

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <go32.h>
#include <time.h>
#include <sys/farptr.h>
#include <sys/segments.h>

#include "allegro.h"

int c1,c2,c3,c4,d,o;

PALLETE pal;
void cclear(void)
{
    int     x,y;

    for (y=0;y<200;y++)
        for (x=0;x<240;x++)
            putpixel(screen,x,y,0);

}

void mandel_float(void)
{
    float   zx,zy,zx2,zy2,cx,cy;
    int     x,y,i;

    cy=-2.0;
    cx=-2.0;
    for (y=0;y<200;y++) {
        cx=-2.0;
        for (x=0;x<240;x++) {
            i=0;
            zx=0;zy=0;
            do {
                zx2=zx*zx;
                zy2=zy*zy;
                zy=2.0*zx*zy+cy;
                zx=zx2-zy2+cx;
                i++;
            } while (i<64 && zx2+zy2<4.0);
            putpixel(screen,x,y,i+o);
            cx=cx+4.0/240.0;
        }
        cy=cy+4.0/200.0;
    }
}

void mandel_double(void)
{
    double  zx,zy,zx2,zy2,cx,cy;
    int     x,y,i;

    cy=-2.0;
    cx=-2.0;
    for (y=0;y<200;y++) {
        cx=-2.0;
        for (x=0;x<240;x++) {
            i=0;
            zx=0;zy=0;
            do {
                zx2=zx*zx;
                zy2=zy*zy;
                zy=2.0*zx*zy+cy;
                zx=zx2-zy2+cx;
                i++;
            } while (i<64 && zx2+zy2<4.0);
            putpixel(screen,x,y,i+o);
            cx=cx+4.0/240.0;
        }
        cy=cy+4.0/200.0;
    }
}

void mandel_ddouble(void)
{
    long double  zx,zy,zx2,zy2,cx,cy;
    int     x,y,i;

    cy=-2.0;
    cx=-2.0;
    for (y=0;y<200;y++) {
        cx=-2.0;
        for (x=0;x<240;x++) {
            i=0;
            zx=0;zy=0;
            do {
                zx2=zx*zx;
                zy2=zy*zy;
                zy=2.0*zx*zy+cy;
                zx=zx2-zy2+cx;
                i++;
            } while (i<64 && zx2+zy2<4.0);
            putpixel(screen,x,y,i+o);
            cx=cx+4.0/240.0;
        }
        cy=cy+4.0/200.0;
    }
}

void mandel_fix2(int x0,int y0,float scale)
{
    fixed  zx,zy,zx2,zy2,cx,cy;
    int    x,y,i;

    fixed  kcx,kcy,kkx,kky;
    fixed  thr;

    thr=ftofix(4.0);
    kcx=ftofix(-2.0/scale+x0);
    kcy=ftofix(-2.0/scale+y0);
    kkx=ftofix(4.0/240.0/scale);
    kky=ftofix(4.0/200.0/scale);

    cy=kcy;
    cx=kcx;
    for (y=0;y<200;y++) {
        cx=kcx;
        for (x=0;x<240;x++) {
            i=0;
            zx=0;zy=0;
            do {
                zx2=fmul(zx,zx);
                zy2=fmul(zy,zy);
                zy=2*fmul(zx,zy)+cy;
                zx=zx2-zy2+cx;
                i++;
            } while (i<64 && zx2+zy2<thr);
            putpixel(screen,x,y,i+o);
            cx+=kkx;
        }
        cy+=kky;
    }
}

void mandel_fix(void)
{
    fixed  zx,zy,zx2,zy2,cx,cy;
    int    x,y,i;

    fixed  k1,k2,k3,k4;

    k1=ftofix(-2.0);
    k2=ftofix(4.0);
    k3=ftofix(4.0/240.0);
    k4=ftofix(4.0/200.0);

    cy=k1;
    cx=k1;
    for (y=0;y<200;y++) {
        cx=k1;
        for (x=0;x<240;x++) {
            i=0;
            zx=0;zy=0;
            do {
                zx2=fmul(zx,zx);
                zy2=fmul(zy,zy);
                zy=2*fmul(zx,zy)+cy;
                zx=zx2-zy2+cx;
                i++;
            } while (i<64 && zx2+zy2<k2);
            putpixel(screen,x,y,i+o);
            cx+=k3;
        }
        cy+=k4;
    }
}

int main(int argc, char *argv[])
{
   int i;float f;
   allegro_init();
   install_keyboard();
   set_gfx_mode(GFX_VGA, 320, 200, 0, 0);
   d=clock();for (o=0;o<100;o++)mandel_float();   c1=clock()-d; cclear();
   d=clock();for (o=0;o<100;o++)mandel_double();  c2=clock()-d; cclear();
   d=clock();for (o=0;o<100;o++)mandel_ddouble(); c3=clock()-d; cclear();
   d=clock();for (o=0;o<100;o++)mandel_fix();     c4=clock()-d; cclear();
   set_gfx_mode(GFX_TEXT,80,25,0,0);
   printf("Float:        %d\n",c1);
   printf("Double:       %d\n",c2);
   printf("Long double:  %d\n",c3);
   printf("Fix point     %d\n",c4);
   return 0;
}
