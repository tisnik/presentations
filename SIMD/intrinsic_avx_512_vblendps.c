#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v16sf x = { 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 };
    __v16sf y = { 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 };
    __v16sf z;
    int i;

    z = __builtin_ia32_blendmps_512_mask(x, y, 0x0000);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }

    putchar('\n');

    z = __builtin_ia32_blendmps_512_mask(x, y, 0x1111);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }

    putchar('\n');

    z = __builtin_ia32_blendmps_512_mask(x, y, 0x5555);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }

    putchar('\n');

    z = __builtin_ia32_blendmps_512_mask(x, y, 0xffff);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }

    return 0;
}
