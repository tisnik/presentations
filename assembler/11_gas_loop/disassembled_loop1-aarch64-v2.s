
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000048  00000000004000b0  00000000004000b0  000000b0  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .bss          00000028  00000000004100f8  00000000004100f8  000000f8  2**3
                  ALLOC
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	58000201 	ldr	x1, 0x4000f0
  4000b4:	d2800502 	mov	x2, #0x28                  	// #40
  4000b8:	52800543 	mov	w3, #0x2a                  	// #42
  4000bc:	39000023 	strb	w3, [x1]
  4000c0:	91000421 	add	x1, x1, #0x1
  4000c4:	f1000442 	subs	x2, x2, #0x1
  4000c8:	54ffffa1 	b.ne	0x4000bc
  4000cc:	d2800808 	mov	x8, #0x40                  	// #64
  4000d0:	d2800020 	mov	x0, #0x1                   	// #1
  4000d4:	580000e1 	ldr	x1, 0x4000f0
  4000d8:	d2800502 	mov	x2, #0x28                  	// #40
  4000dc:	d4000001 	svc	#0x0
  4000e0:	d2800ba8 	mov	x8, #0x5d                  	// #93
  4000e4:	d2800000 	mov	x0, #0x0                   	// #0
  4000e8:	d4000001 	svc	#0x0
  4000ec:	00000000 	.inst	0x00000000 ; undefined
  4000f0:	004100f8 	.inst	0x004100f8 ; undefined
  4000f4:	00000000 	.inst	0x00000000 ; undefined
