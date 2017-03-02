#include <stdio.h>

const char *message = "Hello world!";

int main()
{
    __asm__ __volatile__(
        "mov   r7, #4         @ cislo syscallu pro funkci write  \n\t"
        "mov   r0, #1         @ standardni vystup  \n\t"
        "ldr   r1, %0         @ adresa retezce, ktery se ma vytisknout  \n\t"
        "mov   r2, #12        @ pocet znaku, ktere se maji vytisknout  \n\t"
        "svc   0              @ volani Linuxoveho kernelu  \n\t"
        :                        /* zadne vystupni operandy */
        : "m" (message)          /* zadne vstupni operandy */
        : "r0", "r1", "r2", "r7" /* registry pouzivane uvnitr kodu */
    );

    return 0;
}

