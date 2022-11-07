#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v8sf x = { 0.0, 0.1, 1.0, 3.14, 1e5, 1e10, 1e15, -1e10 };
    __v8hi half;
    __v8sf y;
    int i;

    // konverze float -> half
    half = __builtin_ia32_vcvtps2ph256(x, 0);

    // konverze half -> float
    y = __builtin_ia32_vcvtph2ps256(half);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d   %8.6g   %04hx   %f\n", i, x[i], half[i], y[i]);
    }
    return 0;
}
