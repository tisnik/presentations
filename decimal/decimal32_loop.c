#include <stdio.h>

int main(void) {
    _Decimal32 x;

    for (x=0.0df; x!=1.0df; x+=0.1df) {
        printf("%f\n", (float)x);
    }
    return 0;
}
