#include <stdio.h>
#include <string.h>

int startswith(char *prefix, char *str) {
    return strncmp(prefix, str, strlen(prefix)) == 0;
}

int main(int argc, char *argv[]) {
    int i;

    printf("Arguments count: %d\n", argc);

    for (i = 0; i < argc; i++) {
        char *argument;

        argument = argv[i];
        printf("Testing argument '%s'\n", argument);

        if (startswith("-name=", argument)) {
            printf("Found name in argument '%s'\n", argument);
        }
    }

    return 0;
}
