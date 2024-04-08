void calc_mandelbrot(unsigned int width, unsigned int height, unsigned int maxiter, unsigned char palette[][3])
{
    const number_type zero = 0.0;
    const number_type two = 2.0;
    const number_type three = 3.0;
    const number_type bailout = 4.0;

    puts("P3");
    printf("%d %d\n", width, height);
    puts("255");

    number_type cy = -1.5;
    int y;
    for (y=0; y<height; y++) {
        number_type cx = -2.0;
        int x;
        for (x=0; x<width; x++) {
            number_type zx = zero;
            number_type zy = zero;
            unsigned int i = 0;
            while (i < maxiter) {
                number_type zx2 = zx * zx;
                number_type zy2 = zy * zy;
                if (zx2 + zy2 > bailout) {
                    break;
                }
                zy = two * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                i++;
            }
            unsigned char *color = palette[i % 256];
            unsigned char r = *color++;
            unsigned char g = *color++;
            unsigned char b = *color;
            printf("%d %d %d\n", r, g, b);
            cx += three/width;
        }
        cy += three/height;
    }
}
