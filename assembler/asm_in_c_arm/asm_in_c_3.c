#include <stdio.h>

unsigned long result;

int main()
{
    __asm__ __volatile__(
        "mov    r0, #42    \n\t"
        "mov    %0, r0     \n\t"
        : "=r" (result)  /* vystupni operand */
        :                /* zadne vstupni operandy */
        : "r0"           /* registry pouzivane uvnitr kodu */
    );

    printf("%ld\n", result);

    return 0;
}

