#include <stdio.h>
#include <xmmintrin.h>

int main(void)
{
    __v8hi x = { 1, 2, 3, 4, 5, 6, 7, 8 };
    __v8hi y = x;
    __v8hi z;
    int i;

    z = __builtin_ia32_paddw128(x, y);

    for (i = 0; i < sizeof(x) / sizeof(short int); i++) {
        printf("%2d %2d %2d %2d\n", i, x[i], y[i], z[i]);
    }
}
