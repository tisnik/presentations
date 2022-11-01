#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    __v8sf x = { 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 };
    __v8sf y = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
    __v8sf z;
    int i;

    z = __builtin_ia32_addps256(x, y);

    for (i = 0; i < sizeof(x) / sizeof(float); i++) {
        printf("%2d %f %f %f\n", i, x[i], y[i], z[i]);
    }
}
