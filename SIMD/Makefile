CC=gcc
OBJDUMP=objdump

all:	simd04_1.lst simd04_2.lst \
    	simd07_1.lst simd07_2.lst \
    	simd08_1.lst simd08_2.lst \
    	simd12_1.lst simd12_2.lst

clean:
	rm *.lst
	rm *.o

%.lst:	%.o
	objdump -d -M intel -S $< > $@ 

simd04_1.o:	simd04.c
	gcc -c -mno-sse -g -o $@ $<

simd04_2.o:	simd04.c
	gcc -c -g -o $@ $<

simd07_1.o:	simd07.c
	gcc -c -mno-sse -g -o $@ $<

simd07_2.o:	simd07.c
	gcc -c -g -o $@ $<

simd08_1.o:	simd08.c
	gcc -c -mno-sse -g -o $@ $<

simd08_2.o:	simd08.c
	gcc -c -g -o $@ $<

simd12_1.o:	simd12.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd12_2.o:	simd12.c
	gcc -c -O0 -g -o $@ $<
