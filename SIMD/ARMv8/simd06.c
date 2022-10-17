#include <stdio.h>

typedef float v16f __attribute__((vector_size(16)));
typedef double v16d __attribute__((vector_size(16)));

int main(void)
{
    printf("scalar float:  %ld bytes\n", sizeof(float));
    printf("vector float:  %ld bytes\n", sizeof(v16f));

    printf("scalar double: %ld bytes\n", sizeof(double));
    printf("vector double: %ld bytes\n", sizeof(v16d));

    return 0;
}
