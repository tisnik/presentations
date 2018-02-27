#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define FILE_NAME       "ifs_"                  // zacatek jmena souboru pro ulozeni pixmapy

#define PIXMAP_WIDTH    352                     // sirka pixmapy
#define PIXMAP_HEIGHT   288                     // vyska pixmapy

typedef struct {                                // struktura popisujici pixmapu
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} pixmap;

pixmap *pix;

float fmap[PIXMAP_HEIGHT][PIXMAP_WIDTH];        // pixmapa s floaty pro logaritmovani histogramu

static double data[][7]={
    // binary
    { 0.500000, 0.000000, 0.000000, 0.500000,-2.563477,-0.000003, 0.333333},
    { 0.500000, 0.000000, 0.000000, 0.500000, 2.436544,-0.000003, 0.333333},
    { 0.000000,-0.500000, 0.500000, 0.000000, 4.873085, 7.563492, 0.333333},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // coral
    { 0.307692,-0.531469,-0.461538,-0.293706, 5.401953, 8.655175, 0.400000},
    { 0.307692,-0.076923, 0.153846,-0.447552,-1.295248, 4.152990, 0.150000},
    { 0.000000, 0.545455, 0.692308,-0.195804,-4.893637, 7.269794, 0.450000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // crystal
    { 0.696970,-0.481061,-0.393939,-0.662879, 2.147003,10.310288, 0.747826},
    { 0.090909,-0.443182, 0.515152,-0.094697, 4.286558, 2.925762, 0.252174},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // dragon
    { 0.824074, 0.281482,-0.212346, 0.864198,-1.882290,-0.110607, 0.787473},
    { 0.088272, 0.520988,-0.463889,-0.377778, 0.785360, 8.095795, 0.212527},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // dragon2
    { 0.824074, 0.281481,-0.212346, 0.864197,-1.772710, 0.137795, 0.771268},
    {-0.138580, 0.283951,-0.670062,-0.279012, 2.930991, 7.338924, 0.228732},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // feathe
    { 0.870370, 0.074074,-0.115741, 0.851852,-1.278016, 0.070331, 0.798030},
    {-0.162037,-0.407407, 0.495370, 0.074074, 6.835726, 5.799174, 0.201970},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // fern
    { 0.850000, 0.040000,-0.040000, 0.850000, 0.000000, 1.600000, 0.850000},
    { 0.200000,-0.260000, 0.230000, 0.220000, 0.000000, 1.600000, 0.070000},
    {-0.150000, 0.280000, 0.260000, 0.240000, 0.000000, 0.440000, 0.070000},
    { 0.000000, 0.000000, 0.000000, 0.160000, 0.000000, 0.000000, 0.010000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // koch
    { 0.307692, 0.000000, 0.000000, 0.294118, 4.119164, 1.604278, 0.151515},
    { 0.192308,-0.205882, 0.653846, 0.088235,-0.688840, 5.978916, 0.253788},
    { 0.192308, 0.205882,-0.653846, 0.088235, 0.668580, 5.962514, 0.253788},
    { 0.307692, 0.000000, 0.000000, 0.294118,-4.136530, 1.604278, 0.151515},
    { 0.384615, 0.000000, 0.000000,-0.294118,-0.007718, 2.941176, 1.000000},

    // spiral
    { 0.787879,-0.424242, 0.242424, 0.859848, 1.758647, 1.408065, 0.895652},
    {-0.121212, 0.257576, 0.151515, 0.053030,-6.721654, 1.377236, 0.052174},
    { 0.181818,-0.136364, 0.090909, 0.181818, 6.086107, 1.568035, 0.052174},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // tree
    { 0.000000, 0.000000, 0.000000, 0.500000, 0.000000, 0.000000, 0.050000},
    { 0.420000,-0.420000, 0.420000, 0.420000, 0.000000, 0.200000, 0.400000},
    { 0.420000, 0.420000,-0.420000, 0.420000, 0.000000, 0.200000, 0.400000},
    { 0.100000, 0.000000, 0.000000, 0.100000, 0.000000, 0.200000, 0.150000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    // triangle
    { 0.500000, 0.000000, 0.000000, 0.500000,-0.500000, 0.000000, 0.333333},
    { 0.500000, 0.000000, 0.000000, 0.500000, 0.500000, 0.000000, 0.333333},
    { 0.500000, 0.000000, 0.000000, 0.500000, 0.000000, 0.860000, 0.333334},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

};



//-----------------------------------------------------------------------------
// Funkce pro vytvoreni pixmapy o zadane velikosti
//-----------------------------------------------------------------------------
pixmap * createPixmap(const unsigned int width, const unsigned int height)
{
    pixmap *p=(pixmap *)malloc(sizeof(pixmap)); // alokace struktury pixmapy
    if (!p) return NULL;
    p->width=width;                             // naplneni struktury
    p->height=height;
    p->pixels=(unsigned char *)malloc(3*width*height);
    if (!p->pixels) {                           // alokace pole pro pixely
        free(p);                                // alokace se nepovedla
        return NULL;
    }
    else {
        memset(p->pixels, 0, 3*width*height);   // smazani pixmapy
    }
    return p;
}



//-----------------------------------------------------------------------------
// Funkce pro zruseni pixmapy
//-----------------------------------------------------------------------------
void destroyPixmap(pixmap *p)
{
    if (p->pixels) free(p->pixels);             // uvolnit vlastni pixmapu
    if (p) free(p);                             // i okolni strukturu
}



//-----------------------------------------------------------------------------
// Vymazani pixmapy
//-----------------------------------------------------------------------------
void clearPixmap(const pixmap *p)
{
    if (!p) return;
    if (!p->pixels) return;
    memset(p->pixels, 0, 3*p->width*p->height);
    memset(fmap, 0, PIXMAP_WIDTH*PIXMAP_HEIGHT*sizeof(float));
}



//-----------------------------------------------------------------------------
// Ulozeni pixmapy do externiho souboru
//-----------------------------------------------------------------------------
void savePixmap(const pixmap *p, const char *fileName)
{
    FILE *fout;
    unsigned int i, j, k;
    unsigned char tgaHeader[18]={               // hlavicka formatu typu TGA
                        0x00,                   // typ hlavicky TGA
                        0x00,                   // nepouzivame paletu
                        0x02,                   // typ obrazku je RGB TrueColor
                        0x00, 0x00,             // delka palety je nulova
                        0x00, 0x00, 0x00,       // pozice v palete nas nezajima
                        0x00, 0x00, 0x00, 0x00, // obrazek je umisteny na pozici [0, 0]
                        0x00, 0x00, 0x00, 0x00, // sirka a vyska obrazku (dva byty na polozku)
                        0x18,                   // format je 24 bitu na pixel
                        0x20                    // orientace bitmapy v obrazku
    };
    if (!p || !p->pixels) return;
    memcpy(tgaHeader+12, &(p->width), 2);       // do hlavicky TGA zapsat velikost obrazku
    memcpy(tgaHeader+14, &(p->height), 2);
    fout=fopen(fileName, "wb");
    if (fout) {
        fwrite(tgaHeader, 18, 1, fout);         // zapsat hlavicku TGA do souboru
        for (j=p->height; j; j--) {             // radky zapisovat v opacnem poradi
            unsigned int yoff=(j-1)*3*p->width; // y-ovy offset v poli
            unsigned int xoff=0;                // x-ovy offset v poli
            for (i=0; i<p->width; i++) {        // pro kazdy pixel na radku
                for (k=0; k<3; k++) {           // prohodit barvy RGB na BGR
                    fputc(p->pixels[xoff+yoff+2-k], fout); // a zapsat do souboru
                }
                xoff+=3;                        // posun na dalsi pixel
            }
        }
        fclose(fout);
    }
}



//-----------------------------------------------------------------------------
// Zmena barvy pixelu na zadanych souradnicich
//-----------------------------------------------------------------------------
void putpixel(pixmap *p,
              const unsigned int x,             // pozice pixelu v pixmape
              const unsigned int y,
              const unsigned char r,            // barva pixelu
              const unsigned char g,
              const unsigned char b)
{
    int pos;
    // zde se vyuziva zkraceneho vyhodnoceni vyrazu - pokud plati !p, nic se dale netestuje
    if (!p || !p->pixels || x>=p->width || y>=p->height) return;
    pos=3*(x+y*p->width);
    p->pixels[pos++]=r;                         // nastaveni barvy pixelu
    p->pixels[pos++]=g;
    p->pixels[pos]=b;
}



//-----------------------------------------------------------------------------
// Prirustek barvy pixelu na zadanych souradnicich
//-----------------------------------------------------------------------------
void addpixel(pixmap *p, const unsigned int x, const unsigned int y,
                         const unsigned char dr, const unsigned char dg, const unsigned char db)
{
    int pos;
    // zde se vyuziva zkraceneho vyhodnoceni vyrazu - pokud plati !p, nic se dale netestuje
    if (!p || !p->pixels || x>=p->width || y>=p->height) return;
    pos=3*(x+y*p->width);
    if (p->pixels[pos]<256-dr) p->pixels[pos]+=dr;// nastaveni cervene slozky barvy pixelu
    pos++;
    if (p->pixels[pos]<256-dg) p->pixels[pos]+=dg;// nastaveni zelene slozky barvy pixelu
    pos++;
    if (p->pixels[pos]<256-db) p->pixels[pos]+=db;// nastaveni modre slozky barvy pixelu
}



//-----------------------------------------------------------------------------
void addfloat(const unsigned int x, const unsigned int y)
{
    if (x>=PIXMAP_WIDTH || y>=PIXMAP_HEIGHT) return;
    fmap[y][x]++;
}



//-----------------------------------------------------------------------------
void recalcIFS(pixmap *pix, int maxIter, int startIter, double morphRatio, int firstIFS, int secondIFS)
{
    double x1=0, y1=0, x2=0, y2=0;              // generovane souradnice
    double xmin=1e10, xmax=-1e10;               // obdelnik opsany IFS fraktalu
    double ymin=1e10, ymax=-1e10;
    int    x, y, k;
    double pp, sum;
    double delitel=12.0;
    int i,j;

    double a[5][7];
    xmin=-7.0; xmax=10.0; ymin=-1.0; ymax=00.0;

    for (j=0; j<5; j++) {                       // prenos koeficientu IFS systemu
        for (i=0; i<7; i++) {                   // a smichani prvniho a druheho systemu
            a[j][i]=(1.0-morphRatio)*data[j+firstIFS*5][i]
                   +(morphRatio)*data[j+secondIFS*5][i];
        }
    }
    for (i=0; i<maxIter; i++) {                 // pro vsechny iterace
        pp=((float)rand())/RAND_MAX;            // p lezi v rozsahu 0.0-1.0
        sum=0;                                  // na zaklade nahodneho cisla
        for (k=0; sum<=pp; k++)                 // najit transformaci
            sum+=a[k][6];
        k--;
        x2=x1*a[k][0] + y1*a[k][1] + a[k][4];   // aplikovat transformaci
        y2=x1*a[k][2] + y1*a[k][3] + a[k][5];
        x1=x2; y1=y2;
        if (i>startIter) {                      // pokud byl prekrocen pocet
            x2=(x1-xmin)*(double)(pix->width)/delitel; // startovnich iteraci
            y2=(y1-ymin)*(double)(pix->height)/delitel;
            x=(int)x2; y=(int)y2;               // vypocitat a zobrazit pozice pixelu
            addfloat(x, y);
            //addpixel(pix, x, y, 10, 10, 10);
            // putpixel(pix, x, y, 255, 255, 255);
        }
        /*
        else {                                  // pokud se jedna o startovni iterace
            if (x1<xmin) xmin=x1;               // provest vypocet opsaneho obdelnika
            if (y1<ymin) ymin=y1;
            if (x1>xmax) xmax=x1;
            if (y1>ymax) ymax=y1;
        }
        if (i==startIter) {                     // zafixovat opsany obdelnik
            xmin*=1.1;
            xmax*=1.1;
            ymin*=1.1;
            ymax*=1.1;
            delitel=(xmax-xmin);
            if (ymax-ymin>xmax-xmin) delitel=ymax-ymin;
        }*/
    }
    {                                           // logaritmovani histogramu a prevod na byty
        float maxp=0;
        for (j=0; j<PIXMAP_HEIGHT; j++)
            for (i=0; i<PIXMAP_WIDTH; i++)
                if (maxp<fmap[j][i]) maxp=fmap[j][i];
        printf("maxp=%f\n", maxp);
        for (j=0; j<PIXMAP_HEIGHT; j++) {
            for (i=0; i<PIXMAP_WIDTH; i++) {
                float pixel=log(fmap[j][i])/log(maxp)*255.0;
                putpixel(pix, i, j, (int)pixel, (int)pixel, (int)pixel);
            }
        }
    }
    
}



//-----------------------------------------------------------------------------
// Hlavni funkce konzolove aplikace
//-----------------------------------------------------------------------------
int main(int argc, char **argv)
{
    int    maxiter=100000;
    int    startiter=100;
    int    frames=100;
    int    i,j, cnt=0;
    char   name[50];
    int    zac[]={0, 3, 6, 7, 8};
    int    kon[]={3, 6, 7, 8, 0};

    puts("\nfractals_ifs\n");

    printf("processing:\n");

    // vytvoreni a prvotni smazani pixmapy
    pix=createPixmap(PIXMAP_WIDTH, PIXMAP_HEIGHT);
    clearPixmap(pix);

    for (j=0; j<5; j++) {
        for (i=0; i<frames; i++) {
            clearPixmap(pix);
            sprintf(name, "%s%03d%s", FILE_NAME, cnt++, ".tga");
            printf("%3d\t", i);
            recalcIFS(pix, maxiter, startiter, (float)i/(frames-1.0), zac[j], kon[j]);
            savePixmap(pix, name);
        }
    }
    printf("\ndone!\n");
    return 0;
}



//-----------------------------------------------------------------------------
// finito
//-----------------------------------------------------------------------------

