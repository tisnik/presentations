/*
 * Symbolicka jmena operandu
 */
#include <stdio.h>

unsigned long ix = 100;
unsigned long iy = 200;
unsigned long ox;
unsigned long oy;

int main()
{
    printf("%ld\t%ld\n", ix, iy);

    __asm__ __volatile__(
        "mov    r0, %[input1]           \n\t"
        "mov    r1, %[input2]           \n\t"
        "mov    %[output1], r0, lsr #2  \n\t"
        "mov    %[output2], r1, lsr #2  \n\t"
        : [output1] "=r" (ox),  /* vystupni operandy */
          [output2] "=r" (oy)
        : [input1]  "r" (ix),   /* vstupni operandy */
          [input2]  "r" (iy)
        : "r0", "r1"            /* registry pouzivane uvnitr kodu */
    );

    printf("%ld\t%ld\n", ox, oy);

    return 0;
}

