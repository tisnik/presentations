#include <stdio.h>

int main(int argc, char *argv[]) {
    int i;

    printf("Arguments count: %d\n", argc);

    for (i = 0; i < argc; i++) {
        printf("Argument #%d is '%s'\n", i, argv[i]);
    }

    return 0;
}
