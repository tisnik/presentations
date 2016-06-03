#include <stdio.h>

typedef struct
{
    int   x;
    float y;
    char  z;
} s_x;

s_x var_x = {42, 3.1415, '@'};

int array1[100];

int main(int argc, char **argv)
{
    int i;
    for (i=0; i<100; i++) {
        array1[i] = i*i;
    }
    return 0;
}

