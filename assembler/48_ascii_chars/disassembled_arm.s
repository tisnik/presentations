
a.out:     file format elf32-littlearm
architecture: arm, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x00008320

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .interp       00000019  00008134  00008134  00000134  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .note.ABI-tag 00000020  00008150  00008150  00000150  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .note.gnu.build-id 00000024  00008170  00008170  00000170  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  3 .hash         00000028  00008194  00008194  00000194  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .gnu.hash     0000002c  000081bc  000081bc  000001bc  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynsym       00000050  000081e8  000081e8  000001e8  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .dynstr       00000043  00008238  00008238  00000238  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version  0000000a  0000827c  0000827c  0000027c  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .gnu.version_r 00000020  00008288  00008288  00000288  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rel.dyn      00000008  000082a8  000082a8  000002a8  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .rel.plt      00000020  000082b0  000082b0  000002b0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 11 .init         0000000c  000082d0  000082d0  000002d0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .plt          00000044  000082dc  000082dc  000002dc  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .text         00000144  00008320  00008320  00000320  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .fini         00000008  00008464  00008464  00000464  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 15 .rodata       00000004  0000846c  0000846c  0000046c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .ARM.exidx    00000008  00008470  00008470  00000470  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 17 .eh_frame     00000004  00008478  00008478  00000478  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 18 .init_array   00000004  0001047c  0001047c  0000047c  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 19 .fini_array   00000004  00010480  00010480  00000480  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 20 .jcr          00000004  00010484  00010484  00000484  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 21 .dynamic      000000f0  00010488  00010488  00000488  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 22 .got          00000020  00010578  00010578  00000578  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         00000022  00010598  00010598  00000598  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000002  000105ba  000105ba  000005ba  2**0
                  ALLOC
 25 .comment      00000022  00000000  00000000  000005ba  2**0
                  CONTENTS, READONLY
 26 .ARM.attributes 0000002d  00000000  00000000  000005dc  2**0
                  CONTENTS, READONLY
SYMBOL TABLE:
00008134 l    d  .interp	00000000              .interp
00008150 l    d  .note.ABI-tag	00000000              .note.ABI-tag
00008170 l    d  .note.gnu.build-id	00000000              .note.gnu.build-id
00008194 l    d  .hash	00000000              .hash
000081bc l    d  .gnu.hash	00000000              .gnu.hash
000081e8 l    d  .dynsym	00000000              .dynsym
00008238 l    d  .dynstr	00000000              .dynstr
0000827c l    d  .gnu.version	00000000              .gnu.version
00008288 l    d  .gnu.version_r	00000000              .gnu.version_r
000082a8 l    d  .rel.dyn	00000000              .rel.dyn
000082b0 l    d  .rel.plt	00000000              .rel.plt
000082d0 l    d  .init	00000000              .init
000082dc l    d  .plt	00000000              .plt
00008320 l    d  .text	00000000              .text
00008464 l    d  .fini	00000000              .fini
0000846c l    d  .rodata	00000000              .rodata
00008470 l    d  .ARM.exidx	00000000              .ARM.exidx
00008478 l    d  .eh_frame	00000000              .eh_frame
0001047c l    d  .init_array	00000000              .init_array
00010480 l    d  .fini_array	00000000              .fini_array
00010484 l    d  .jcr	00000000              .jcr
00010488 l    d  .dynamic	00000000              .dynamic
00010578 l    d  .got	00000000              .got
00010598 l    d  .data	00000000              .data
000105ba l    d  .bss	00000000              .bss
00000000 l    d  .comment	00000000              .comment
00000000 l    d  .ARM.attributes	00000000              .ARM.attributes
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crt1.o
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crti.o
0000835c l     F .text	00000000              call_gmon_start
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crtn.o
00000000 l    df *ABS*	00000000              crtstuff.c
00010484 l     O .jcr	00000000              __JCR_LIST__
00008380 l     F .text	00000000              __do_global_dtors_aux
000105ba l     O .bss	00000001              completed.5637
00010480 l     O .fini_array	00000000              __do_global_dtors_aux_fini_array_entry
0000839c l     F .text	00000000              frame_dummy
0001047c l     O .init_array	00000000              __frame_dummy_init_array_entry
00000000 l    df *ABS*	00000000              /tmp/ccBtJIsL.o
000105a0 l       .data	00000000              ASCII_char_message
000083d4 l       .text	00000000              loop
00000000 l    df *ABS*	00000000              elf-init.oS
00000000 l    df *ABS*	00000000              crtstuff.c
00008478 l     O .eh_frame	00000000              __FRAME_END__
00010484 l     O .jcr	00000000              __JCR_END__
00000000 l    df *ABS*	00000000              
00010480 l       .init_array	00000000              __init_array_end
00010488 l     O .dynamic	00000000              _DYNAMIC
0001047c l       .init_array	00000000              __init_array_start
00010578 l     O .got	00000000              _GLOBAL_OFFSET_TABLE_
00008460 g     F .text	00000004              __libc_csu_fini
00010598  w      .data	00000000              data_start
00000000       F *UND*	00000000              printf@@GLIBC_2.4
000105ba g       .bss	00000000              __bss_start__
000105bc g       .bss	00000000              _bss_end__
000105ba g       .data	00000000              _edata
00008464 g     F .fini	00000000              _fini
000105bc g       .bss	00000000              __bss_end__
00010598 g       .data	00000000              __data_start
00000000       F *UND*	00000000              __libc_start_main@@GLIBC_2.4
00000000  w      *UND*	00000000              __gmon_start__
0001059c g     O .data	00000000              .hidden __dso_handle
0000846c g     O .rodata	00000004              _IO_stdin_used
00008400 g     F .text	00000060              __libc_csu_init
000105bc g       .bss	00000000              _end
00008320 g     F .text	00000000              _start
000105bc g       .bss	00000000              __end__
000105ba g       .bss	00000000              __bss_start
000083cc g       .text	00000000              main
00000000  w      *UND*	00000000              _Jv_RegisterClasses
00000000       F *UND*	00000000              abort@@GLIBC_2.4
000082d0 g     F .init	00000000              _init



