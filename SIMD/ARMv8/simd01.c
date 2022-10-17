#include <stdio.h>

typedef unsigned short int v16us __attribute__((vector_size(16)));

int main(void)
{
    printf("scalar: %ld bytes\n", sizeof(unsigned short int));
    printf("vector: %ld bytes\n", sizeof(v16us));

    return 0;
}
