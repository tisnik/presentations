CC=gcc
OBJDUMP=objdump

all:	simd04_1.lst simd04_2.lst \
    	simd04B_1.lst simd04B_2.lst \
    	simd07_1.lst simd07_2.lst \
    	simd08_1.lst simd08_2.lst \
    	simd12_1.lst simd12_2.lst \
    	simd13_1.lst simd13_2.lst simd13_3.lst simd13_4.lst \
    	simd14_1.lst simd14_2.lst simd14_3.lst simd14_4.lst \
    	simd15_1.lst simd15_2.lst simd15_3.lst simd15_4.lst \
    	simd16_1.lst simd16_2.lst simd16_3.lst simd16_4.lst \
    	simd17_1.lst simd17_2.lst simd17_3.lst simd17_4.lst \
    	simd18_1.lst simd18_2.lst simd18_3.lst simd18_4.lst

clean:
	rm *.lst
	rm *.o

%.lst:	%.o
	objdump -d -M intel -S $< > $@ 

simd04_1.o:	simd04.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd04_2.o:	simd04.c
	gcc -c -O0 -g -o $@ $<

simd04B_1.o:	simd04B.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd04B_2.o:	simd04B.c
	gcc -c -O0 -g -o $@ $<

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

simd13_1.o:	simd13.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd13_2.o:	simd13.c
	gcc -c -O0 -g -o $@ $<

simd13_3.o:	simd13.c
	gcc -c -O3 -mno-sse -g -o $@ $<

simd13_4.o:	simd13.c
	gcc -c -O3 -g -o $@ $<

simd14_1.o:	simd14.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd14_2.o:	simd14.c
	gcc -c -O0 -g -o $@ $<

simd14_3.o:	simd14.c
	gcc -c -O3 -mno-sse -g -o $@ $<

simd14_4.o:	simd14.c
	gcc -c -O3 -g -o $@ $<

simd15_1.o:	simd15.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd15_2.o:	simd15.c
	gcc -c -O0 -g -o $@ $<

simd15_3.o:	simd15.c
	gcc -c -O3 -mno-sse -g -o $@ $<

simd15_4.o:	simd15.c
	gcc -c -O3 -g -o $@ $<

simd16_1.o:	simd16.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd16_2.o:	simd16.c
	gcc -c -O0 -g -o $@ $<

simd16_3.o:	simd16.c
	gcc -c -O3 -mno-sse -g -o $@ $<

simd16_4.o:	simd16.c
	gcc -c -O3 -g -o $@ $<

simd17_1.o:	simd17.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd17_2.o:	simd17.c
	gcc -c -O0 -g -o $@ $<

simd17_3.o:	simd17.c
	gcc -c -O3 -mno-sse -g -o $@ $<

simd17_4.o:	simd17.c
	gcc -c -O3 -g -o $@ $<

simd18_1.o:	simd18.c
	gcc -c -O0 -mno-sse -g -o $@ $<

simd18_2.o:	simd18.c
	gcc -c -O0 -g -o $@ $<

simd18_3.o:	simd18.c
	gcc -c -O3 -mno-sse -g -o $@ $<

simd18_4.o:	simd18.c
	gcc -c -O3 -g -o $@ $<