Disassembly of section .init:

000082d0 <_init>:
    82d0:	e92d4008 	push	{r3, lr}
    82d4:	eb000020 	bl	835c <call_gmon_start>
    82d8:	e8bd8008 	pop	{r3, pc}

Disassembly of section .plt:

000082dc <printf@plt-0x14>:
    82dc:	e52de004 	push	{lr}		; (str lr, [sp, #-4]!)
    82e0:	e59fe004 	ldr	lr, [pc, #4]	; 82ec <_init+0x1c>
    82e4:	e08fe00e 	add	lr, pc, lr
    82e8:	e5bef008 	ldr	pc, [lr, #8]!
    82ec:	0000828c 	.word	0x0000828c

000082f0 <printf@plt>:
    82f0:	e28fc600 	add	ip, pc, #0, 12
    82f4:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    82f8:	e5bcf28c 	ldr	pc, [ip, #652]!	; 0x28c

000082fc <__libc_start_main@plt>:
    82fc:	e28fc600 	add	ip, pc, #0, 12
    8300:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    8304:	e5bcf284 	ldr	pc, [ip, #644]!	; 0x284

00008308 <__gmon_start__@plt>:
    8308:	e28fc600 	add	ip, pc, #0, 12
    830c:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    8310:	e5bcf27c 	ldr	pc, [ip, #636]!	; 0x27c

00008314 <abort@plt>:
    8314:	e28fc600 	add	ip, pc, #0, 12
    8318:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    831c:	e5bcf274 	ldr	pc, [ip, #628]!	; 0x274

Disassembly of section .text:

00008320 <_start>:
    8320:	e3a0b000 	mov	fp, #0
    8324:	e3a0e000 	mov	lr, #0
    8328:	e49d1004 	pop	{r1}		; (ldr r1, [sp], #4)
    832c:	e1a0200d 	mov	r2, sp
    8330:	e52d2004 	push	{r2}		; (str r2, [sp, #-4]!)
    8334:	e52d0004 	push	{r0}		; (str r0, [sp, #-4]!)
    8338:	e59fc010 	ldr	ip, [pc, #16]	; 8350 <_start+0x30>
    833c:	e52dc004 	push	{ip}		; (str ip, [sp, #-4]!)
    8340:	e59f000c 	ldr	r0, [pc, #12]	; 8354 <_start+0x34>
    8344:	e59f300c 	ldr	r3, [pc, #12]	; 8358 <_start+0x38>
    8348:	ebffffeb 	bl	82fc <__libc_start_main@plt>
    834c:	ebfffff0 	bl	8314 <abort@plt>
    8350:	00008460 	.word	0x00008460
    8354:	000083cc 	.word	0x000083cc
    8358:	00008400 	.word	0x00008400

0000835c <call_gmon_start>:
    835c:	e59f3014 	ldr	r3, [pc, #20]	; 8378 <call_gmon_start+0x1c>
    8360:	e59f2014 	ldr	r2, [pc, #20]	; 837c <call_gmon_start+0x20>
    8364:	e08f3003 	add	r3, pc, r3
    8368:	e7933002 	ldr	r3, [r3, r2]
    836c:	e3530000 	cmp	r3, #0
    8370:	012fff1e 	bxeq	lr
    8374:	eaffffe3 	b	8308 <__gmon_start__@plt>
    8378:	0000820c 	.word	0x0000820c
    837c:	0000001c 	.word	0x0000001c

00008380 <__do_global_dtors_aux>:
    8380:	e59f3010 	ldr	r3, [pc, #16]	; 8398 <__do_global_dtors_aux+0x18>
    8384:	e5d32000 	ldrb	r2, [r3]
    8388:	e3520000 	cmp	r2, #0
    838c:	03a02001 	moveq	r2, #1
    8390:	05c32000 	strbeq	r2, [r3]
    8394:	e12fff1e 	bx	lr
    8398:	000105ba 	.word	0x000105ba

0000839c <frame_dummy>:
    839c:	e59f0020 	ldr	r0, [pc, #32]	; 83c4 <frame_dummy+0x28>
    83a0:	e92d4008 	push	{r3, lr}
    83a4:	e5903000 	ldr	r3, [r0]
    83a8:	e3530000 	cmp	r3, #0
    83ac:	08bd8008 	popeq	{r3, pc}
    83b0:	e59f3010 	ldr	r3, [pc, #16]	; 83c8 <frame_dummy+0x2c>
    83b4:	e3530000 	cmp	r3, #0
    83b8:	08bd8008 	popeq	{r3, pc}
    83bc:	e12fff33 	blx	r3
    83c0:	e8bd8008 	pop	{r3, pc}
    83c4:	00010484 	.word	0x00010484
    83c8:	00000000 	.word	0x00000000

000083cc <main>:
    83cc:	e92d4000 	stmfd	sp!, {lr}
    83d0:	e3a04020 	mov	r4, #32

000083d4 <loop>:
    83d4:	e59f0020 	ldr	r0, [pc, #32]	; 83fc <loop+0x28>
    83d8:	e1a01004 	mov	r1, r4
    83dc:	e1a02004 	mov	r2, r4
    83e0:	e1a03004 	mov	r3, r4
    83e4:	ebffffc1 	bl	82f0 <printf@plt>
    83e8:	e2844001 	add	r4, r4, #1
    83ec:	e354007f 	cmp	r4, #127	; 0x7f
    83f0:	1afffff7 	bne	83d4 <loop>
    83f4:	e3a0002a 	mov	r0, #42	; 0x2a
    83f8:	e8bd8000 	ldmfd	sp!, {pc}
    83fc:	000105a0 	.word	0x000105a0

00008400 <__libc_csu_init>:
    8400:	e92d45f8 	push	{r3, r4, r5, r6, r7, r8, sl, lr}
    8404:	e1a06000 	mov	r6, r0
    8408:	e59f5048 	ldr	r5, [pc, #72]	; 8458 <__libc_csu_init+0x58>
    840c:	e59fa048 	ldr	sl, [pc, #72]	; 845c <__libc_csu_init+0x5c>
    8410:	e08f5005 	add	r5, pc, r5
    8414:	e08fa00a 	add	sl, pc, sl
    8418:	e065a00a 	rsb	sl, r5, sl
    841c:	e1a07001 	mov	r7, r1
    8420:	e1a08002 	mov	r8, r2
    8424:	ebffffa9 	bl	82d0 <_init>
    8428:	e1b0a14a 	asrs	sl, sl, #2
    842c:	08bd85f8 	popeq	{r3, r4, r5, r6, r7, r8, sl, pc}
    8430:	e3a04000 	mov	r4, #0
    8434:	e4953004 	ldr	r3, [r5], #4
    8438:	e1a00006 	mov	r0, r6
    843c:	e1a01007 	mov	r1, r7
    8440:	e1a02008 	mov	r2, r8
    8444:	e2844001 	add	r4, r4, #1
    8448:	e12fff33 	blx	r3
    844c:	e154000a 	cmp	r4, sl
    8450:	1afffff7 	bne	8434 <__libc_csu_init+0x34>
    8454:	e8bd85f8 	pop	{r3, r4, r5, r6, r7, r8, sl, pc}
    8458:	00008064 	.word	0x00008064
    845c:	00008064 	.word	0x00008064

00008460 <__libc_csu_fini>:
    8460:	e12fff1e 	bx	lr

Disassembly of section .fini:

00008464 <_fini>:
    8464:	e92d4008 	push	{r3, lr}
    8468:	e8bd8008 	pop	{r3, pc}
