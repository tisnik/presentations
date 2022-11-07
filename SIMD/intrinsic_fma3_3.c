#include <stdio.h>
#include <immintrin.h>
#include <float.h>

void print_results(const char *title, __v4sf * a, __v4sf * b, __v4sf * c,
                   __v4sf * result)
{
    int i;

    puts(title);
    for (i = 0; i < sizeof(*a) / sizeof(float); i++) {
        printf("%2d  %5.2g * %5.2g + %5.2g = %5.2g\n", i, (*a)[i], (*b)[i],
               (*c)[i], (*result)[i]);
    }

    putchar('\n');
}

int main(void)
{
    __v4sf a = { 0.8, 0.9, 1.0, 1.1 };
    __v4sf b = { FLT_MAX, FLT_MAX, FLT_MAX, FLT_MAX };
    __v4sf c = { 0, 0, 0, 0 };;
    __v4sf result;

    result = __builtin_ia32_vfmaddps(a, b, c);
    print_results(" #     a      b       c       result", &a, &b, &c,
                  &result);
}
