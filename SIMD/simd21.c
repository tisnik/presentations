#include <stdio.h>

typedef float v32float __attribute__((vector_size(32)));

void add32float(v32float x, v32float y, v32float * z)
{
    *z = x + y;
}

typedef double v32double __attribute__((vector_size(32)));

void add32double(v32double x, v32double y, v32double * z)
{
    *z = x + y;
}

int main(void)
{
    {
        v32float x = { 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 };
        v32float y = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        v32float z;
        int i;

        add32float(x, y, &z);

        puts("vector of floats");

        for (i = 0; i < sizeof(v32float) / sizeof(float); i++) {
            printf("%d     %f + %f = %f\n", i, x[i], y[i], z[i]);
        }
    }

    putchar('\n');

    {
        v32double x = { 1.0, 2.0, 3.0, 4.0 };
        v32double y = { 0.5, 0.5, 0.5, 0.5 };
        v32double z;
        int i;

        add32double(x, y, &z);

        puts("vector of doubles");

        for (i = 0; i < sizeof(v32double) / sizeof(double); i++) {
            printf("%d     %f + %f = %f\n", i, x[i], y[i], z[i]);
        }
    }


    return 0;
}
