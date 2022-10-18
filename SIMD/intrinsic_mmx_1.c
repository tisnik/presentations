#include <stdio.h>
#include <mmintrin.h>

int main(void)
{
    __v8qi x = { 1, 2, 3, 4, 5, 6, 7, 8 };
    __v8qi y = { 1, 2, 3, 4, 5, 6, 7, 8 };
    __v8qi z;
    int i;

    z = __builtin_ia32_paddb(x, y);

    for (i = 0; i < 8; i++) {
        printf("%d %d\n", i, z[i]);
    }
}
