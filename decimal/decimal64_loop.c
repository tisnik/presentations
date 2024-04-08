#include <stdio.h>
#include <stdint.h>

int main(void) {
    _Decimal64 x;

    for (x=0.0dd; x!=1.0dd; x+=0.1dd) {
        printf("%f\n", (float)x);
    }
    return 0;
}
