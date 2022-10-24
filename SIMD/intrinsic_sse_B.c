#include <stdio.h>
#include <xmmintrin.h>

void print_results(const char *title, __v4sf * x, __v4sf * y, __v4sf * z)
{
    int i;

    puts(title);
    for (i = 0; i < sizeof(*x) / sizeof(float); i++) {
        printf("%2d  %2.0f  %2.0f  %2.0f\n", i, (*x)[i], (*y)[i], (*z)[i]);
    }

    putchar('\n');
}

int main(void)
{
    __v4sf x = { 1, 2, 3, 4 };
    __v4sf y = { 6, 7, 8, 9 };
    __v4sf z;

    z = __builtin_ia32_unpckhps(x, y);
    print_results(" #   x   y   z", &x, &y, &z);

    z = __builtin_ia32_unpcklps(x, y);
    print_results(" #   x   y   z", &x, &y, &z);
}
