#include <stdio.h>

void decode_decimal32(_Decimal32 value)
{
    const int combination_bits = 11;
    const int trailing_bits = 20;

    const int combination_mask = 0x7ff;
    const int trailing_mask = 0x0fffff;

    const int exponent_bias = 101;


    typedef union {
        _Decimal32 value;
        __uint32_t x;
    } IEEE_754_decimal32;

    IEEE_754_decimal32 d;
    d.value = value;
    __uint32_t x = d.x;

    unsigned int sign = 0x01 & (x >> (combination_bits + trailing_bits));
    unsigned int combination = combination_mask & (x >> trailing_bits);
    unsigned int trailing =  trailing_mask & x;
    unsigned int g10 = 0x01 & (combination >> 10);
    unsigned int g9 = 0x01 & (combination >> 9);

    // hodnota po konverzi
    printf("%+10.4f       ", (float)value);

    // ziskana bitova pole
    printf("%d  %d  %d  %03x  %05x      ", sign, g10, g9, combination, trailing);

    // znamenko
    printf("%c  ", sign ? '-' : '+');

    if ((combination & 0x7c0) == 0x780) {
        printf("infinity\n");
    } else if ((combination & 0x7c0) == 0x7c0) {
        printf("NaN\n");
    } else if ((g10 == 1) && (g9 == 1)) {
        printf("special case\n");
    } else {
        unsigned int exponent = (combination >> 3) - exponent_bias;
        unsigned int mantissa = trailing + ((combination & 0x07) << 20);
        printf("%d x 10^%d\n", mantissa, exponent);
    }
}


int main(void)
{
    _Decimal32 one = 1.0dd;
    _Decimal32 three = 3.0dd;
    _Decimal32 values[] = {0.0dd, 0.1dd, 0.2dd, 1.0dd, 2.0dd,
                           10.0dd, 100.0dd, 1000.0dd, 1000.1dd,
                           one/three, 1.0dd/0.0dd,
                           -0.0dd, -0.1dd, -0.2dd, -1.0dd,
                           -1000.0dd, -1.0dd/0.0dd, 0.0dd/0.0dd};
    int i;

    printf("    value        S G10 G9 comb.trailing   decoded\n");
    for (i=0; i<sizeof(values)/sizeof(_Decimal32); i++) {
        decode_decimal32(values[i]);
    }

    return 0;
}
