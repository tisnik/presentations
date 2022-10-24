#include <stdio.h>
#include <xmmintrin.h>

void print_results(const char *title, __v4sf * x, __v4sf * y, __v4sf * z)
{
    int i;

    puts(title);
    for (i = 0; i < sizeof(*x) / sizeof(float); i++) {
        printf("%2d  %3.1f  %3.1f  %s\n", i, (*x)[i], (*y)[i],
               (*z)[i] == 0 ? "no" : "yes");
    }

    putchar('\n');
}

int main(void)
{
    __v4sf x = { 1, 2.5, 2.5, 4 };
    __v4sf y = { 2.5, 2.5, 2.5, 2.5 };
    __v4sf z;

    z = __builtin_ia32_cmpeqps(x, y);
    print_results(" #  x    y    x==y?", &x, &y, &z);

    z = __builtin_ia32_cmpgtps(x, y);
    print_results(" #  x    y    x>y?", &x, &y, &z);

    z = __builtin_ia32_cmpltps(x, y);
    print_results(" #  x    y    x<y?", &x, &y, &z);

    z = __builtin_ia32_cmpgeps(x, y);
    print_results(" #  x    y    x>=y?", &x, &y, &z);

    z = __builtin_ia32_cmpleps(x, y);
    print_results(" #  x    y    x<=y?", &x, &y, &z);

    z = __builtin_ia32_cmpneqps(x, y);
    print_results(" #  x    y    x!=y?", &x, &y, &z);
}
