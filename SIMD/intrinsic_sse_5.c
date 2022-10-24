#include <stdio.h>
#include <xmmintrin.h>

int main(void)
{
    __v4sf x = { 1.0, 2.0, 3.0, 4.0 };
    __v4sf y = { 0.1, 0.1, 0.1, 0.1 };
    __v4sf z;
    int i;

    z = __builtin_ia32_addps(x, y);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }
}
