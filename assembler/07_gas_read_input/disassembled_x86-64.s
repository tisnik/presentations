
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000064  00000000004000b0  00000000004000b0  000000b0  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .data         00000017  0000000000600114  0000000000600114  00000114  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000038  0000000000600130  0000000000600130  0000012b  2**3
                  ALLOC
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	b8 04 00 00 00       	mov    eax,0x4
  4000b5:	bb 01 00 00 00       	mov    ebx,0x1
  4000ba:	b9 14 01 60 00       	mov    ecx,0x600114
  4000bf:	ba 11 00 00 00       	mov    edx,0x11
  4000c4:	cd 80                	int    0x80
  4000c6:	b8 03 00 00 00       	mov    eax,0x3
  4000cb:	bb 00 00 00 00       	mov    ebx,0x0
  4000d0:	b9 30 01 60 00       	mov    ecx,0x600130
  4000d5:	ba 32 00 00 00       	mov    edx,0x32
  4000da:	cd 80                	int    0x80
  4000dc:	b8 04 00 00 00       	mov    eax,0x4
  4000e1:	bb 01 00 00 00       	mov    ebx,0x1
  4000e6:	b9 25 01 60 00       	mov    ecx,0x600125
  4000eb:	ba 06 00 00 00       	mov    edx,0x6
  4000f0:	cd 80                	int    0x80
  4000f2:	b8 04 00 00 00       	mov    eax,0x4
  4000f7:	bb 01 00 00 00       	mov    ebx,0x1
  4000fc:	b9 30 01 60 00       	mov    ecx,0x600130
  400101:	ba 32 00 00 00       	mov    edx,0x32
  400106:	cd 80                	int    0x80
  400108:	b8 01 00 00 00       	mov    eax,0x1
  40010d:	bb 00 00 00 00       	mov    ebx,0x0
  400112:	cd 80                	int    0x80
