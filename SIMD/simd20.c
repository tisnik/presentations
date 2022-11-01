#include <stdio.h>

typedef signed char v32sb __attribute__((vector_size(32)));

void add32sb(v32sb x, v32sb y, v32sb * z)
{
    *z = x + y;
}

typedef signed short v32ss __attribute__((vector_size(32)));

void add32ss(v32ss x, v32ss y, v32ss * z)
{
    *z = x + y;
}

typedef signed int v32si __attribute__((vector_size(32)));

void add32si(v32si x, v32si y, v32si * z)
{
    *z = x + y;
}

typedef signed long int v32sl __attribute__((vector_size(32)));

void add32sl(v32sl x, v32sl y, v32sl * z)
{
    *z = x + y;
}

int main(void)
{
    {
        v32sb x =
            { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
          18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 };
        v32sb y =
            { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
          0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
          0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
};
        v32sb z;

        add32sb(x, y, &z);

        int i;

        puts("vector of signed chars");

        for (i = 0; i < sizeof(v32sb) / sizeof(signed char); i++) {
            printf("%d %d\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v32ss x = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
        v32ss y =
            { 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff,
          0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff,
          0xffff };
        v32ss z;

        add32ss(x, y, &z);

        int i;

        puts("vector of signed short ints");

        for (i = 0; i < sizeof(v32ss) / sizeof(signed short); i++) {
            printf("%d %d\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v32si x = { 0, 1, 2, 3, 4, 5, 6, 7 };
        v32si y =
            { 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff,
          0xffffffff, 0xffffffff, 0xffffffff };
        v32si z;

        add32si(x, y, &z);

        int i;

        puts("vector of signed ints");

        for (i = 0; i < sizeof(v32si) / sizeof(signed int); i++) {
            printf("%d %d\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v32sl x = { 0, 1, 2, 3 };
        v32sl y =
            { 0x7fffffffffffffff, 0x7fffffffffffffff, 0x7fffffffffffffff,
          0x7fffffffffffffff };
        v32sl z;

        add32sl(x, y, &z);

        int i;

        puts("vector of signed longs");

        for (i = 0; i < sizeof(v32sl) / sizeof(signed long); i++) {
            printf("%d %ld\n", i, z[i]);
        }
    }

    return 0;
}
