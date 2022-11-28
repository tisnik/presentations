#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v16sf x = { 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 };
    __v16sf y = { 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 };
    __v16sf z = -x;
    __v16sf w;
    int i;

    w = __builtin_ia32_addps512_mask(x, y, z, 0, _MM_FROUND_CUR_DIRECTION);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d  %5.1f  %5.1f  %5.1f  %5.1f\n", i, x[i], y[i], z[i], w[i]);
    }

    w = __builtin_ia32_addps512_mask(x, y, z, 0xf0f0, _MM_FROUND_CUR_DIRECTION);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d  %5.1f  %5.1f  %5.1f  %5.1f\n", i, x[i], y[i], z[i], w[i]);
    }

    w = __builtin_ia32_addps512_mask(x, y, z, -1, _MM_FROUND_CUR_DIRECTION);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d  %5.1f  %5.1f  %5.1f  %5.1f\n", i, x[i], y[i], z[i], w[i]);
    }

    return 0;
}
