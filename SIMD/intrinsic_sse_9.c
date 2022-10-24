#include <stdio.h>
#include <xmmintrin.h>

void print_results(const char *title, __v4sf * x, __v4sf * y)
{
    int i;

    puts(title);
    for (i = 0; i < sizeof(*x) / sizeof(float); i++) {
        printf("%2d  %5.2f  %3.1f\n", i, (*x)[i], (*y)[i]);
    }

    putchar('\n');
}

int main(void)
{
    __v4sf x = { 1, 2, 4, 10 };
    __v4sf y;

    y = __builtin_ia32_rcpps(x);
    print_results(" #   x     1/x", &x, &y);

    y = __builtin_ia32_sqrtps(x);
    print_results(" #   x     sqrt(x)", &x, &y);

    y = __builtin_ia32_rsqrtps(x);
    print_results(" #   x     1/sqrt(x)", &x, &y);
}
