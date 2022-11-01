#include <stdio.h>
#include <string.h>

int startswith(char *prefix, char *str)
{
    return strncmp(prefix, str, strlen(prefix)) == 0;
}

int main(int argc, char *argv[])
{
    int i;

    printf("Arguments count: %d\n", argc);

    for (i = 0; i < argc; i++) {
        char *argument;
        char *name;

        argument = argv[i];
        if (startswith("-name=", argument)) {
            int from;

            printf("Found name in argument '%s'\n", argument);

            from = strlen("-name=");
            name = argument + from;

            printf("Hello %s!\n", name);
        }
    }

    return 0;
}
