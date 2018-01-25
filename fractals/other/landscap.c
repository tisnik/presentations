#include    <math.h>
#include    <stdlib.h>
#include    <stdio.h>
#include    <allegro.h>

//////////////////////////////////////////////////////////////
// Definice datovych typu
//////////////////////////////////////////////////////////////
typedef unsigned char byte;
typedef unsigned int  word;
typedef struct {
  float     xmin;                       // rozmer M-setu
  float     xmax;
  float     ymin;
  float     ymax;
  float     cx0;                        // pocatecni podminky pro vypocet
  float     cy0;                        // fraktalu
  float     slope;
}           t_fraktal;

//////////////////////////////////////////////////////////////
// Definice promennych
//////////////////////////////////////////////////////////////
int         it=255;                     // pocet iteraci
float       xx1=-9,xx2=-9,yy1=-9,yy2=-9;
PALLETE     pallete;                    // barevna paleta
byte        aiter[256][256];
float       amag [256][256];
t_fraktal   fraktal={                   // pocatecni hodnoty pro fraktal
            -2.0, 1.5,-1.5, 1.5,0,0,500};
t_fraktal   old_fraktal={               // predchozi fraktal
            -2.0, 1.5,-1.5, 1.5,-9,-9,500};
t_fraktal   fraktaly[]={                // dalsi zajimave fraktaly
//  {xmin}        {xmax}        {ymin}            {ymax}           {cx0}   {cy0}    {slope}
  {-4.0000000000, 2.0000000000,-2.0000000000000, 2.0000000000000, 0.0000, 0.0000,    500},
  {-0.6874310480,-0.6674249520,-0.4379062860000,-0.4229017140000, 0.0000, 0.0000,  20000},
  { 0.4586363643, 0.4686363630, 0.3882097995000, 0.3957097985000, 0.0000, 0.0000,   5000},
  {-0.1166244700, 0.0689754750, 0.9106760200000, 1.0498760000000, 0.0000, 0.0000,   1100},
  {-0.6336530010,-0.5920529990, 0.6627919990000, 0.6939920010000, 0.0000, 0.0000,   5000},
  {-1.4368174608,-1.4359574608, 0.0033076507336, 0.0039526507739, 0.0000, 0.0000,1000000},
  {-0.7201258938,-0.7108458931, 0.3337184922000, 0.3406784927000, 0.0000, 0.0000, 100000},
  { 0.3829519690, 0.4101520310, 0.5533478740000, 0.5757981260000, 0.0000, 0.0000,   3000},
  { 0.0615186996, 0.1133427000, 0.6137320000000, 0.6526000000000, 0.0000, 0.0000,  20000},
  { 0.2482900300, 0.4482877800, 0.6192228200000, 0.7692211300000,-0.0700,-0.0700,   2000},
  { 0.7847811740, 0.7057155740,-0.9030032000000,-0.7975824000000, 0.0000,-0.5000,   1500},
  {-0.7083810300,-0.5385506300,-0.8383919300000,-0.7110191300000, 0.0000, 0.1300,   2000},
  {-0.4597190900,-0.3478044200, 0.9719013470000, 1.0558373500000, 0.2000, 0.0000,   1000},
  {-1.9896928000,-1.7603595000,-0.2882110600000,-0.1162110600000, 0.0000, 0.1000,    800}
};

int potential(int iterations,float mag,float slope)
{
  float     pot;
  int       i_pot;

  if(iterations<255) {                  // neni prekrocen maximalni pocet iteraci
    pot=iterations+1;                   // uprava na pocitani dle FractIntu
    if(pot<=0 || mag<=1.0)              // pro spravne logaritmovani
      pot = 0.0;
    else {                              // pot=log(mag)/2^iter
      pot=log(mag)/pow(2.0,(float)pot);
      pot=(float)sqrt((float)pot);      // pot=sqrt(pot)
      pot=255-pot*slope-1.0;            // uprava vysky
      if(pot<1.0) pot=1.0;              // zabranit podteceni
    }
  }
  else                                  // je prekrocen maximalni pocet iteraci
    pot=255;                            // dosadit maximalni hodnotu
  i_pot=pot;                            // prevod na int
  if(i_pot>=255) i_pot=255;             // zajistit jen dany pocet barev
  return(i_pot);
}

