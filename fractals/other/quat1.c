#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "allegro.h"

BITMAP *bmp;
PALLETE pal;

  int zant=450;   //z-resolution. bigger zant -> better resolution
  int zant1=25;   //z-resolution. bigger zant -> better resolution
  int pixsize=2, vissize=1;

  double xmin=-1.66, xmax=1;
  double ymin=-1, ymax=1;
  double zmin=-1.7, zmax=1.7;
  int iter=6;

  double lightx=-1, lighty=1, lightz=-3;

  double vx=0, vy=0, vz=0;

  double cr=0.50;  //constant real value
  double ci=0.40;  //constant imaginary(1) value
  double cj=1;  //constant imaginary(2) value
  double ck=0.05;   //constant imaginary(3) value
  double wk=-0.55;   //4th dimension

  int background = 0;

  int maxcolor = 16;

  int sx,sy;
  double dx,dy,dz;
  double origx, origy, origz;
  double rminx, rminy, rminz;
  double dxx, dxy, dxz;
  double dyx, dyy, dyz;
  double dzx, dzy, dzz;
  double dzx1, dzy1, dzz1;
  double tempx, tempy, tempz;
  double cosx,cosy,cosz,sinx,siny,sinz;
  double z_buffer[320][10];
  int buffer_y;

void rotate3D(double * xxx,double * yyy,double * zzz)
{
  double x,y,z;
  double xy,xz,xx,yx,yz,zx,zy;

  x=(*xxx);
  y=(*yyy);
  z=(*zzz);

  x-=origx;y-=origy;z-=origz;
  xy=y*cosx-z*sinx;
  xz=y*sinx+z*cosx;
  xx=x;
  x=xx;
  y=xy;
  z=xz;
  yx=x*cosy+z*siny;
  yz=-x*siny+z*cosy;
  x=yx;
  z=yz;
  zx=x*cosz-y*sinz;
  zy=x*sinz+y*cosz;
  x=zx;
  y=zy;
  x+=origx;y+=origy;z+=origz;
  (*xxx)=x;
  (*yyy)=y;
  (*zzz)=z;
}

void rotatevalues()
{
  rminx=xmin;rminy=ymin;rminz=zmin;
  rotate3D(&rminx, &rminy, &rminz);
  tempx=xmax;tempy=ymin;tempz=zmin;
  rotate3D(&tempx, &tempy, &tempz);
  dxx=(tempx-rminx)/sx;dxy=(tempy-rminy)/sx;dxz=(tempz-rminz)/sx;
  tempx=xmin;tempy=ymax;tempz=zmin;
  rotate3D(&tempx, &tempy, &tempz);
  dyx=(tempx-rminx)/sy;dyy=(tempy-rminy)/sy;dyz=(tempz-rminz)/sy;
  tempx=xmin;tempy=ymin;tempz=zmax;
  rotate3D(&tempx, &tempy, &tempz);
  dzx=(tempx-rminx)/zant;dzy=(tempy-rminy)/zant;dzz=(tempz-rminz)/zant;
  dzx1=dzx/zant1;dzy1=dzy/zant1;dzz1=dzz/zant1;
}

double calc_l(double x, double y, double z)
{     //  (x,y,z,w)^2 =
		//					( x*x - y*y - z*z - w*w ,
		//					  x*y + y*x + z*w - w*z ,
		//					  x*z + z*x - y*w + w*y ,
		//					  x*w + w*x + y*z - z*y ) }
  double lengde;
  double temp;
  double w=wk;
  int m=0;
  do {
	temp=x+x;
	x=x*x-y*y-z*z-w*w+cr;
	y=temp*y+ci;
	z=temp*z+cj;
	w=temp*w+ck;

	m++;
	lengde=x*x+y*y+z*z+w*w;
  } while ((m<iter) && (lengde<2));
 return lengde;
}

