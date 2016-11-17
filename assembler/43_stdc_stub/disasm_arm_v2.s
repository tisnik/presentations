
a.out:     file format elf32-littlearm
architecture: arm, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x000082e4

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .interp       00000019  00008134  00008134  00000134  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .note.ABI-tag 00000020  00008150  00008150  00000150  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .note.gnu.build-id 00000024  00008170  00008170  00000170  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  3 .hash         00000024  00008194  00008194  00000194  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .gnu.hash     00000024  000081b8  000081b8  000001b8  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynsym       00000040  000081dc  000081dc  000001dc  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .dynstr       0000003c  0000821c  0000821c  0000021c  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version  00000008  00008258  00008258  00000258  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .gnu.version_r 00000020  00008260  00008260  00000260  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rel.dyn      00000008  00008280  00008280  00000280  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .rel.plt      00000018  00008288  00008288  00000288  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 11 .init         0000000c  000082a0  000082a0  000002a0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .plt          00000038  000082ac  000082ac  000002ac  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .text         00000118  000082e4  000082e4  000002e4  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .fini         00000008  000083fc  000083fc  000003fc  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 15 .rodata       00000004  00008404  00008404  00000404  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .ARM.exidx    00000008  00008408  00008408  00000408  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 17 .eh_frame     00000004  00008410  00008410  00000410  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 18 .init_array   00000004  00010414  00010414  00000414  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 19 .fini_array   00000004  00010418  00010418  00000418  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 20 .jcr          00000004  0001041c  0001041c  0000041c  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 21 .dynamic      000000f0  00010420  00010420  00000420  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 22 .got          0000001c  00010510  00010510  00000510  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         00000008  0001052c  0001052c  0000052c  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000004  00010534  00010534  00000534  2**0
                  ALLOC
 25 .comment      00000022  00000000  00000000  00000534  2**0
                  CONTENTS, READONLY
 26 .ARM.attributes 0000002d  00000000  00000000  00000556  2**0
                  CONTENTS, READONLY
SYMBOL TABLE:
00008134 l    d  .interp	00000000              .interp
00008150 l    d  .note.ABI-tag	00000000              .note.ABI-tag
00008170 l    d  .note.gnu.build-id	00000000              .note.gnu.build-id
00008194 l    d  .hash	00000000              .hash
000081b8 l    d  .gnu.hash	00000000              .gnu.hash
000081dc l    d  .dynsym	00000000              .dynsym
0000821c l    d  .dynstr	00000000              .dynstr
00008258 l    d  .gnu.version	00000000              .gnu.version
00008260 l    d  .gnu.version_r	00000000              .gnu.version_r
00008280 l    d  .rel.dyn	00000000              .rel.dyn
00008288 l    d  .rel.plt	00000000              .rel.plt
000082a0 l    d  .init	00000000              .init
000082ac l    d  .plt	00000000              .plt
000082e4 l    d  .text	00000000              .text
000083fc l    d  .fini	00000000              .fini
00008404 l    d  .rodata	00000000              .rodata
00008408 l    d  .ARM.exidx	00000000              .ARM.exidx
00008410 l    d  .eh_frame	00000000              .eh_frame
00010414 l    d  .init_array	00000000              .init_array
00010418 l    d  .fini_array	00000000              .fini_array
0001041c l    d  .jcr	00000000              .jcr
00010420 l    d  .dynamic	00000000              .dynamic
00010510 l    d  .got	00000000              .got
0001052c l    d  .data	00000000              .data
00010534 l    d  .bss	00000000              .bss
00000000 l    d  .comment	00000000              .comment
00000000 l    d  .ARM.attributes	00000000              .ARM.attributes
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crt1.o
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crti.o
00008320 l     F .text	00000000              call_gmon_start
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crtn.o
00000000 l    df *ABS*	00000000              crtstuff.c
0001041c l     O .jcr	00000000              __JCR_LIST__
00008344 l     F .text	00000000              __do_global_dtors_aux
00010534 l     O .bss	00000001              completed.5637
00010418 l     O .fini_array	00000000              __do_global_dtors_aux_fini_array_entry
00008360 l     F .text	00000000              frame_dummy
00010414 l     O .init_array	00000000              __frame_dummy_init_array_entry
00000000 l    df *ABS*	00000000              /tmp/ccfuozez.o
00000000 l    df *ABS*	00000000              elf-init.oS
00000000 l    df *ABS*	00000000              crtstuff.c
00008410 l     O .eh_frame	00000000              __FRAME_END__
0001041c l     O .jcr	00000000              __JCR_END__
00000000 l    df *ABS*	00000000              
00010418 l       .init_array	00000000              __init_array_end
00010420 l     O .dynamic	00000000              _DYNAMIC
00010414 l       .init_array	00000000              __init_array_start
00010510 l     O .got	00000000              _GLOBAL_OFFSET_TABLE_
000083f8 g     F .text	00000004              __libc_csu_fini
0001052c  w      .data	00000000              data_start
00010534 g       .bss	00000000              __bss_start__
00010538 g       .bss	00000000              _bss_end__
00010534 g       .data	00000000              _edata
000083fc g     F .fini	00000000              _fini
00010538 g       .bss	00000000              __bss_end__
0001052c g       .data	00000000              __data_start
00000000       F *UND*	00000000              __libc_start_main@@GLIBC_2.4
00000000  w      *UND*	00000000              __gmon_start__
00010530 g     O .data	00000000              .hidden __dso_handle
00008404 g     O .rodata	00000004              _IO_stdin_used
00008398 g     F .text	00000060              __libc_csu_init
00010538 g       .bss	00000000              _end
000082e4 g     F .text	00000000              _start
00010538 g       .bss	00000000              __end__
00010534 g       .bss	00000000              __bss_start
00008390 g       .text	00000000              main
00000000  w      *UND*	00000000              _Jv_RegisterClasses
00000000       F *UND*	00000000              abort@@GLIBC_2.4
000082a0 g     F .init	00000000              _init



