#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
        char *age_str;

        argument = argv[i];
        if (startswith("-name=", argument)) {
            int from;

            printf("Found name in argument '%s'\n", argument);

            from = strlen("-name=");
            name = argument + from;

            printf("Hello %s!\n", name);
        }
        if (startswith("-age=", argument)) {
            int from;

            printf("Found age in argument '%s'\n", argument);

            from = strlen("-age=");
            age_str = argument + from;

            int age = atoi(age_str);

            if (age < 18) {
                printf("Forbidden\n");
            } else {
                printf("ok\n");
            }
            printf("Age %d!\n", age);
        }
    }

    return 0;
}
