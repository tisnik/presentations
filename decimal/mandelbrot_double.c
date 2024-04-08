#include <stdlib.h>
#include <stdio.h>

#include "palette_mandmap.h"

typedef double number_type;

#include "mandelbrot.h"

int main(int argc, char **argv)
{
    if (argc < 4) {
        puts("usage: ./mandelbrot width height maxiter");
        return 1;
    }
    int width = atoi(argv[1]);
    int height = atoi(argv[2]);
    int maxiter = atoi(argv[3]);
    calc_mandelbrot(width, height, maxiter, palette);
    return 0;
}

