#include <stdio.h>

int main(void)
{
    double values[] = {0.0, 0.1, 0.2, 1.0, 2.0, 10.0, 100.0, 1000.0, 1000.1, 1.0/0.0, -0.0, -0.1, -0.2, -1.0, -1000.0, -1.0/0.0, 0.0/0.0};
    int i;

    for (i=0; i<sizeof(values)/sizeof(double); i++) {
        printf("%9.4f   %a\n", values[i], values[i]);
    }

    return 0;
}