Disassembly of section .init:

000082a0 <_init>:
    82a0:	e92d4008 	push	{r3, lr}
    82a4:	eb00001d 	bl	8320 <call_gmon_start>
    82a8:	e8bd8008 	pop	{r3, pc}

Disassembly of section .plt:

000082ac <__libc_start_main@plt-0x14>:
    82ac:	e52de004 	push	{lr}		; (str lr, [sp, #-4]!)
    82b0:	e59fe004 	ldr	lr, [pc, #4]	; 82bc <_init+0x1c>
    82b4:	e08fe00e 	add	lr, pc, lr
    82b8:	e5bef008 	ldr	pc, [lr, #8]!
    82bc:	00008254 	.word	0x00008254

000082c0 <__libc_start_main@plt>:
    82c0:	e28fc600 	add	ip, pc, #0, 12
    82c4:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    82c8:	e5bcf254 	ldr	pc, [ip, #596]!	; 0x254

000082cc <__gmon_start__@plt>:
    82cc:	e28fc600 	add	ip, pc, #0, 12
    82d0:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    82d4:	e5bcf24c 	ldr	pc, [ip, #588]!	; 0x24c

000082d8 <abort@plt>:
    82d8:	e28fc600 	add	ip, pc, #0, 12
    82dc:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    82e0:	e5bcf244 	ldr	pc, [ip, #580]!	; 0x244

Disassembly of section .text:

000082e4 <_start>:
    82e4:	e3a0b000 	mov	fp, #0
    82e8:	e3a0e000 	mov	lr, #0
    82ec:	e49d1004 	pop	{r1}		; (ldr r1, [sp], #4)
    82f0:	e1a0200d 	mov	r2, sp
    82f4:	e52d2004 	push	{r2}		; (str r2, [sp, #-4]!)
    82f8:	e52d0004 	push	{r0}		; (str r0, [sp, #-4]!)
    82fc:	e59fc010 	ldr	ip, [pc, #16]	; 8314 <_start+0x30>
    8300:	e52dc004 	push	{ip}		; (str ip, [sp, #-4]!)
    8304:	e59f000c 	ldr	r0, [pc, #12]	; 8318 <_start+0x34>
    8308:	e59f300c 	ldr	r3, [pc, #12]	; 831c <_start+0x38>
    830c:	ebffffeb 	bl	82c0 <__libc_start_main@plt>
    8310:	ebfffff0 	bl	82d8 <abort@plt>
    8314:	000083f8 	.word	0x000083f8
    8318:	00008390 	.word	0x00008390
    831c:	00008398 	.word	0x00008398

00008320 <call_gmon_start>:
    8320:	e59f3014 	ldr	r3, [pc, #20]	; 833c <call_gmon_start+0x1c>
    8324:	e59f2014 	ldr	r2, [pc, #20]	; 8340 <call_gmon_start+0x20>
    8328:	e08f3003 	add	r3, pc, r3
    832c:	e7933002 	ldr	r3, [r3, r2]
    8330:	e3530000 	cmp	r3, #0
    8334:	012fff1e 	bxeq	lr
    8338:	eaffffe3 	b	82cc <__gmon_start__@plt>
    833c:	000081e0 	.word	0x000081e0
    8340:	00000018 	.word	0x00000018

00008344 <__do_global_dtors_aux>:
    8344:	e59f3010 	ldr	r3, [pc, #16]	; 835c <__do_global_dtors_aux+0x18>
    8348:	e5d32000 	ldrb	r2, [r3]
    834c:	e3520000 	cmp	r2, #0
    8350:	03a02001 	moveq	r2, #1
    8354:	05c32000 	strbeq	r2, [r3]
    8358:	e12fff1e 	bx	lr
    835c:	00010534 	.word	0x00010534

00008360 <frame_dummy>:
    8360:	e59f0020 	ldr	r0, [pc, #32]	; 8388 <frame_dummy+0x28>
    8364:	e92d4008 	push	{r3, lr}
    8368:	e5903000 	ldr	r3, [r0]
    836c:	e3530000 	cmp	r3, #0
    8370:	08bd8008 	popeq	{r3, pc}
    8374:	e59f3010 	ldr	r3, [pc, #16]	; 838c <frame_dummy+0x2c>
    8378:	e3530000 	cmp	r3, #0
    837c:	08bd8008 	popeq	{r3, pc}
    8380:	e12fff33 	blx	r3
    8384:	e8bd8008 	pop	{r3, pc}
    8388:	0001041c 	.word	0x0001041c
    838c:	00000000 	.word	0x00000000

00008390 <main>:
    8390:	e3a00000 	mov	r0, #0
    8394:	e12fff1e 	bx	lr

00008398 <__libc_csu_init>:
    8398:	e92d45f8 	push	{r3, r4, r5, r6, r7, r8, sl, lr}
    839c:	e1a06000 	mov	r6, r0
    83a0:	e59f5048 	ldr	r5, [pc, #72]	; 83f0 <__libc_csu_init+0x58>
    83a4:	e59fa048 	ldr	sl, [pc, #72]	; 83f4 <__libc_csu_init+0x5c>
    83a8:	e08f5005 	add	r5, pc, r5
    83ac:	e08fa00a 	add	sl, pc, sl
    83b0:	e065a00a 	rsb	sl, r5, sl
    83b4:	e1a07001 	mov	r7, r1
    83b8:	e1a08002 	mov	r8, r2
    83bc:	ebffffb7 	bl	82a0 <_init>
    83c0:	e1b0a14a 	asrs	sl, sl, #2
    83c4:	08bd85f8 	popeq	{r3, r4, r5, r6, r7, r8, sl, pc}
    83c8:	e3a04000 	mov	r4, #0
    83cc:	e4953004 	ldr	r3, [r5], #4
    83d0:	e1a00006 	mov	r0, r6
    83d4:	e1a01007 	mov	r1, r7
    83d8:	e1a02008 	mov	r2, r8
    83dc:	e2844001 	add	r4, r4, #1
    83e0:	e12fff33 	blx	r3
    83e4:	e154000a 	cmp	r4, sl
    83e8:	1afffff7 	bne	83cc <__libc_csu_init+0x34>
    83ec:	e8bd85f8 	pop	{r3, r4, r5, r6, r7, r8, sl, pc}
    83f0:	00008064 	.word	0x00008064
    83f4:	00008064 	.word	0x00008064

000083f8 <__libc_csu_fini>:
    83f8:	e12fff1e 	bx	lr

Disassembly of section .fini:

000083fc <_fini>:
    83fc:	e92d4008 	push	{r3, lr}
    8400:	e8bd8008 	pop	{r3, pc}