double calc_angle(double w,double e,double n,double s,double cx,double cy,double cz)
{
  double lightdx=cx-lightx;
  double lightdy=cy-lighty;
  double lightdz=cz-lightz;

  double lightlength=sqrt(lightdx*lightdx+lightdy*lightdy+lightdz*lightdz);

  double fx=/*(0)*(s-n)*/-(e-w)*(dy+dy);
  double fy=/*(e-w)*(0)*/-(dx+dx)*(s-n);
  double fz=(dx+dx)*(dy+dy)/*-(0)*(0)*/;

  double flength=sqrt(fx*fx+fy*fy+fz*fz);
  double c=(fx*lightdx+fy*lightdy+fz*lightdz)/(flength*lightlength);
  return c;
}

void show_buffer(int y)
{
  double a;
  int t,i;

  for (t=1; t<sx; t++) {
	 for (i=1; i<=8; i++) {
		if ((y+i)<sy) {
		  a=calc_angle(z_buffer[t-1][i],z_buffer[t+1][i],z_buffer[t][i-1],z_buffer[t][i+1]
						 ,t*dx+xmin,(y+i)*dy+ymin,z_buffer[t][i]);
		  if ((z_buffer[t][i]>zmax) && (background==0)) {
//			 setfillstyle(1,0);
		  } else if (a<0) {
//			 setfillstyle(1,1);
		  } else {
//			 setfillstyle(1,1+(maxcolor-1)*a);
		  }
                  putpixel(screen,t,y+i,a);
		}
	 }
  }

  for (t=0; t<640; t++) {
	 z_buffer[t][0]=z_buffer[t][8];
	 z_buffer[t][1]=z_buffer[t][9];
  }
  buffer_y=2;
}


void main()
{
  int pz, pz1;
  double l;
  double dz1;
  int px,py,ve;

  allegro_init();
  install_keyboard();
  set_gfx_mode(GFX_VGA, 320, 200, 0, 0);
/*
  for (int i=1; i<16; i++) {
	 setrgbpalette(i, 0, i*4, 0);
	 setpalette(i, i);
  }
  setrgbpalette(0,0,0,63);
  setpalette(0, 0);
*/

  sx=320/pixsize;sy=200/pixsize;
  dx=(xmax-xmin)/sx;
  dy=(ymax-ymin)/sy;
  dz=(zmax-zmin)/zant;
  dz1=dz/zant1;

  origx=(xmin+xmax)/2;
  origy=(ymin+ymax)/2;
  origz=(zmin+zmax)/2;


  ve=0;
  vx=vx/180*3.14159265;
  vy=vy/180*3.14159265;
  vz=vz/180*3.14159265;


  cosx=cos(vx);cosy=cos(vy);cosz=cos(vz);
  sinx=sin(vx);siny=sin(vy);sinz=sin(vz);

  rotatevalues();

  buffer_y=0;
  for (py=0; py<=sy; py++) {
	 for (px=0; px<=sx; px++) {
		tempx=rminx+px*dxx+py*dyx/*+pz*dzx*/;
		tempy=rminy+px*dxy+py*dyy/*+pz*dzy*/;
		tempz=rminz+px*dxz+py*dyz/*+pz*dzz*/;
		pz=0;
		do {
		  tempx+=dzx;
		  tempy+=dzy;
		  tempz+=dzz;
		  l=calc_l(tempx,tempy,tempz);
		  pz++;
		} while ((l>2) && (pz<zant));
		pz1=0;
		do {
		  pz1++;
		  tempx-=dzx1;
		  tempy-=dzy1;
		  tempz-=dzz1;
		  l=calc_l(tempx,tempy,tempz);
		} while (l<2);
		if (pz < zant)
		  z_buffer[px][buffer_y]=zmin+pz*dz-pz1*dz1;
		else
		  z_buffer[px][buffer_y]=zmax+dz;
//		setfillstyle(1,15-pz/10);
                putpixel(screen,px,py,15-pz/10);
//		bar(px*vissize,py*vissize,px*vissize+vissize-1,py*vissize+vissize-1);
		if (kbhit()) break;
	 }
	 buffer_y++;
	 if (buffer_y==10) show_buffer(py-9);
	 if (kbhit()) break;
  }
  if (!kbhit()) {
	 show_buffer(py-buffer_y);
  }
}