#include <stdio.h>

int add(int x, int y)
{
    int result;
    result = x;
    result += y;
    return result;
}

int main(int argc, char **argv)
{
    int i = add(10, 20);
    printf("%d\n", i);
    return 0;
}

