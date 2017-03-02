#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *message = NULL;

int main()
{
    message = (char*) malloc(20);
    strcpy(message, "Hello world!");

    puts(message);

    __asm__ __volatile__(
        "ldr   r1, %0         @ adresa retezce  \n\t"
        "mov   r2, #'*'       @ zapisovany znak \n\t"
        "mov   r3, #2         @ pocitadlo smycky \n\t"
        "\n"
        "loop:\n\t"
        "strb  r2, [r1,r3]    @ prepis jednoho znaku \n\t"
        "add   r3, r3, #2     @ zvyseni hodnoty pocitadla \n\t"
        "cmp   r3, #12        @ porovnani s ocekavanou koncovou hodnotou \n\t"
        "bne  loop            @ podmineny skok na zacatek smycky \n\t"
        :                         /* zadne vystupni operandy */
        : "m" (message)           /* vstupni operandy */
        : "r1", "r2", "r3"        /* registry pouzivane uvnitr kodu */
    );

    puts(message);

    return 0;
}

