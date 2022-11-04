#include <stdio.h>

#define sqr(x) x*x

int main(void)
{
    printf("%d\n", sqr(10));
    printf("%d\n", sqr(5 + 5));
    return 0;
}
