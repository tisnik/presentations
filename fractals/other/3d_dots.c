#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <allegro.h>
#include <values.h>

#define BODU 5000
/*
float a[10][3][3]={
      { {0.40,0.00,0.00},
        {0.00,0.50,0.00},
        {0.00,0.00,0.50}},
      { {0.50,0.00,0.00},
        {0.00,0.60,0.00},
        {0.00,0.00,0.50}},
      { {0.50,0.00,0.00},
        {0.00,0.50,0.00},
        {0.00,0.00,0.50}},
      { {0.50,0.00,0.00},
        {0.00,0.40,0.00},
        {0.00,0.00,0.70}}
};

float b[10][3]={
    { 0.00, 0.00, 1.00},
    { 0.00, 0.87,-0.50},
    {-0.87,-0.50,-0.50},
    { 0.87,-0.50,-0.50}
};

float p[10]={
    0.25,0.25,0.25,0.25
};
*/

float a[10][3][3]={
      { {0.00,0.00,0.00},
        {0.00,0.18,0.00},
        {0.00,0.00,0.00}},
      { {0.85,0.00,0.00},
        {0.00,0.85,0.10},
        {0.00,-0.1,0.85}},
      { {0.20,-0.2,0.00},
        {0.20,0.20,0.00},
        {0.00,0.00,0.30}},
      { {-0.2,0.20,0.00},
        {0.20,0.20,0.00},
        {0.00,0.00,0.30}}
};

float b[10][3]={
    { 0.00, 0.00, 1.00},
    { 0.00, 1.60, 0.00},
    { 0.00, 0.80, 0.00},
    { 0.00, 0.80, 0.00}
};

float p[10]={
    0.01,0.85,0.07,0.07
};

fixed bodx[BODU];
fixed body[BODU];
fixed bodz[BODU];
char  bodc[BODU];
int   oldx[BODU];
int   oldy[BODU];

float rrandom(float max)
{
    return(random()*max/MAXINT);
}

void ifs(void)
{
    float x,y,z,x1,y1,z1;
    float pp;
    float sum;
    int   i,k;

    x=0;y=0;z=0;                          // pocatecni poloha bodu
    for (i=0;i<BODU;i++) {                // pocet iteraci
        pp=rrandom(255)/255.0;               // pravdepodobnost pro vyber transformace
        k=0;                                // promenna cyklu
        sum=0;
        while (sum<=pp)
        {
            sum=sum+p[k];
            k++;
        }					                // k urcuje druh transformace
        k--;
        x1=a[k][0][0]*x+a[k][0][1]*y+a[k][0][2]*z+b[k][0];
        y1=a[k][1][0]*x+a[k][1][1]*y+a[k][1][2]*z+b[k][1];
        z1=a[k][2][0]*x+a[k][2][1]*y+a[k][2][2]*z+b[k][2];
        x=x1;y=y1;z=z1;
        bodx[i]=ftofix(x*20.0);
        body[i]=ftofix((y-5.8)*20.0);
        bodz[i]=ftofix(z*20.0);
        bodc[i]=k+9;
    }
}

void main(void)
{
  int d;
  fixed x,y,z;
  struct MATRIX matice;
  int   pozx,pozy;

  allegro_init();
  install_keyboard();
  set_gfx_mode(GFX_VGA,320,200,0,0);
  ifs();
  get_transformation_matrix(&matice,ftofix(1.0),
                            ftofix(3.0),ftofix(4.0),ftofix(5.0),
                            ftofix(0.0),ftofix(0.0),ftofix(0.0));
  while (!keypressed()) {
    for (d=0;d<BODU;d++) {
#define PER 256
      apply_matrix(&matice,bodx[d],body[d],bodz[d],&x,&y,&z);
      bodx[d]=x;body[d]=y;bodz[d]=z;
      pozx=160+fixtoi(fdiv (bodx[d]*PER,bodz[d]+itofix(PER)) );
      pozy=100+fixtoi(fdiv (body[d]*PER,bodz[d]+itofix(PER)) );
      putpixel(screen,oldx[d],oldy[d],0);
      putpixel(screen,pozx,pozy,bodc[d]);
      oldx[d]=pozx;
      oldy[d]=pozy;
    }
  };
  remove_keyboard();
  allegro_exit();
}

