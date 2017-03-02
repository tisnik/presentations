#include <stdio.h>

unsigned long ix = 100;
unsigned long iy = 200;
unsigned long ox;
unsigned long oy;

int main()
{
    printf("%ld\t%ld\n", ix, iy);

    __asm__ __volatile__(
        "mov    r0, %2          \n\t"
        "mov    r1, %3          \n\t"
        "mov    %0, r0, lsr #2  \n\t"
        "mov    %1, r1, lsr #2  \n\t"
        : "=r" (ox), "=r" (oy)  /* vystupni operandy */
        : "r" (ix),  "r" (iy)   /* vstupni operandy */
        : "r0", "r1"            /* registry pouzivane uvnitr kodu */
    );

    printf("%ld\t%ld\n", ox, oy);

    return 0;
}

