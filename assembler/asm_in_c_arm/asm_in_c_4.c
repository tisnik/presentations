#include <stdio.h>

unsigned long x = 10;
unsigned long y = 20;

int main()
{
    printf("%ld\t%ld\n", x, y);

    __asm__ __volatile__(
        "mov    r0, #42          \n\t"
        "mov    r1, r0, lsl #1   \n\t"
        "mov    %0, r0           \n\t"
        "mov    %1, r1           \n\t"
        : "=r" (x), "=r" (y)  /* vystupni operandy */
        :                     /* zadne vstupni operandy */
        : "r0", "r1"          /* registry pouzivane uvnitr kodu */
    );

    printf("%ld\t%ld\n", x, y);

    return 0;
}

