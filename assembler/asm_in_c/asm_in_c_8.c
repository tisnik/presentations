#include <stdio.h>

unsigned long long x = 10;
unsigned long long y = 20;
unsigned long long result;

int main ()
{
    __asm__ __volatile__(
        "mov    %%rbx, %%rax;   \n\t"
        "add    %%rcx, %%rax;   \n\t"
        : "=a" (result)    /* vystupni operand */
        : "b" (x), "c" (y) /* dva vstupni operandy v registrech rbx a rcx */
        :                  /* registry pouzivane uvnitr kodu */
    );

    printf("%Ld\n", result);

    return 0;
}

