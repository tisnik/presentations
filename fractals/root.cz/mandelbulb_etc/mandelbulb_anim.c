#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define WIDTH  400
#define HEIGHT 400

void writeImage(char *filename, int width, int height, unsigned char *image)
{
    int i;
    FILE *fout;

    fout = fopen(filename, "wb");
    fputs("P5\n", fout);
    fprintf(fout, "%d %d\n", width, height);
    fputs("255\n", fout);
    for (i=0; i<width*height; i++) {
        fputc(image[i], fout);
    }
    fclose(fout);
}

#define maxN 400

int main(int argc, char **argv)
{
    double cx, cy;
    double zx, zy;

    int i, j, k, n;

    char filename[100];
    char pixels[WIDTH * HEIGHT];

    double cz = 0.0;
    for (k = 0; k <= 20; k++) {
        memset((void*)pixels, 0, (size_t)(WIDTH*HEIGHT));
        fprintf(stderr, "%d %f\n", k, cz);
        cy = -2.0;
        for (j = 0; j < HEIGHT; j++) {
            cx = -2.0;
            for (i = 0; i < WIDTH; i++) {
                double zx = 0, zy=0, zz=0;//*/acos(zz/wr);cz;
                for (n = 0; n < maxN; n++) {
                    float wr, phi, rho;
                    // extract polar coordinates
                    wr = sqrt(zx*zx+zy*zy+zz*zz);
                    phi = wr == 0.0 ? 0.0 : atan2(zy, zx);
                    rho = wr == 0.0 ? 0.0 : atan2(sqrt(zx*zx+zy*zy), zz);//acos(zz/wr);

                    if (wr > 2.0) break;

                    // scale and rotate the point
                    wr = pow(wr, 8.0);
                    phi = phi * 8.0;
                    rho = rho * 8.0;

                    // convert back to cartesian coordinates
                    zx = wr*sin(rho)*cos(phi)+cx;
                    zy = wr*sin(rho)*sin(phi)+cy;
                    zz = wr*cos(rho)+cz;
                }
                if (n == maxN) {
                    pixels[j*WIDTH+i] = 255;
                }
                cx += 4.0 / WIDTH;
            }
            cy += 4.0 / HEIGHT;
        }
        cz += 1.0 / 20.0;
        sprintf(filename, "out_%02d.pgm", k);
        writeImage(filename, WIDTH, HEIGHT, pixels);
    }

    return 0;
}

