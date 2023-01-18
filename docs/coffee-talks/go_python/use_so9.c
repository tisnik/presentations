#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#include "so9.h"

int main()
{
    void *library;
    GoInt64(*sum) (int *values, GoInt length);

    /* pokus o otevreni a nacteni sdilene knihovny */
    library = dlopen("./so9.so", RTLD_LAZY);
    if (library != NULL) {
        printf("dynamic library loaded: %p\n", library);
    } else {
        puts("unable to load dynamic library");
        return 1;
    }

    sum = dlsym(library, "sum");

    if (sum != NULL) {
        int ret;
        int input[] = { 1, 2, 3, 4 };
        printf("address for 'sum' retrieved: %p\n", (void *) sum);
        puts("Calling 'sum'...");
        ret = sum(input, sizeof(input) / sizeof(int));
        printf("...called, return value: %d\n", ret);
    } else {
        puts("unable to retrieve address for 'sum'");
    }


    /* pokus o uzavreni sdilene knihovny */
    if (library != NULL) {
        int err = dlclose(library);
        if (err != 0) {
            puts("unable to close dynamic library");
            return 1;
        } else {
            puts("dynamic library closed");
        }
    }

    return EXIT_SUCCESS;
}
