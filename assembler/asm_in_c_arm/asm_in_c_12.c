#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float x = 0.5f;
float y = 1.0f;
float z = 1000.0f;

int main()
{
    printf("%f\n", z);

    __asm__ __volatile__(
        "    mov %0, %1\n"    /* presunuti prvniho vstupniho operandu na vystup */
        : "=r" (z)            /* vystupni operand */
        : "r" (x), "r" (y)    /* vstupni operandy */
        :                     /* registry pouzivane uvnitr kodu */
    );

    printf("%f\n", z);

    return 0;
}

