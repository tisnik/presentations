#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define WIDTH  400
#define HEIGHT 400

void writeImage(int width, int height, unsigned char *image)
{
    int i;
    puts("P2");
    printf("%d %d\n", width, height);
    puts("255");
    for (i=0; i<width*height; i++) {
        printf("%d ", image[i]);
    }
}

#define maxN 100

int main(int argc, char **argv)
{
    double cx, cy;
    double zx, zy;

    int i, j, n;

    char pixels[WIDTH * HEIGHT];
    memset((void*)pixels, 0, (size_t)(WIDTH*HEIGHT));

    double cz = 0.0;
    cy = -3.0;
    for (j = 0; j < HEIGHT; j++) {
        cx = -3.0;
        for (i = 0; i < WIDTH; i++) {
            double zx = 0, zy=0, zz=0;
            for (n = 0; n < maxN; n++) {
                // extract polar coordinates
                float wr = sqrt(zx*zx+zy*zy);
                float wo = atan2(zy, zx);
                //float wi = atan2(zx,zz);

                if (wr > 2.0) break;

                // scale and rotate the point
                wr = pow(wr, 8.0);
                wo = wo * 8.0;
                //wi = wi * 2.0;

                // convert back to cartesian coordinates
                zx = wr*cos(wo)+cx;//*sin(wi);
                zy = wr*sin(wo)+cy;
                //zz = wr*sin(wo)+cz;//*cos(wi);
            }
            pixels[j*WIDTH+i] = n;
            cx += 6.0 / WIDTH;
        }
        cy += 6.0 / HEIGHT;
    }

    writeImage(WIDTH, HEIGHT, pixels);
    return 0;
}

