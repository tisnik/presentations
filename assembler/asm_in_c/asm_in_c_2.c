#include <stdio.h>

int main()
{
    __asm__ __volatile__(
        "nop   \n\t"
    );

    return 0;
}

