#include <stdio.h>

typedef unsigned char v32ub __attribute__((vector_size(32)));

void add32ub(v32ub x, v32ub y, v32ub * z)
{
    *z = x + y;
}

typedef unsigned short v32us __attribute__((vector_size(32)));

void add32us(v32us x, v32us y, v32us * z)
{
    *z = x + y;
}

typedef unsigned int v32ui __attribute__((vector_size(32)));

void add32ui(v32ui x, v32ui y, v32ui * z)
{
    *z = x + y;
}

typedef unsigned long int v32ul __attribute__((vector_size(32)));

void add32ul(v32ul x, v32ul y, v32ul * z)
{
    *z = x + y;
}

int main(void)
{
    {
        v32ub x =
            { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
        };
        v32ub y =
            { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                0xff,
        };
        v32ub z;

        add32ub(x, y, &z);

        int i;

        puts("vector of unsigned chars");

        for (i = 0; i < sizeof(v32ub) / sizeof(unsigned char); i++) {
            printf("%d %u\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v32us x = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
        v32us y = { 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff,
            0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff,
            0xffff
        };
        v32us z;

        add32us(x, y, &z);

        int i;

        puts("vector of unsigned short ints");

        for (i = 0; i < sizeof(v32us) / sizeof(unsigned short); i++) {
            printf("%d %u\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v32ui x = { 0, 1, 2, 3, 4, 5, 6, 7 };
        v32ui y =
            { 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff,
            0xffffffff, 0xffffffff, 0xffffffff
        };
        v32ui z;

        add32ui(x, y, &z);

        int i;

        puts("vector of unsigned ints");

        for (i = 0; i < sizeof(v32ui) / sizeof(unsigned int); i++) {
            printf("%d %u\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v32ul x = { 0, 1, 2, 3 };
        v32ul y =
            { 0xffffffffffffffff, 0xffffffffffffffff, 0xffffffffffffffff,
            0xffffffffffffffff
        };
        v32ul z;

        add32ul(x, y, &z);

        int i;

        puts("vector of unsigned longs");

        for (i = 0; i < sizeof(v32ul) / sizeof(unsigned long); i++) {
            printf("%d %lu\n", i, z[i]);
        }
    }

    return 0;
}
