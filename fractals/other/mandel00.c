// Mandelbrotova mnozina vypocitana ve float-point
// vnitrni smycka napsana v assembleru

#include <math.h>
#include <conio.h>
#include <dos.h>

void main()
{
  float c2=2.0;
  float c4=4.0;
  int x,y;                              /* pro pozici na obrazovce */
  int iter;                             /* pocitadlo iteraci */
  float xpos,ypos;                      /* pozice v mnozine */
  float zx1,zy1,zx2,zy2;                /* pro pocitani z^2+c */
  float ccx,ccy;                                /* -//- */
  unsigned int adr=0;

  asm {
    mov ax,0x13
    int 0x10

//    mov       dword ptr [bp-8],large 0C0200000h       // xpos=-2.5
//    mov       dword ptr [bp-12],large 0C0000000h      // ypos=-2.0
  }
  xpos=-2.5;
  ypos=-2.0;
  for (y=0; y<200; y++)
  {
    ypos+=4.0/200.0;                    /* dalsi radek */
    xpos=-2.5;
    for (x=0; x<320; x++)
    {
      xpos+=4.0/260.0;
      zx1=0;                            /* pro pocatecni iteraci */
      zy1=0;
      ccx=xpos;                         /* pocatecni pozice v mnozine */
      ccy=ypos;
        asm {
        mov    ax,50
        mov    iter,ax
        }
smycka: asm {
        fld    zx1                //|
        fmul   zx1                //|zx2=zx1*zx1
        fstp   zx2                //|

        fld    zy1                //|
        fmul   zy1                //|zy2=zy1*zy1
        fstp   zy2                //|

        fld    c2                 //|
        fmul   zx1                //|
        fmul   zy1                //|zy1=c2*zx1*zy1+cy
        fadd   ccy                //|
        fstp   zy1                //|

        fld    zx2                //|
        fsub   zy2                //|zx1=zx2-zy2+cx
        fadd   ccx                //|
        fstp   zx1                //|

        fld    zx2
        fadd   zy2
        fcomp  c4
        fstsw  ax
        sahf
        jnb    short pokr
        dec    iter
        jnz    smycka
      }
pokr:
      pokeb(0xa000,adr,50-iter);
      adr++;
    }
  }
  getch();
  asm {
    mov ax,0x03
    int 0x10
  }
}
