#include <stdio.h>
#include <stdint.h>

int main(void) {
    double x;

    for (x=0.0; x!=1.0; x+=0.1) {
        printf("%f\n", x);
    }
    return 0;
}