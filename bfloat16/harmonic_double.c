#include <stdio.h>

int main(void)
{
    long n = 1;
    double h1 = 0.0, h2 = 0.0;

    while (1) {
        h2 = h1 + 1.0 / (double) n;
        if (n % 10000000 == 0) {
            printf("%lf %lf %20.18lf %ld\n", h1, h2, h2 - h1, n);
        }
        if (h1 == h2)
            break;
        h1 = h2;
        n++;
    }
    printf("%lf %lf %ld\n", h1, h2, n);

    return 0;
}
