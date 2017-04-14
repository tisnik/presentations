#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define WIDTH  400
#define HEIGHT 400

#define lado 400

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

double encuentraMax(double arr[lado][lado]) {
    int i=0, j=0;
    double max = 0;
    for (i = 0; i < lado; i++) {
        for (j = 0; j < lado; j++) {
            if (arr[i][j] > max) {
                max = arr[i][j];
                fprintf(stderr, "%f ", max);
            }
        }
    }
    return max;
}


int main(int argc, char **argv)
{
    double cx, cy, increm = 4 / 1000.0;

    int i, j, n;

    const int maxN=200;
    double trayectoria[200][2];
    memset((void*)trayectoria, 0, (size_t)(sizeof(double)*maxN*2));
    int coordX, coordY, color;
    double pixelsTemp[lado][lado];

    unsigned char pixels[lado * lado];
    memset((void*)pixels, 0, (size_t)(lado*lado));

    for (cy = -2; cy < 2; cy += increm) {
        for (cx = -2; cx < 2; cx += increm) {
            double zx = 0, zy = 0;
            for (n = 0; n < maxN; n++) {
                double zx2 = zx * zx;
                double zy2 = zy * zy;
                zy = 2.0 * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                trayectoria[n][0] = zx;
                trayectoria[n][1] = zy;
                if (zx2 + zy2 > 4.0) break;
            }

            if (n < maxN) 
                for (i = 0; i < n; i++) {
                    coordX = (int)(((trayectoria[i][0] + 2) / 4) * lado);
                    coordY = (int)(((trayectoria[i][1] + 2) / 4) * lado);
                    if (coordX < 0 || coordX >= lado || coordY < 0 || coordY >= lado)
                        continue; 
                    pixelsTemp[coordX][coordY]++;
                }
          }
    }

    double maxColor = encuentraMax(pixelsTemp);
    fprintf(stderr, "%f\n", maxColor);
    double factorColor  = 255.0 / maxColor;
    for (i = 0; i < lado; i++)
        for (j = 0; j < lado; j++) {
            color = (int)(pixelsTemp[i][j] * factorColor);
            pixels[i * lado + j] = color;
    }

    writeImage(WIDTH, HEIGHT, pixels);
    return 0;
}

