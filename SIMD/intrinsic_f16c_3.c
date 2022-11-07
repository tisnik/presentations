#include <stdio.h>
#include <immintrin.h>

void print_vectors(__v4sf x, __v4sf y, __v8hi half)
{
    int i;

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d   %9.8f   %04x   %9.8f\n", i, x[i], half[i], y[i]);
    }

    putchar('\n');
}

int main(void)
{
    __v4sf x = { 5e-4, 5e-5, 5e-6, 5e-7 };
    __v8hi half;
    __v4sf y;

    // round to nearest even
    half = __builtin_ia32_vcvtps2ph(x, 0);
    y = __builtin_ia32_vcvtph2ps(half);
    print_vectors(x, y, half);

    // round down
    half = __builtin_ia32_vcvtps2ph(x, 1);
    y = __builtin_ia32_vcvtph2ps(half);
    print_vectors(x, y, half);

    // round up
    half = __builtin_ia32_vcvtps2ph(x, 2);
    y = __builtin_ia32_vcvtph2ps(half);
    print_vectors(x, y, half);

    // truncate
    half = __builtin_ia32_vcvtps2ph(x, 3);
    y = __builtin_ia32_vcvtph2ps(half);
    print_vectors(x, y, half);

    return 0;
}
