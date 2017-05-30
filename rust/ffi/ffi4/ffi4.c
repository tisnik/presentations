#include <stdio.h>

int string_length(const char *str)
{
    printf("C side pointer:    %p\n", str);
    int len = 0;
    for (; *str; str++, len++)
        ;
    return len;
}

