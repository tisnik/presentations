#include <stdio.h>
#include <xmmintrin.h>

int main(void)
{
    __v2di x = { 1, 2 };
    __v2di y = x;
    __v2di z;
    int i;

    z = __builtin_ia32_paddq128(x, y);

    for (i = 0; i < sizeof(x) / sizeof(long int); i++) {
        printf("%2d %2Ld %2Ld %2Ld\n", i, x[i], y[i], z[i]);
    }
}
