#include <stdio.h>
#include <xmmintrin.h>

int main(void)
{
    __v2df x = { 1.0, 2.0 };
    __v2df y = { 0.1, 0.1 };
    __v2df z;
    int i;

    z = __builtin_ia32_addpd(x, y);

    for (i = 0; i < sizeof(x) / sizeof(double); i++) {
        printf("%2d %lf %lf %lf\n", i, x[i], y[i], z[i]);
    }
}
