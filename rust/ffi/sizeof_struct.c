#include <stdint.h>
#include <stdio.h>

typedef struct {
    uint8_t a;
    uint8_t b;
    uint8_t c;
    int32_t d;
    int32_t e;
    float   f;
} test_struct1;

typedef struct __attribute__((__packed__)) {
    uint8_t a;
    uint8_t b;
    uint8_t c;
    int32_t d;
    int32_t e;
    float   f;
} test_struct2;

int main(void)
{
    printf("sizeof(test_struct1) = %lu bytes\n", sizeof(test_struct1));
    printf("sizeof(test_struct2) = %lu bytes\n", sizeof(test_struct2));
    return 0;
}