void calcfrac(t_fraktal f)              // vypocet Mandelbrotovy mnoziny
{
  int       x,y,iter,vyska;
  float     xpos=f.xmin,ypos=f.ymin;    // pocatecni hodnoty (levy horni roh)
  float     xd=(f.xmax-f.xmin)/256.0;   // krok v ose x
  float     yd=(f.ymax-f.ymin)/256.0;   // krok v ose y
  float     zx1,zy1,zx2,zy2,cx,cy;

  show_mouse(NULL);
  for (y=0; y<256; y++) {               // pres vsechny radky
    ypos+=yd;                           // dalsi bod v mnozine
    xpos=f.xmin;                        // zacatek prvniho bodu v radku
    for (x=0; x<256; x++) {             // pres vsechny sloupce
      xpos+=xd;                         // dalsi bod v mnozine
      zx1=f.cx0;zy1=f.cy0;              // pocatecni podminky
      cx=xpos;cy=ypos;
      vyska=255;
      for (iter=0;iter<it;iter++) {     // blok iteraci
        zx2=zx1*zx1;zy2=zy1*zy1;        // kvadraty souradnic
        if ((zx2+zy2)>4) break;         // kontrola bailout
        zy1=2*zx1*zy1+cy;               // vypocet z=z^2+c
        zx1=zx2-zy2+cx;
      }
      aiter[x][y]=iter;                 // zaznamenat pocet iteraci
      amag [x][y]=zx2+zy2;              // zaznamenat vzdalenost bodu od 0
      vyska=potential(iter,zx2+zy2,f.slope);
      putpixel(screen,x,y,vyska);       // vykreslit vysledek na obrazovku
    }
  }
  show_mouse(screen);
}

void get_coords(float*a,float*b)
{
  float     x,y;
//  show_mouse(NULL);
//  textout(screen,font,"Zadej souradnice na fraktalu:",400,460,15);
//  show_mouse(screen);
  while (!mouse_b);                     // cekani na stlaceni tlacitka mysi
  do {
    x=mouse_x;
    y=mouse_y;
  } while (mouse_b);                    // cekani na pusteni tlacitka mysi
  *a=x*(old_fraktal.xmax-old_fraktal.xmin)/256+old_fraktal.xmin;
  *b=y*(old_fraktal.ymax-old_fraktal.ymin)/256+old_fraktal.ymin;
}

void redraw_val(void)                   // prekresleni hodnot promennych
{
  char      pom[20];
  float     x_origin=old_fraktal.xmin;
  float     y_origin=old_fraktal.ymin;
  float     x_mag=256.0/(old_fraktal.xmax-old_fraktal.xmin);
  float     y_mag=256.0/(old_fraktal.ymax-old_fraktal.ymin);
  show_mouse(NULL);                     // skryt kurzor mysi
  putpixel(screen,639,0,0);
  sprintf(pom,"%+1.5f",fraktal.cx0);    textout(screen,font,pom,560,15,7);
  sprintf(pom,"%+1.5f",fraktal.cy0);    textout(screen,font,pom,560,40,7);
  sprintf(pom,"%+1.5f",fraktal.xmin);   textout(screen,font,pom,560,65,7);
  sprintf(pom,"%+1.5f",fraktal.ymin);   textout(screen,font,pom,560,90,7);
  sprintf(pom,"%+1.5f",fraktal.xmax);   textout(screen,font,pom,560,115,7);
  sprintf(pom,"%+1.5f",fraktal.ymax);   textout(screen,font,pom,560,140,7);
  sprintf(pom,"%+5.0f",fraktal.slope);  textout(screen,font,pom,560,165,7);
  sprintf(pom,"%5d",it);                textout(screen,font,pom,560,190,7);
  xor_mode(TRUE);
  circle(screen,x_mag*(old_fraktal.cx0-x_origin),
                y_mag*(old_fraktal.cy0-y_origin),6,15);
  old_fraktal.cx0=fraktal.cx0;          old_fraktal.cy0=fraktal.cy0;
  circle(screen,x_mag*(old_fraktal.cx0-x_origin),
                y_mag*(old_fraktal.cy0-y_origin),6,15);
  rect(screen,  x_mag*(xx1-x_origin),y_mag*(yy1-y_origin),
                x_mag*(xx2-x_origin),y_mag*(yy2-y_origin),15);
  xx1=fraktal.xmin;                     xx2=fraktal.xmax;
  yy1=fraktal.ymin;                     yy2=fraktal.ymax;
  rect(screen,  x_mag*(xx1-x_origin),y_mag*(yy1-y_origin),
                x_mag*(xx2-x_origin),y_mag*(yy2-y_origin),15);
  xor_mode(FALSE);
  solid_mode();
  show_mouse(screen);                   // zapnout kurzor mysi
}

