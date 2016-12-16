
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x0000000000400078

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         0000000c  0000000000400078  0000000000400078  00000078  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
SYMBOL TABLE:
no symbols



Disassembly of section .text:

0000000000400078 <.text>:
  400078:	b8 01 00 00 00       	mov    $0x1,%eax
  40007d:	bb 00 00 00 00       	mov    $0x0,%ebx
  400082:	cd 80                	int    $0x80
