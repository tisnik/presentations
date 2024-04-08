#include <stdio.h>
#include <stdint.h>

int main(void) {
    _Decimal64 x;

    for (x=0.0df; x!=1.0df; x+=0.1df) {
        printf("%f\n", (float)x);
    }
    return 0;
}
