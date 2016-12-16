
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000022  00000000004000b0  00000000004000b0  000000b0  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .data         0000000e  00000000006000d2  00000000006000d2  000000d2  2**0
                  CONTENTS, ALLOC, LOAD, DATA
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	b8 04 00 00 00       	mov    $0x4,%eax
  4000b5:	bb 01 00 00 00       	mov    $0x1,%ebx
  4000ba:	b9 d2 00 60 00       	mov    $0x6000d2,%ecx
  4000bf:	ba 0d 00 00 00       	mov    $0xd,%edx
  4000c4:	cd 80                	int    $0x80
  4000c6:	b8 01 00 00 00       	mov    $0x1,%eax
  4000cb:	bb 00 00 00 00       	mov    $0x0,%ebx
  4000d0:	cd 80                	int    $0x80
