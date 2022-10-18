#include <stdio.h>

typedef float v16float __attribute__((vector_size(16)));

void add16float(v16float x, v16float y, v16float * z)
{
    *z = x + y;
}

typedef double v16double __attribute__((vector_size(16)));

void add16double(v16double x, v16double y, v16double * z)
{
    *z = x + y;
}

int main(void)
{
    {
        v16float x = { 0, 1, 2, 3 };
        v16float y = { 0.1, 0.1, 0.1, 0.1 };
        v16float z;

        add16float(x, y, &z);

        int i;

        puts("vector of floats");

        for (i = 0; i < sizeof(v16float) / sizeof(float); i++) {
            printf("%d %f\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16double x = { 0, 1 };
        v16double y = { 0.1, 0.1 };
        v16double z;

        add16double(x, y, &z);

        int i;

        puts("vector of doubles");

        for (i = 0; i < sizeof(v16double) / sizeof(double); i++) {
            printf("%d %f\n", i, z[i]);
        }
    }
    return 0;
}
