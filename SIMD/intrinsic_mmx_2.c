#include <stdio.h>
#include <mmintrin.h>

int main(void)
{
    __v4hi x = { 1, 2, 3, 4 };
    __v4hi y = { 1000, 1000, 1000, 1000 };
    __v4hi z;
    int i;

    z = __builtin_ia32_paddw(x, y);

    for (i = 0; i < 4; i++) {
        printf("%d %d\n", i, z[i]);
    }
}
