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

    /* ------------------------------------- */
    /* | x3     | x2     | x1     | x0     | */
    /* | y2     | y2     | y1     | y0     | */
    /* | y3..y0 | y3..y0 | x3..x0 | x3..x0 | */
    /* ------------------------------------- */

    z = __builtin_ia32_shufps(x, y, 0);
    print_results(" #   x   y   z", &x, &y, &z);

    z = __builtin_ia32_shufps(x, y, 0b11110000);
    print_results(" #   x   y   z", &x, &y, &z);

    z = __builtin_ia32_shufps(x, y, 0b10100101);
    print_results(" #   x   y   z", &x, &y, &z);
}
