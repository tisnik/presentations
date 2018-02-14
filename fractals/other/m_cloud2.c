#include <allegro.h>
#include <math.h>

void mandel_cloud(double xmin, double ymin, double xmax, double ymax,
    double maxiter, double x_start, double y_start)
{
  int x,y;                            /* pro pozici na obrazovce */
  int iter;                           /* pocitadlo iteraci */
  int hranice=10;
  double xpos,ypos;                   /* pozice v mnozine */
  double zx1,zy1,zx2,zy2;             /* pro pocitani z^2+c */
  double cx,cy;                               /* -//- */
  double xd,yd;                               /* prirustex x a y */
  int x_,y_;
  xpos=xmin;                          /* pocatecni nastaveni */
  ypos=ymin;
  xd=(xmax-xmin)/30.0;                        /* vypocet prirustku */
  yd=(ymax-ymin)/30.0;
  for (y=0; y<30; y++)
  {
    ypos+=yd;                               /* dalsi radek */
    xpos=xmin;
    for (x=0; x<30; x++)
    {
      xpos+=xd;                           /* dalsi pixel */
      zx1=x_start;                        /* pro pocatecni iteraci */
      zy1=y_start;
      cx=xpos;                            /* pocatecni pozice v mnozine */
      cy=ypos;
      for (iter=0;iter<maxiter;iter++)    /* iterace */
      {
        zx2=zx1*zx1;
        zy2=zy1*zy1;
        if ((zx2+zy2)>4)break;                  /* test na bailout */
        zy1=2*zx1*zy1+cx;
        zx1=zx2-zy2+cy;                             /* z=z^2+c */
        if (iter>hranice)
        {
          x_=320.0+zx1*150.0;
          y_=240.0+zy1*150.0;

          putpixel(screen,x_,y_,x+y+31);              /* vystup */
        }
      }
    }
  }
}

void mandel_cloud2(double xmin, double ymin, double xmax, double ymax,
    double maxiter, double x_start, double y_start)
{
  int x,y;                            /* pro pozici na obrazovce */
  int iter;                           /* pocitadlo iteraci */
  int hranice=10;
  double xpos,ypos;                   /* pozice v mnozine */
  double zx1,zy1,zx2,zy2;             /* pro pocitani z^2+c */
  double cx,cy;                               /* -//- */
  double xd,yd;                               /* prirustex x a y */
  int x_,y_;
  int kreslit;

  xpos=xmin;                          /* pocatecni nastaveni */
  ypos=ymin;
  xd=(xmax-xmin)/30.0;                        /* vypocet prirustku */
  yd=(ymax-ymin)/30.0;
  for (y=0; y<30; y++)
  {
    ypos+=yd;                               /* dalsi radek */
    xpos=xmin;
    for (x=0; x<30; x++)
    {
      xpos+=xd;                           /* dalsi pixel */
      zx1=x_start;                        /* pro pocatecni iteraci */
      zy1=y_start;
      cx=xpos;                            /* pocatecni pozice v mnozine */
      cy=ypos;
      kreslit=1;
      for (iter=0;iter<maxiter;iter++) {
        zx2=zx1*zx1;zy2=zy1*zy1;
        if ((zx2+zy2)>4) {
          kreslit=0;
          break;
        }
        zy1=2*zx1*zy1+cx;
        zx1=zx2-zy2+cy;
      }
      zx1=x_start;                        /* pro pocatecni iteraci */
      zy1=y_start;
      if (kreslit)
        for (iter=0;iter<maxiter;iter++)    /* iterace */
        {
          zx2=zx1*zx1;
          zy2=zy1*zy1;
          if ((zx2+zy2)>4)break;                  /* test na bailout */
          zy1=2*zx1*zy1+cx;
          zx1=zx2-zy2+cy;                             /* z=z^2+c */
          if (iter>hranice)
          {
            x_=320.0+zx1*180.0;
            y_=240.0+zy1*180.0;

            putpixel(screen,x_,y_,x+y+31);              /* vystup */
          }
        }
    }
  }
}

void main(void)
{
  float a;
  allegro_init();
  set_gfx_mode(GFX_VESA1,640,480,640,480);
  install_keyboard();
  clear_keybuf();
  mandel_cloud(-1.63,-1.033,1.04,0.99,200, 0,0);
  readkey();
  for (a=0.0;a<1.0;a+=0.1) {
    clear(screen);
    mandel_cloud2(-1.63,-1.033,1.04,0.99,200,a,a);
    readkey();
  }
}
