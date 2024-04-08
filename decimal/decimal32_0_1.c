#include <stdio.h>

int main(void) {
    _Decimal32 x = 0.1df;
    _Decimal32 y = 0.2df;
    _Decimal32 z = 0.3df;

    puts(x + y == z ? "rovnost" : "nerovnost");
    return 0;
}
