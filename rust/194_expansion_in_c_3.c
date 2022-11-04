#include <stdio.h>

#define sqr(x) (x)*(x)

int getx(void)
{
    puts("getx() called");
    return 2;
}

int main(void)
{
    printf("%d\n", sqr(getx()));

    return 0;
}
