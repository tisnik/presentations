#include <stdio.h>
#include <stdint.h>

int main(void) {
    _Decimal128 x;

    for (x=0.0dl; x!=1.0dl; x+=0.1dl) {
        printf("%f\n", (float)x);
    }
    return 0;
}
