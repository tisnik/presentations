
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000050  00000000004000b0  00000000004000b0  000000b0  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .bss          00000028  0000000000410100  0000000000410100  00000100  2**3
                  ALLOC
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	58000241 	ldr	x1, 0x4000f8
  4000b4:	d2800522 	mov	x2, #0x29                  	// #41
  4000b8:	52800543 	mov	w3, #0x2a                  	// #42
  4000bc:	d1000442 	sub	x2, x2, #0x1
  4000c0:	f100005f 	cmp	x2, #0x0
  4000c4:	54000080 	b.eq	0x4000d4
  4000c8:	39000023 	strb	w3, [x1]
  4000cc:	91000421 	add	x1, x1, #0x1
  4000d0:	17fffffb 	b	0x4000bc
  4000d4:	d2800808 	mov	x8, #0x40                  	// #64
  4000d8:	d2800020 	mov	x0, #0x1                   	// #1
  4000dc:	580000e1 	ldr	x1, 0x4000f8
  4000e0:	d2800502 	mov	x2, #0x28                  	// #40
  4000e4:	d4000001 	svc	#0x0
  4000e8:	d2800ba8 	mov	x8, #0x5d                  	// #93
  4000ec:	d2800000 	mov	x0, #0x0                   	// #0
  4000f0:	d4000001 	svc	#0x0
  4000f4:	00000000 	.inst	0x00000000 ; undefined
  4000f8:	00410100 	.inst	0x00410100 ; undefined
  4000fc:	00000000 	.inst	0x00000000 ; undefined
