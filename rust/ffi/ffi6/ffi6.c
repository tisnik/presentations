#include <stdint.h>

#include <stdio.h>

float sum(uint32_t len, float *array)
{
    float s = 0.0f;
    int i;
    for (i=0; i < len; i++) {
        s += array[i];
        array[i] = 0.0f;
    }
    return s;
}

