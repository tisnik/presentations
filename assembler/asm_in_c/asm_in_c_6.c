#include <stdio.h>

unsigned long long x = 10;
unsigned long long y = 20;
unsigned long long result;

int main()
{
    __asm__ __volatile__(
        "mov    %1, %%rbx;   \n\t"
        "add    %2, %%rbx;   \n\t"
        "mov    %%rbx, %%rcx \n\t"
        : "=c" (result)    /* vystupni operand */
        : "r" (x), "r" (y) /* dva vstupni operandy */
        : "%rbx"           /* registry pouzivane uvnitr kodu */
    );

    printf("%Ld\n", result);

    return 0;
}

