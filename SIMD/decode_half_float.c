#include <stdio.h>
#include <immintrin.h>

void decode_half(unsigned short int half)
{
    const int exponent_bias = 15;
    const int mantissa_base = 1024;
    const int max_exponent = 31;

    const int mantissa_bits = 10;
    const int exponent_bits = 5;

    unsigned int sign = 0x01 & (half >> (mantissa_bits + exponent_bits));
    unsigned int exponent = 0x1f & (half >> mantissa_bits);
    unsigned int mantissa = 0x03ff & half;

    if (exponent == max_exponent) {
        printf("%c infinity\n", sign ? '-' : '+');
    } else {
        printf("%c %8.6f x 2^%-2d\n", sign ? '-' : '+',
               1.0 + (float) mantissa / mantissa_base, exponent - exponent_bias);
    }
}

void convert_and_decode(__v4sf x)
{
    __v8hi half;
    int i;

    // konverze float -> half
    half = __builtin_ia32_vcvtps2ph(x, 0);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%12.6f    %04hx    ", x[i], half[i]);
        decode_half(half[i]);
    }
}

int main(void)
{
    __v4sf x = { 0.0, 0.1, 1.0, 2.0 };
    convert_and_decode(x);

    __v4sf y = { 10000, 65400, 65504, 65600 };
    convert_and_decode(y);

    __v4sf z = { 1.0, -1.0, 0.01, -0.01 };
    convert_and_decode(z);

    __v4sf w = {0.001, 0.0001, 0.00001, 0.000001 };
    convert_and_decode(w);

    return 0;
}
