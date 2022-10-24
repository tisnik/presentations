#include <stdio.h>
#include <xmmintrin.h>

void print_results(const char *title, __v16qi * x, __v16qi * y,
                   __v16qi * z)
{
    int i;

    puts(title);
    for (i = 0; i < sizeof(*x) / sizeof(char); i++) {
        printf("%2d %2d %2d  %s\n", i, (*x)[i], (*y)[i],
               (*z)[i] == 0 ? "no" : "yes");
    }

    putchar('\n');
}

int main(void)
{
    __v16qi x = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 };
    __v16qi y = { 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8 };
    __v16qi z;

    z = __builtin_ia32_pcmpeqb128(x, y);
    print_results(" #  x  y  x==y?", &x, &y, &z);

    z = __builtin_ia32_pcmpgtb128(x, y);
    print_results(" #  x  y  x>y?", &x, &y, &z);
}
