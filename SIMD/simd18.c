#include <stdio.h>

typedef float v16float __attribute__((vector_size(16)));

void add16float(v16float x, v16float y, v16float * z)
{
    *z = x + y;
}

void sub16float(v16float x, v16float y, v16float * z)
{
    *z = x - y;
}

void mul16float(v16float x, v16float y, v16float * z)
{
    *z = x * y;
}

void div16float(v16float x, v16float y, v16float * z)
{
    *z = x / y;
}

void print_vectors(const char *message, const char op, v16float * x,
                   v16float * y, v16float * z)
{
    int i;

    puts(message);
    for (i = 0; i < sizeof(v16float) / sizeof(float); i++) {
        printf("%2d    %5.3f %c %5.3f = %5.3f\n", i, (*x)[i], op, (*y)[i],
               (*z)[i]);
    }

    putchar('\n');
}

int main(void)
{
    v16float x;
    v16float y;
    v16float z;
    int i;

    for (i = 0; i < sizeof(v16float) / sizeof(float); i++) {
        x[i] = i;
        y[i] = i + 0.1;
    }

    add16float(x, y, &z);
    print_vectors("vector addition", '+', &x, &y, &z);

    sub16float(x, y, &z);
    print_vectors("vector subtraction", '-', &x, &y, &z);

    mul16float(x, y, &z);
    print_vectors("vector multiply", '*', &x, &y, &z);

    div16float(x, y, &z);
    print_vectors("vector divide", '/', &x, &y, &z);

    return 0;
}
