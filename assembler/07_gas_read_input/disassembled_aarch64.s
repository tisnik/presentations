
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000078  00000000004000b0  00000000004000b0  000000b0  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .data         00000017  0000000000410128  0000000000410128  00000128  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000038  0000000000410140  0000000000410140  0000013f  2**3
                  ALLOC
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	d2800808 	mov	x8, #0x40                  	// #64
  4000b4:	d2800020 	mov	x0, #0x1                   	// #1
  4000b8:	580002c1 	ldr	x1, 0x400110
  4000bc:	d2800222 	mov	x2, #0x11                  	// #17
  4000c0:	d4000001 	svc	#0x0
  4000c4:	d28007e8 	mov	x8, #0x3f                  	// #63
  4000c8:	d2800000 	mov	x0, #0x0                   	// #0
  4000cc:	58000261 	ldr	x1, 0x400118
  4000d0:	d2800642 	mov	x2, #0x32                  	// #50
  4000d4:	d4000001 	svc	#0x0
  4000d8:	d2800808 	mov	x8, #0x40                  	// #64
  4000dc:	d2800020 	mov	x0, #0x1                   	// #1
  4000e0:	58000201 	ldr	x1, 0x400120
  4000e4:	d28000c2 	mov	x2, #0x6                   	// #6
  4000e8:	d4000001 	svc	#0x0
  4000ec:	d2800808 	mov	x8, #0x40                  	// #64
  4000f0:	d2800020 	mov	x0, #0x1                   	// #1
  4000f4:	58000121 	ldr	x1, 0x400118
  4000f8:	d2800642 	mov	x2, #0x32                  	// #50
  4000fc:	d4000001 	svc	#0x0
  400100:	d2800ba8 	mov	x8, #0x5d                  	// #93
  400104:	d2800000 	mov	x0, #0x0                   	// #0
  400108:	d4000001 	svc	#0x0
  40010c:	00000000 	.inst	0x00000000 ; undefined
  400110:	00410128 	.inst	0x00410128 ; undefined
  400114:	00000000 	.inst	0x00000000 ; undefined
  400118:	00410140 	.inst	0x00410140 ; undefined
  40011c:	00000000 	.inst	0x00000000 ; undefined
  400120:	00410139 	.inst	0x00410139 ; undefined
  400124:	00000000 	.inst	0x00000000 ; undefined
