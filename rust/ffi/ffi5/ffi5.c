#include <stdint.h>

#include <stdio.h>

float sum(uint32_t len, const float *array)
{
    float s = 0.0f;
    int i;
    for (i=0; i < len; i++) {
        s += array[i];
    }
    return s;
}

