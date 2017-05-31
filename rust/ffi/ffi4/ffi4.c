#include <stdint.h>

#include <stdio.h>

int32_t string_length(const char *str)
{
    printf("C side pointer:    %p\n", str);
    int32_t len = 0;
    for (; *str; str++, len++)
        ;
    return len;
}

