#include <stdio.h>

int main(void) {
    _Decimal128 x = 0.1dd;
    _Decimal128 y = 0.2dd;
    _Decimal128 z = 0.3dd;

    puts(x + y == z ? "rovnost" : "nerovnost");
    return 0;
}
