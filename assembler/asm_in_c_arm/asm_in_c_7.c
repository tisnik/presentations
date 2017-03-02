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
        "strb  r2, [r1,#4]    @ prepis jednoho 'o' \n\t"
        "strb  r2, [r1,#7]    @ prepis druheho 'o' \n\t"
        :                         /* zadne vystupni operandy */
        : "m" (message)           /* vstupni operandy */
        : "r1", "r2"              /* registry pouzivane uvnitr kodu */
    );

    puts(message);

    return 0;
}

