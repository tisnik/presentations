#include <stdio.h>
#include <inttypes.h>

typedef union {
    float f;
    uint32_t i;
} bfloat16mock;

int main(void)
{
    long n = 1;
    bfloat16mock h1;
    bfloat16mock h2;

    h1.f = 0.0;
    h2.f = 0.0;

    while (1) {
        h2.f = h1.f + 1.0 / (float) n;
        h2.i &= 0xffff0000;
        printf("%f %f %10.8lf %ld\n", h1.f, h2.f, h2.f - h1.f, n);
        if (h1.f == h2.f)
            break;
        h1 = h2;
        n++;
    }
    printf("%f %f %ld\n", h1.f, h2.f, n);

    return 0;
}
