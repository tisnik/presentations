#include <stdio.h>

int main(void)
{
    long n = 1;
    float h1 = 0.0, h2 = 0.0;

    while (1) {
        h2 = h1 + 1.0 / (float) n;
        if (n % 1000 == 0) {
            printf("%f %f %10.8f %ld\n", h1, h2, h2 - h1, n);
        }
        if (h1 == h2)
            break;
        h1 = h2;
        n++;
    }
    printf("%f %f %ld\n", h1, h2, n);

    return 0;
}
