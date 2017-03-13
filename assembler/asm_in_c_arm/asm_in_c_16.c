#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float x = 100.0f;
float y = -0.1f;
float z = 0.0f;

int main()
{
    printf("%f\n", z);

    __asm__ __volatile__(
        "    vdiv.f32 %[var_z], %[var_x], %[var_y]\n"  /* soucet obou vstupnich operandu */
        : [var_z]"=w" (z)                 /* vystupni operand */
        : [var_x]"w" (x),
          [var_y]"w" (y)                  /* vstupni operandy */
        :                                 /* registry pouzivane uvnitr kodu */
    );

    printf("%f\n", z);

    return 0;
}

