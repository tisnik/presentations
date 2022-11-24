#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *c;
    c = (char *) malloc(100 * sizeof(char));

    strcpy(c, "Hello hello Red Hat hello");

    puts(c);

    putchar('\n');

    // "Hello hello Red Hat hello"0
    //  ^           ^
    //  |           |
    //  c           c2
    char *c2 = strstr(c, "Red Hat");
    puts(c2);

    return 0;
}
