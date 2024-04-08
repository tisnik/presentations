#include <stdio.h>

void decode_double(double value)
{
    const int exponent_bias = 1023;
    const __uint64_t mantissa_base = 1L << 52;
    const int max_exponent = 2047;
    const __uint64_t mantissa_mask = 0x0fffffffffffff;

    const int mantissa_bits = 52;
    const int exponent_bits = 11;

    typedef union {
        double value;
        __uint64_t x;
    } IEEE_754_double;

    IEEE_754_double d;
    d.value = value;
    __uint64_t x = d.x;

    unsigned int sign = 0x01 & (x >> (mantissa_bits + exponent_bits));
    unsigned int exponent = max_exponent & (x >> mantissa_bits);
    __uint64_t mantissa = mantissa_mask & x;

    printf("%+10.4f       ", value);

    if (exponent == max_exponent) {
        if (mantissa == 0) {
            printf("%c infinity\n", sign ? '-' : '+');
        } else {
            puts("NaN");
        }
    } else {
        printf("%c %10.8f x 2^%-2d\n", sign ? '-' : '+',
               1.0 + (double) mantissa / mantissa_base, exponent - exponent_bias);
    }
}


int main(void)
{
    double values[] = {0.0, 0.1, 0.2, 1.0, 2.0, 10.0, 100.0, 1000.0, 1000.1, 1.0/0.0, -0.0, -0.1, -0.2, -1.0, -1000.0, -1.0/0.0, 0.0/0.0};
    int i;

    for (i=0; i<sizeof(values)/sizeof(double); i++) {
        decode_double(values[i]);
    }

    return 0;
}
