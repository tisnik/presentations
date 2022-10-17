#include <stdio.h>

typedef unsigned char v16ub __attribute__((vector_size(16)));
typedef unsigned short int v16us __attribute__((vector_size(16)));
typedef unsigned int v16ui __attribute__((vector_size(16)));
typedef unsigned long int v16ul __attribute__((vector_size(16)));

int main(void)
{
    printf("unsigned char:  %ld bytes\n", sizeof(unsigned char));
    printf("unsigned short: %ld bytes\n", sizeof(unsigned short int));
    printf("unsigned int:   %ld bytes\n", sizeof(unsigned int));
    printf("unsigned long:  %ld bytes\n", sizeof(unsigned long int));

    printf("vector unsigned char:  %ld bytes\n", sizeof(v16ub));
    printf("vector unsigned short: %ld bytes\n", sizeof(v16us));
    printf("vector unsigned int:   %ld bytes\n", sizeof(v16ui));
    printf("vector unsigned long:  %ld bytes\n", sizeof(v16ul));

    return 0;
}
