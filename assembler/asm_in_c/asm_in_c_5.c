#include <stdio.h>

unsigned long long result;

int main()
{
    __asm__ __volatile__(
        "mov    $42, %%rbx;   \n\t"
        : "=b" (result)  /* vystupni operand */
        :                /* zadne vstupni operandy */
        :                /* registry pouzivane uvnitr kodu */
    );

    printf("%Ld\n", result);

    return 0;
}

