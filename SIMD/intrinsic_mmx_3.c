#include <stdio.h>
#include <mmintrin.h>

int main(void)
{
    __v8qi x = { 0, 2, 4, 6, 8, 10, 12, 14 };
    __v8qi y = { 120, 120, 120, 120, 120, 120, 120, 120 };
    __v8qi z;
    int i;

    z = __builtin_ia32_paddb(x, y);

    for (i = 0; i < 8; i++) {
        printf("%d %d %d %d\n", i, x[i], y[i], z[i]);
    }
}
