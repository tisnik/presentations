#include <stdio.h>

typedef signed char v16ib __attribute__((vector_size(16)));

void add16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x + y;
}

void sub16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x - y;
}

void mul16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x * y;
}

void div16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x / y;
}

void mod16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x % y;
}

void and16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x & y;
}

void or16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x | y;
}

void xor16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x ^ y;
}

void rshift16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x >> y;
}

void lshift16ib(v16ib x, v16ib y, v16ib * z)
{
    *z = x << y;
}

void print_vectors(const char *message, const char *op, v16ib * x,
                   v16ib * y, v16ib * z)
{
    int i;

    puts(message);
    for (i = 0; i < sizeof(v16ib) / sizeof(signed char); i++) {
        printf("%2d    %d %s %d = %d\n", i, (*x)[i], op, (*y)[i], (*z)[i]);
    }

    putchar('\n');
}

int main(void)
{
    v16ib x;
    v16ib y;
    v16ib z;
    int i;

    for (i = 0; i < sizeof(v16ib) / sizeof(signed char); i++) {
        x[i] = i * 2;
        y[i] = 16 - i;
    }

    add16ib(x, y, &z);
    print_vectors("vector addition", "+", &x, &y, &z);

    sub16ib(x, y, &z);
    print_vectors("vector subtraction", "-", &x, &y, &z);

    mul16ib(x, y, &z);
    print_vectors("vector multiply", "*", &x, &y, &z);

    div16ib(x, y, &z);
    print_vectors("vector divide", "/", &x, &y, &z);

    mod16ib(x, y, &z);
    print_vectors("vector modulo", "%", &x, &y, &z);

    and16ib(x, y, &z);
    print_vectors("vector bitwise and", "&", &x, &y, &z);

    or16ib(x, y, &z);
    print_vectors("vector bitwise or", "|", &x, &y, &z);

    xor16ib(x, y, &z);
    print_vectors("vector bitwise xor", "^", &x, &y, &z);

    rshift16ib(x, y, &z);
    print_vectors("vector right shift", ">>", &x, &y, &z);

    lshift16ib(x, y, &z);
    print_vectors("vector left shift", "<<", &x, &y, &z);

    return 0;
}
