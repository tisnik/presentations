
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x0000000000400078

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         0000000c  0000000000400078  0000000000400078  00000078  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
SYMBOL TABLE:
no symbols



Disassembly of section .text:

0000000000400078 <.text>:
  400078:	d2800ba8 	mov	x8, #0x5d                  	// #93
  40007c:	d2800000 	mov	x0, #0x0                   	// #0
  400080:	d4000001 	svc	#0x0
