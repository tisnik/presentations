#include <stdio.h>

int main(void) {
    _Decimal64 x = 0.1dd;
    _Decimal64 y = 0.2dd;
    _Decimal64 z = 0.3dd;

    puts(x + y == z ? "rovnost" : "nerovnost");
    return 0;
}
