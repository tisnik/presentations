#include <stdio.h>

typedef signed char v16ub __attribute__((vector_size(16)));
typedef signed short int v16us __attribute__((vector_size(16)));
typedef signed int v16ui __attribute__((vector_size(16)));
typedef signed long int v16ul __attribute__((vector_size(16)));

int main(void)
{
    printf("signed char:  %ld bytes\n", sizeof(signed char));
    printf("signed short: %ld bytes\n", sizeof(signed short int));
    printf("signed int:   %ld bytes\n", sizeof(signed int));
    printf("signed long:  %ld bytes\n", sizeof(signed long int));

    printf("vector signed char:  %ld bytes\n", sizeof(v16ub));
    printf("vector signed short: %ld bytes\n", sizeof(v16us));
    printf("vector signed int:   %ld bytes\n", sizeof(v16ui));
    printf("vector signed long:  %ld bytes\n", sizeof(v16ul));

    return 0;
}
