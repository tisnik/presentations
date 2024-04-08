#include <stdio.h>

int main(void) {
    _Decimal128 x = 0.1dl;
    _Decimal128 y = 0.2dl;
    _Decimal128 z = 0.3dl;

    puts(x + y == z ? "rovnost" : "nerovnost");
    return 0;
}
