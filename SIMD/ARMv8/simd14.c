#include <stdio.h>

typedef signed char v16ib __attribute__((vector_size(16)));

void add16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x + y;
}

typedef signed short v16is __attribute__((vector_size(16)));

void add16is(v16is x, v16is y, v16is * z)
{
    *z = x + y;
}

typedef signed int v16ii __attribute__((vector_size(16)));

void add16ii(v16ii x, v16ii y, v16ii * z)
{
    *z = x + y;
}

typedef signed long int v16il __attribute__((vector_size(16)));

void add16il(v16il x, v16il y, v16il * z)
{
    *z = x + y;
}

int main(void)
{
    {
        v16ib x = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
        v16ib y =
            { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        };
        v16ib z;

        add16ib(x, y, &z);

        int i;

        puts("vector of signed chars");

        for (i = 0; i < sizeof(v16ib) / sizeof(signed char); i++) {
            printf("%d %d\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16is x = { 0, 1, 2, 3, 4, 5, 6, 7 };
        v16is y = { 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff,
            0xffff
        };
        v16is z;

        add16is(x, y, &z);

        int i;

        puts("vector of signed short ints");

        for (i = 0; i < sizeof(v16is) / sizeof(signed short); i++) {
            printf("%d %d\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16ii x = { 0, 1, 2, 3 };
        v16ii y = { 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff };
        v16ii z;

        add16ii(x, y, &z);

        int i;

        puts("vector of signed ints");

        for (i = 0; i < sizeof(v16ii) / sizeof(signed int); i++) {
            printf("%d %d\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16il x = { 0, 1 };
        v16il y = { 0xffffffffffffffff, 0xffffffffffffffff };
        v16il z;

        add16il(x, y, &z);

        int i;

        puts("vector of signed longs");

        for (i = 0; i < sizeof(v16il) / sizeof(signed long); i++) {
            printf("%d %ld\n", i, z[i]);
        }
    }

    return 0;
}
