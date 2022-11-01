#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v4df x = { 1.0, 2.0, 3.0, 4.0 };
    __v4df y = { 0.1, 0.1, 0.1, 0.1 };
    __v4df z;
    int i;

    z = __builtin_ia32_addpd256(x, y);

    for (i = 0; i < sizeof(x) / sizeof(double); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }
}
