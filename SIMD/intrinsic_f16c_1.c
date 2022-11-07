#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v4sf x = { 0.0, 0.1, 1.0, 3.14 };
    __v8hi half;
    __v4sf y;
    int i;

    // konverze float -> half
    half = __builtin_ia32_vcvtps2ph(x, 0);

    // konverze half -> float
    y = __builtin_ia32_vcvtph2ps(half);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d   %f   %04x   %f\n", i, x[i], half[i], y[i]);
    }
    return 0;
}
