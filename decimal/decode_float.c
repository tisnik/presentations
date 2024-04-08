#include <stdio.h>

void decode_float(float value)
{
    const int exponent_bias = 127;
    const int mantissa_base = 1 << 23;
    const int max_exponent = 255;
    const int mantissa_mask = 0x07fffff;

    const int mantissa_bits = 23;
    const int exponent_bits = 8;

    typedef union {
        float value;
        __uint32_t x;
    } IEEE_754_float;

    IEEE_754_float f;
    f.value = value;
    __uint32_t x = f.x;

    unsigned int sign = 0x01 & (x >> (mantissa_bits + exponent_bits));
    unsigned int exponent = max_exponent & (x >> mantissa_bits);
    unsigned int mantissa = mantissa_mask & x;

    printf("%+10.4f       ", value);

    if (exponent == max_exponent) {
        if (mantissa == 0) {
            printf("%c infinity\n", sign ? '-' : '+');
        } else {
            puts("NaN");
        }
    } else {
        printf("%c %10.8f x 2^%-2d\n", sign ? '-' : '+',
               1.0 + (float) mantissa / mantissa_base, exponent - exponent_bias);
    }
}


int main(void)
{
    float values[] = {0.0, 0.1, 0.2, 1.0, 2.0, 10.0, 100.0, 1000.0, 1000.1, 1.0/0.0, -0.0, -0.1, -0.2, -1.0, -1000.0, -1.0/0.0, 0.0/0.0};
    int i;

    for (i=0; i<sizeof(values)/sizeof(float); i++) {
        decode_float(values[i]);
    }

    return 0;
}
