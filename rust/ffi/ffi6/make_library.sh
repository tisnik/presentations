gcc -Wall -ansi -c -fPIC ffi6.c -o ffi6.o

gcc -shared -Wl,-soname,libffi6.so -o libffi6.so ffi6.o

