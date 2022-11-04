#include <stdio.h>
#include <stdlib.h>

union {
    float flt;
    int hex;
} float_hex;

int main(int argc, char **argv)
{
    if (argc == 2) {
        float_hex.flt = atof(argv[1]);
        printf("%08x\n", float_hex.hex);
    }
    return 0;
}
