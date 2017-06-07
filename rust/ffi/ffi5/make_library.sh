gcc -Wall -ansi -c -fPIC ffi5.c -o ffi5.o

gcc -shared -Wl,-soname,libffi5.so -o libffi5.so ffi5.o

