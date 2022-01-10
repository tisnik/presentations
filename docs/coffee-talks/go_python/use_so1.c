#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#include "so1.h"

int main()
{
    void *library;
    void (*hello)();

    /* pokus o otevreni a nacteni sdilene knihovny */
    library = dlopen("./so1.so", RTLD_LAZY);
    if (library != NULL) {
        printf("dynamic library loaded: %p\n", library);
    } else {
        puts("unable to load dynamic library");
        return 1;
    }

    hello = dlsym(library, "hello");

    /* pro preklad s --pedantic
    *(void **) (&hello) = dlsym(library, "hello");
    */

    if (hello != NULL) {
        printf("address for 'hello' retrieved: %p\n", (void*)hello);
        puts("Calling 'hello'...");
        hello();
        puts("...called");
    } else {
        puts("unable to retrieve address for 'hello'");
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
