#include <stdio.h>
#include <immintrin.h>

void print_results(const char *title, __v4sf * a, __v4sf * b, __v4sf * c,
                   __v4sf * result)
{
    int i;

    puts(title);
    for (i = 0; i < sizeof(*a) / sizeof(float); i++) {
        printf("%2d  -%1.0f * %1.0f + %1.0f = %1.0f\n", i, (*a)[i],
               (*b)[i], (*c)[i], (*result)[i]);
    }

    putchar('\n');
}

int main(void)
{
    __v4sf a = { 1, 2, 3, 4 };
    __v4sf b = { 2, 2, 2, 2 };
    __v4sf c = { 1, 1, 1, 1 };;
    __v4sf result;

    result = __builtin_ia32_vfnmaddps(a, b, c);
    print_results(" #   a   b   c   result", &a, &b, &c, &result);
}
