#include <stdio.h>

typedef unsigned char v16ub __attribute__((vector_size(16)));

void add16ub(v16ub x, v16ub y, v16ub * z)
{
    *z = x + y;
}

typedef unsigned short v16us __attribute__((vector_size(16)));

void add16us(v16us x, v16us y, v16us * z)
{
    *z = x + y;
}

typedef unsigned int v16ui __attribute__((vector_size(16)));

void add16ui(v16ui x, v16ui y, v16ui * z)
{
    *z = x + y;
}

typedef unsigned long int v16ul __attribute__((vector_size(16)));

void add16ul(v16ul x, v16ul y, v16ul * z)
{
    *z = x + y;
}

int main(void)
{
    {
        v16ub x = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
        v16ub y =
            { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        };
        v16ub z;

        add16ub(x, y, &z);

        int i;

        puts("vector of unsigned chars");

        for (i = 0; i < sizeof(v16ub) / sizeof(unsigned char); i++) {
            printf("%d %u\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16us x = { 0, 1, 2, 3, 4, 5, 6, 7 };
        v16us y = { 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff, 0xffff,
            0xffff
        };
        v16us z;

        add16us(x, y, &z);

        int i;

        puts("vector of unsigned short ints");

        for (i = 0; i < sizeof(v16us) / sizeof(unsigned short); i++) {
            printf("%d %u\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16ui x = { 0, 1, 2, 3 };
        v16ui y = { 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff };
        v16ui z;

        add16ui(x, y, &z);

        int i;

        puts("vector of unsigned ints");

        for (i = 0; i < sizeof(v16ui) / sizeof(unsigned int); i++) {
            printf("%d %u\n", i, z[i]);
        }
    }

    putchar('\n');

    {
        v16ul x = { 0, 1 };
        v16ul y = { 0xffffffffffffffff, 0xffffffffffffffff };
        v16ul z;

        add16ul(x, y, &z);

        int i;

        puts("vector of unsigned longs");

        for (i = 0; i < sizeof(v16ul) / sizeof(unsigned long); i++) {
            printf("%d %lu\n", i, z[i]);
        }
    }

    return 0;
}
