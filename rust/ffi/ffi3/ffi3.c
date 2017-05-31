#include <stdint.h>

int32_t string_length(const char *str)
{
    int32_t len = 0;
    for (; *str; str++, len++)
        ;
    return len;
}

