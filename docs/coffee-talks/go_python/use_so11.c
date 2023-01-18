#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#include "so11.h"

int main()
{
    void *library;
    double (*length)(struct Vector v);

    /* pokus o otevreni a nacteni sdilene knihovny */
    library = dlopen("./so11.so", RTLD_LAZY);
    if (library != NULL) {
        printf("dynamic library loaded: %p\n", library);
    } else {
        puts("unable to load dynamic library");
        return 1;
    }

    length = dlsym(library, "length");

    if (length != NULL) {
        struct Vector v;
        v.X = 1.0;
        v.Y = 1.0;
        double ret;
        printf("address for 'length' retrieved: %p\n", (void *) length);
        puts("Calling 'length'...");
        ret = length(v);
        printf("...called, vector length: %f\n", ret);
    } else {
        puts("unable to retrieve address for 'length'");
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
