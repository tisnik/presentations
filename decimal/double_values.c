#include <stdio.h>
#include <stdint.h>

void print_double_as_hex(double value) {
    union {
        double f;
        uint64_t u;
    } f2u = { .f = value };

    printf("%f -> %016lx\n", value, f2u.u);
}

int main(void) {
    double x = 0.1;
    double y = 0.2;
    double z = 0.3;

    print_double_as_hex(x);
    print_double_as_hex(y);
    print_double_as_hex(z);
    return 0;
}
