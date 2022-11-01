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
    	simd18_1.lst simd18_2.lst simd18_3.lst simd18_4.lst \
	simd19_sse.lst simd19_avx.lst simd19_avx2.lst \
	simd20_sse.lst simd20_avx.lst simd20_avx2.lst \
	simd21_sse.lst simd21_avx.lst simd21_avx2.lst \
	intrinsic_mmx_1.lst \
	intrinsic_mmx_2.lst \
	intrinsic_mmx_3.lst \
	intrinsic_mmx_4.lst \
	intrinsic_mmx_5.lst \
	intrinsic_sse_1.lst \
	intrinsic_sse_2.lst \
	intrinsic_sse_3.lst \
	intrinsic_sse_4.lst \
	intrinsic_sse_5.lst \
	intrinsic_sse_6.lst \
	intrinsic_sse_7.lst \
	intrinsic_sse_8.lst \
	intrinsic_sse_9.lst \
	intrinsic_sse_A.lst \
	intrinsic_sse_B.lst

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

simd19_sse.o:	simd19.c
	gcc -c -O0 -msse -mno-avx -g -o $@ $<

simd19_avx.o:	simd19.c
	gcc -c -O0 -mavx -g -o $@ $<

simd19_avx2.o:	simd19.c
	gcc -c -O0 -mavx2 -g -o $@ $<

simd20_sse.o:	simd20.c
	gcc -c -O0 -msse -mno-avx -g -o $@ $<

simd20_avx.o:	simd20.c
	gcc -c -O0 -mavx -g -o $@ $<

simd20_avx2.o:	simd20.c
	gcc -c -O0 -mavx2 -g -o $@ $<

simd21_sse.o:	simd21.c
	gcc -c -O0 -msse -mno-avx -g -o $@ $<

simd21_avx.o:	simd21.c
	gcc -c -O0 -mavx -g -o $@ $<

simd21_avx2.o:	simd21.c
	gcc -c -O0 -mavx2 -g -o $@ $<

intrinsic_mmx_1.o:	intrinsic_mmx_1.c
	gcc -c -O0 -g -o $@ $<

intrinsic_mmx_2.o:	intrinsic_mmx_2.c
	gcc -c -O0 -g -o $@ $<

intrinsic_mmx_3.o:	intrinsic_mmx_3.c
	gcc -c -O0 -g -o $@ $<

intrinsic_mmx_4.o:	intrinsic_mmx_4.c
	gcc -c -O0 -g -o $@ $<

intrinsic_mmx_5.o:	intrinsic_mmx_5.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_1.o:	intrinsic_sse_1.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_2.o:	intrinsic_sse_2.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_3.o:	intrinsic_sse_3.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_4.o:	intrinsic_sse_4.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_5.o:	intrinsic_sse_5.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_6.o:	intrinsic_sse_6.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_7.o:	intrinsic_sse_7.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_8.o:	intrinsic_sse_8.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_9.o:	intrinsic_sse_9.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_A.o:	intrinsic_sse_A.c
	gcc -c -O0 -g -o $@ $<

intrinsic_sse_B.o:	intrinsic_sse_B.c
	gcc -c -O0 -g -o $@ $<

intrinsic_avx_1.o:	intrinsic_avx_1.c
	gcc -c -mavx -O0 -g -o $@ $<

intrinsic_avx_2.o:	intrinsic_avx_2.c
	gcc -c -mavx -O0 -g -o $@ $<

intrinsic_avx_3.o:	intrinsic_avx_3.c
	gcc -c -mavx -O0 -g -o $@ $<
