gcc -Wall -ansi -c -fPIC ffi2.c -o ffi2.o

gcc -shared -Wl,-soname,libffi2.so -o libffi2.so ffi2.o