void redraw_slope(void)                 // prekresleni slope-krivky
{
  int       x;
  float     vyska;

  show_mouse(NULL);
  rectfill(screen,0,300,256,479,0);
  for (x=0;x<256;x++) {
    vyska=potential(aiter[x][x],amag[x][x],fraktal.slope);
    putpixel(screen,x,470-vyska/1.5,15);
  }
  show_mouse(screen);
}

int d_cxmm(int msg,DIALOG * d,int c)    // cx <<-
{ int       ret=d_button_proc(msg,d,c);
  if (msg==MSG_START || msg==MSG_DRAW) {
    redraw_val();
    redraw_slope();
  }
  if (ret==D_CLOSE) { fraktal.cx0-=0.1;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cxm(int msg,DIALOG * d,int c)     // cx <-
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cx0-=0.01;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cxpp(int msg,DIALOG * d,int c)    // cx <<-
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cx0+=0.1;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cxp (int msg,DIALOG * d,int c)    // cx <<-
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cx0+=0.01;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cymm(int msg,DIALOG * d,int c)    // cx <<-
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cy0-=0.1;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cym(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cy0-=0.01;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cypp(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cy0+=0.1;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_cyp (int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.cy0+=0.01;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x1mm(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmin-=0.1*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x1m(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmin-=0.01*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x1pp(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmin+=0.1*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x1p (int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmin+=0.01*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y1mm(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymin-=0.1*fabs(fraktal.ymax-fraktal.ymin);;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y1m(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymin-=0.01*fabs(fraktal.ymax-fraktal.ymin);;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y1pp(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymin+=0.1*fabs(fraktal.ymax-fraktal.ymin);;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y1p (int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymin+=0.01*fabs(fraktal.ymax-fraktal.ymin);;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x2mm(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmax-=0.1*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x2m(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmax-=0.01*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x2pp(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmax+=0.1*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_x2p (int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.xmax+=0.01*fabs(fraktal.xmax-fraktal.xmin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y2mm(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymax-=0.1*fabs(fraktal.ymax-fraktal.ymin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y2m(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymax-=0.01*fabs(fraktal.ymax-fraktal.ymin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y2pp(int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymax+=0.1*fabs(fraktal.ymax-fraktal.ymin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_y2p (int msg,DIALOG * d,int c)
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.ymax+=0.01*fabs(fraktal.ymax-fraktal.ymin);
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_itmm(int msg,DIALOG * d,int c)    // it--
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { it-=10;
                      if (it<0) it=0;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_itm(int msg,DIALOG * d,int c)     // it-
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { it--;
                      if (it<0) it=0;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_itpp(int msg,DIALOG * d,int c)    // it++
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { it+=10;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_itp (int msg,DIALOG * d,int c)    // it+
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { it++;
                      redraw_val();
                      return D_O_K;}
  return ret;
}
int d_slopemm(int msg,DIALOG * d,int c) // slope--
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.slope-=500;
                      if (fraktal.slope<0) fraktal.slope=0;
                      redraw_val();
                      redraw_slope();
                      return D_O_K;}
  return ret;
}
int d_slopem(int msg,DIALOG * d,int c)  // slope-
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.slope-=10;
                      if (fraktal.slope<0) fraktal.slope=0;
                      redraw_val();
                      redraw_slope();
                      return D_O_K;}
  return ret;
}
int d_slopepp(int msg,DIALOG * d,int c) // slope++
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.slope+=500;
                      redraw_val();
                      redraw_slope();
                      return D_O_K;}
  return ret;
}
int d_slopep (int msg,DIALOG * d,int c) // slope+
{ int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) { fraktal.slope+=10;
                      redraw_val();
                      redraw_slope();
                      return D_O_K;}
  return ret;
}

int d_redraw (int msg,DIALOG * d,int c)
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    calcfrac(fraktal);
    old_fraktal=fraktal;
    redraw_val();
    redraw_slope();
    return D_O_K;
  }
  return ret;
}

int d_3d(int msg,DIALOG * d,int c)      // zobrazeni 3d-krajiny
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    int     x,y;
    float   vyska,old_vyska;
    show_mouse(NULL);
    rectfill(screen,257,242,639,479,0);
    for (y=0;y<256;y++)
      for (x=0;x<256;x++) {
        vyska=potential(aiter[x][y],amag[x][y],fraktal.slope);
        vyska=(x+y-vyska)/4;
        vline(screen,57+420+(x-y)/2,300+vyska,300+vyska+5,(old_vyska-vyska)*7+64);
        old_vyska=vyska;
      }
    show_mouse(screen);
    redraw_val();
    return D_O_K;
  }
  return ret;
}

int d_write  (int msg,DIALOG * d,int c) // zapis vysledku do stdout
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    fprintf(stdout,"{ %f, %f, %f, %f, %f, %f, %f },\n",fraktal.xmin,
                                                       fraktal.xmax,
                                                       fraktal.ymin,
                                                       fraktal.ymax,
                                                       fraktal.cx0,
                                                       fraktal.cy0,
                                                       fraktal.slope);
    return D_O_K;
  }
  return ret;
}

int d_reset  (int msg,DIALOG * d,int c) // reset hodnot
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    fraktal.xmin=-2;
    fraktal.xmax=1.5;
    fraktal.ymin=-1.5;
    fraktal.ymax=1.5;
    fraktal.cx0 =0;
    fraktal.cy0 =0;
    fraktal.slope=500;
    redraw_val();
    return D_O_K;
  }
  return ret;
}

int d_select_c (int msg,DIALOG * d,int c)
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    float a,b;
    get_coords(&a,&b);                  // vezmi souradnice "z mysi"
    fraktal.cx0=a;                      // dosad souradnice
    fraktal.cy0=b;
    redraw_val();
    redraw_slope();
    return D_O_K;
  }
  return ret;
}
int d_select_x1y1 (int msg,DIALOG * d,int c)
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    float a,b;
    get_coords(&a,&b);                  // vezmi souradnice "z mysi"
    fraktal.xmin=a;                     // dosad souradnice
    fraktal.ymin=b;
    redraw_val();
    redraw_slope();
    return D_O_K;
  }
  return ret;
}
int d_select_x2y2 (int msg,DIALOG * d,int c)
{
  int       ret=d_button_proc(msg,d,c);
  if (ret==D_CLOSE) {
    float a,b;
    get_coords(&a,&b);                  // vezmi souradnice "z mysi"
    fraktal.xmax=a;                     // dosad souradnice
    fraktal.ymax=b;
    redraw_val();
    redraw_slope();
    return D_O_K;
  }
  return ret;
}

DIALOG main_dialog[] =                  // hlavni dialog
{
/* (dialog proc)     (x) (y) (w) (h)(f/b)(key) (flags)(d1)(d2)(dp) */
  {d_shadow_box_proc,275,  0,364,240,0,7,    0,      0, 0,  0,NULL     },
  {d_cxmm,           280, 10, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cx <--" },
  {d_cxm,            335, 10, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cx <-"  },
  {d_cxp,            390, 10, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cx ->"  },
  {d_cxpp,           445, 10, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cx -->" },

  {d_select_c,       500, 10, 30, 45,15,4,   0,D_CLOSE, 0,  0,"*"      },

  {d_cypp,           280, 35, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cy <--" },
  {d_cyp,            335, 35, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cy <-"  },
  {d_cym,            390, 35, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cy ->"  },
  {d_cymm,           445, 35, 50, 20,0,8,    0,D_CLOSE, 0,  0,"cy -->" },

  {d_x1mm,           280, 60, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x1 <--" },
  {d_x1m,            335, 60, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x1 <-"  },
  {d_x1p,            390, 60, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x1 ->"  },
  {d_x1pp,           445, 60, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x1 -->" },

  {d_select_x1y1,    500, 60, 30, 45,15,4,   0,D_CLOSE, 0,  0,"*"      },
  {d_y1pp,           280, 85, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y1 <--" },
  {d_y1p,            335, 85, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y1 <-"  },
  {d_y1m,            390, 85, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y1 ->"  },
  {d_y1mm,           445, 85, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y1 -->" },

  {d_x2mm,           280,110, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x2 <--" },
  {d_x2m,            335,110, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x2 <-"  },
  {d_x2p,            390,110, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x2 ->"  },
  {d_x2pp,           445,110, 50, 20,0,8,    0,D_CLOSE, 0,  0,"x2 -->" },

  {d_select_x2y2,    500,110, 30, 45,15,4,   0,D_CLOSE, 0,  0,"*"      },

  {d_y2pp,           280,135, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y2 <--" },
  {d_y2p,            335,135, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y2 <-"  },
  {d_y2m,            390,135, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y2 ->"  },
  {d_y2mm,           445,135, 50, 20,0,8,    0,D_CLOSE, 0,  0,"y2 -->" },

  {d_slopepp,        280,160, 60, 20,0,8,    0,D_CLOSE, 0,  0,"slope--"},
  {d_slopep,         345,160, 60, 20,0,8,    0,D_CLOSE, 0,  0,"slope-" },
  {d_slopem,         410,160, 60, 20,0,8,    0,D_CLOSE, 0,  0,"slope+" },
  {d_slopemm,        475,160, 60, 20,0,8,    0,D_CLOSE, 0,  0,"slope++"},
  {d_itpp,           280,185, 60, 20,0,8,    0,D_CLOSE, 0,  0,"it <<-" },
  {d_itp,            345,185, 60, 20,0,8,    0,D_CLOSE, 0,  0,"it <-"  },
  {d_itm,            410,185, 60, 20,0,8,    0,D_CLOSE, 0,  0,"it ->"  },
  {d_itmm,           475,185, 60, 20,0,8,    0,D_CLOSE, 0,  0,"it ->>" },
  {d_redraw,         280,210, 60, 20,15,2,   0,D_CLOSE, 0,  0,"Redraw" },
  {d_3d,             345,210, 60, 20,15,2,   0,D_CLOSE, 0,  0,"3d"     },
  {d_write,          410,210, 60, 20,15,4,   0,D_CLOSE, 0,  0,"Write"  },
  {d_reset,          475,210, 60, 20,15,1,   0,D_CLOSE, 0,  0,"Reset"  },
  {d_button_proc,    540,210, 60, 20,15,1,   0,D_CLOSE, 0,  0,"Exit"   },
  {NULL,               0,  0,  0,  0, 0,0,   0,   0,    0,  0,NULL }
};

void main()
{
  int       c,d;                        // pomocne promenne

  allegro_init();
  install_keyboard();                   // inicializace klavesnice
  install_mouse();                      // inicializace mysi
  install_timer();                      // inicializace casovace
  set_gfx_mode(GFX_VESA1,640,480,0,0);  // graficky rezim 640x480x256
  gui_fg_color=0;                       // popredi pro GUI
  gui_bg_color=7;                       // pozadi pro GUI
  gui_mg_color=1;                       // zakazana polozka v GUI
  for (c=0; c<64;c++) {                 // nastaveni barevne palety
    pallete[c    ].r=c;    pallete[c    ].g=c;    pallete[c    ].b=c;
    pallete[c+ 64].r=c;    pallete[c+ 64].g=c;    pallete[c+ 64].b=c;
    pallete[c+128].r=64-c; pallete[c+128].g=64-c; pallete[c+128].b=64-c;
    pallete[c+192].r=c;    pallete[c+192].g=c;    pallete[c+192].b=c;
  }
  pallete[0].r=0; pallete[0].g=0; pallete[0].b=0;
  pallete[1].r=40;pallete[1].g=0; pallete[1].b=0;
  pallete[2].r=0; pallete[2].g=40;pallete[2].b=0;
  pallete[3].r=40;pallete[3].g=40;pallete[3].b=0;
  pallete[4].r=0; pallete[4].g=0; pallete[4].b=40;
  pallete[5].r=40;pallete[5].g=0; pallete[5].b=40;
  pallete[6].r=0; pallete[6].g=40;pallete[6].b=40;
  pallete[7].r=40;pallete[7].g=40;pallete[7].b=40;
  pallete[8].r=30;pallete[8].g=30;pallete[8].b=20;
  pallete[15].r=63;pallete[15].g=63;pallete[15].b=63;
  set_pallete(pallete);
  calcfrac(fraktal);                    // vypocet prvniho fraktalu
  popup_dialog(main_dialog,-1);         // spustit hlavni dialog
  set_gfx_mode(GFX_TEXT,80,25,0,0);     // bezny textovy mod
  clear_keybuf();                       // vymazat buffer klavesnice
  exit(0);                              // a konec
}

