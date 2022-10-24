#include <stdio.h>

typedef signed char v16ub __attribute__((vector_size(16)));
typedef signed short int v16us __attribute__((vector_size(16)));
typedef signed int v16ui __attribute__((vector_size(16)));
typedef signed long int v16ul __attribute__((vector_size(16)));

int main(void)
{
    {
        v16ub x = { 1, 2, 3, 4, 5, 6, 7, 8 };
        v16ub y = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff };
        v16ub z = x + y;
    }

    {
        v16us x = { 1, 2, 3, 4, 5, 6, 7, 8 };
        v16us y = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff };
        v16us z = x + y;
    }

    {
        v16ui x = { 1, 2, 3, 4 };
        v16ui y = { 0xff, 0xff, 0xff, 0xff };
        v16ui z = x + y;
    }

    {
        v16ul x = { 1, 2 };
        v16ul y = { 0xff, 0xff };
        v16ul z = x + y;
    }


    return 0;
}
