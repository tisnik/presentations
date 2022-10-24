#include <stdio.h>
#include <xmmintrin.h>

int main(void)
{
    __v16qi x = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 };
    __v16qi y = x;
    __v16qi z;
    int i;

    z = __builtin_ia32_paddb128(x, y);

    for (i = 0; i < sizeof(x) / sizeof(char); i++) {
        printf("%2d %2d %2d %2d\n", i, x[i], y[i], z[i]);
    }
}
