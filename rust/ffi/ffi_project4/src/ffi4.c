#include <stdint.h>
#include <stdio.h>

typedef struct {
    uint8_t a;
    int32_t b;
    uint8_t c;
    int32_t d;
    uint8_t e;
    float   f;
} test_struct;

void print_struct(test_struct s)
{
    printf("sizeof(test_struct) = %lu bytes\n", sizeof(s));
    printf("a = %d\n", s.a);
    printf("b = %d\n", s.b);
    printf("c = %d\n", s.c);
    printf("d = %d\n", s.d);
    printf("e = %d\n", s.e);
    printf("f = %f\n", s.f);
}

