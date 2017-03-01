#include <stdio.h>

unsigned long long x = 10;
unsigned long long y = 20;
unsigned long long result;

int main()
{
    __asm__ __volatile__(
        "add    rax, rbx;   \n\t"
        : "=a" (result)    /* vystupni operand */
        : "a" (x), "b" (y) /* dva vstupni operandy v registrech rax a rbx */
        :                  /* registry pouzivane uvnitr kodu */
    );

    printf("%Ld\n", result);

    return 0;
}

