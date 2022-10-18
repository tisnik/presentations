#include <stdio.h>

typedef float v16f __attribute__((vector_size(16)));

int main(void)
{
    v16f x = { 1, 2, 3, 4 };
    v16f y = { 0.1, 0.1, 0.1, 0.1 };
    v16f z = x + y;

    int i;

    for (i = 0; i < 4; i++) {
        printf("%d %f\n", i, z[i]);
    }

    return 0;
}
