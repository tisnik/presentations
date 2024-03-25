#include <stdio.h>

static inline int add1(int x, int y)
{
    int result;

    asm ("add %1, %2\n\t"
         "mov %2, %1"
        : "=r" (result)
        : "r" (x), "r" (y));
    return result;
}

static inline int add2(int x, int y)
{
    int result;

    asm ("add %1, %2"
        : "=r" (result)
        : "r" (x), "0" (y));
    return result;
}

int main(void)
{
    int x1 = add1(1, 2);
    printf("Result#1 = %d\n", x1);

    int x2 = add2(1, 2);
    printf("Result#2 = %d\n", x2);
    return 0;
}

