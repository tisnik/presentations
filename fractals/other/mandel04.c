// Vypocet Mandelbrotovy mnoziny a vystup do DXF souboru

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MAXITER    200
#define MRIZKA     100
#define PER_CHECK  0.0001
#define PER_PERIOD 16

double ldabs (double x)
{
    return (x<0) ? -x : x;
}

int mtest(double ccx,double ccy)
{
    double  zx,zy,zx2,zy2,zzx,zzy,zzx2,zzy2;
    int     i;
    int     result1,result2;
    int     period=0;
    double  dst;

    result1=0;
    result2=0;
    i=0;
    zx=0; zy=0;
    zzx=0;zzy=0;
    do {
        if (period==PER_PERIOD) {
          zzx2=zzx*zzx;
          zzy2=zzy*zzy;
          zzy=2.0*zzx*zzy+ccy;
          zzx=zzx2-zzy2+ccx;
          period=0;
        }
        zx2=zx*zx;
        zy2=zy*zy;
        zy=2.0*zx*zy+ccy;
        zx=zx2-zy2+ccx;
        i++;
        period++;
        dst=ldabs(zx-zzx)+ldabs(zy-zzy);
        if (dst<PER_CHECK) {
          i=MAXITER;
          result2=1;
        }
    } while (i<MAXITER && zx2+zy2<4.0);

    if (i==MAXITER) {
      if (result2) result1=10;
      else         result1=15;
    }
    else {
      if (result2) result1=9;
      else         result1=12;
    }

    return (result1);
}

void mandel(void)
{
    double  zx,zy,zx2,zy2,cx,cy;
    int     x,y,i;
    int     color;
    int     pocet=0;

    cy=-2.0;
    cx=-2.0;
    for (y=0;y<MRIZKA;y++) {
        cx=-2.0;
        for (x=0;x<MRIZKA;x++) {
            i=0;
            zx=0;zy=0;
              color=mtest(cx,cy);
              if (color==15) {
               do {
                   zx2=zx*zx;
                   zy2=zy*zy;
                   zy=2.0*zx*zy+cy;
                   zx=zx2-zy2+cx;
                   i++;
                   pocet++;
                   if (i>5)
                     printf(
"  0\n"
"POINT\n"
"  8\n"
"0\n"
" 10\n"
"%10.8lf\n"
" 20\n"
"%10.8lf\n"
" 30\n"
"0.0\n",zx,zy);
               } while (i<MAXITER && zx2+zy2<4.0);
              }
            cx=cx+4.0/MRIZKA;
        }
        cy=cy+4.0/MRIZKA;
    }
}

int main(int argc, char *argv[])
{
   mandel();
   return 0;
}


