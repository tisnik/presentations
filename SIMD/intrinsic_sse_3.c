#include <stdio.h>
#include <xmmintrin.h>

int main(void)
{
    __v4si x = { 1, 2, 3, 4 };
    __v4si y = x;
    __v4si z;
    int i;

    z = __builtin_ia32_paddd128(x, y);

    for (i = 0; i < sizeof(x) / sizeof(int); i++) {
        printf("%2d %2d %2d %2d\n", i, x[i], y[i], z[i]);
    }
}
