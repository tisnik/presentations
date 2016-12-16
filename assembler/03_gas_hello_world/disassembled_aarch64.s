
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000028  00000000004000b0  00000000004000b0  000000b0  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .data         0000000e  00000000004100d8  00000000004100d8  000000d8  2**0
                  CONTENTS, ALLOC, LOAD, DATA
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	d2800808 	mov	x8, #0x40                  	// #64
  4000b4:	d2800020 	mov	x0, #0x1                   	// #1
  4000b8:	580000c1 	ldr	x1, 0x4000d0
  4000bc:	d28001a2 	mov	x2, #0xd                   	// #13
  4000c0:	d4000001 	svc	#0x0
  4000c4:	d2800ba8 	mov	x8, #0x5d                  	// #93
  4000c8:	d2800000 	mov	x0, #0x0                   	// #0
  4000cc:	d4000001 	svc	#0x0
  4000d0:	004100d8 	.inst	0x004100d8 ; undefined
  4000d4:	00000000 	.inst	0x00000000 ; undefined
