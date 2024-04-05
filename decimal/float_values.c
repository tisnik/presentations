#include <stdio.h>
#include <stdint.h>

void print_float_as_hex(float value) {
    union {
        float f;
        uint32_t u;
    } f2u = { .f = value };

    printf("%f -> %08x\n", value, f2u.u);
}

int main(void) {
    float x = 0.1;
    float y = 0.2;
    float z = 0.3;

    print_float_as_hex(x);
    print_float_as_hex(y);
    print_float_as_hex(z);
    return 0;
}
