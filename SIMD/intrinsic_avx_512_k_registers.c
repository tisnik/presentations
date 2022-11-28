#include <stdio.h>
#include <immintrin.h>

int main(void)
{
    short unsigned int x = 2;
    short unsigned int y = 3;
    short unsigned int z;

    z = __builtin_ia32_kandhi(x, y);
    printf("and: %d\n", z);

    z = __builtin_ia32_kandnhi(x, y);
    printf("and not: %d\n", z);

    z = __builtin_ia32_korhi(x, y);
    printf("or: %d\n", z);

    z = __builtin_ia32_kxorhi(x, y);
    printf("xor: %d\n", z);

    z = __builtin_ia32_kxnorhi(x, y);
    printf("xnor: %d\n", z);

    return 0;
}
