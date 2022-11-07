#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v4sf x = { 1e3, 1e4, 1e5, 1e6 };
    __v8hi half;
    __v4sf y;
    int i;

    // konverze float -> half
    half = __builtin_ia32_vcvtps2ph(x, 0);

    // konverze half -> float
    y = __builtin_ia32_vcvtph2ps(half);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d  %7.0f   %04x   %7.0f\n", i, x[i], half[i], y[i]);
    }
    return 0;
}
