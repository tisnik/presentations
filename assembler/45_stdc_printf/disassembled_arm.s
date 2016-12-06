
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
 13 .text         00000128  00008320  00008320  00000320  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .fini         00000008  00008448  00008448  00000448  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 15 .rodata       00000004  00008450  00008450  00000450  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .ARM.exidx    00000008  00008454  00008454  00000454  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 17 .eh_frame     00000004  0000845c  0000845c  0000045c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 18 .init_array   00000004  00010460  00010460  00000460  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 19 .fini_array   00000004  00010464  00010464  00000464  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 20 .jcr          00000004  00010468  00010468  00000468  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 21 .dynamic      000000f0  0001046c  0001046c  0000046c  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 22 .got          00000020  0001055c  0001055c  0000055c  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         00000016  0001057c  0001057c  0000057c  2**2
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000002  00010592  00010592  00000592  2**0
                  ALLOC
 25 .comment      00000022  00000000  00000000  00000592  2**0
                  CONTENTS, READONLY
 26 .ARM.attributes 0000002d  00000000  00000000  000005b4  2**0
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
00008448 l    d  .fini	00000000              .fini
00008450 l    d  .rodata	00000000              .rodata
00008454 l    d  .ARM.exidx	00000000              .ARM.exidx
0000845c l    d  .eh_frame	00000000              .eh_frame
00010460 l    d  .init_array	00000000              .init_array
00010464 l    d  .fini_array	00000000              .fini_array
00010468 l    d  .jcr	00000000              .jcr
0001046c l    d  .dynamic	00000000              .dynamic
0001055c l    d  .got	00000000              .got
0001057c l    d  .data	00000000              .data
00010592 l    d  .bss	00000000              .bss
00000000 l    d  .comment	00000000              .comment
00000000 l    d  .ARM.attributes	00000000              .ARM.attributes
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crt1.o
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crti.o
0000835c l     F .text	00000000              call_gmon_start
00000000 l    df *ABS*	00000000              /usr/lib/gcc/arm-linux-gnueabihf/4.6/../../../arm-linux-gnueabihf/crtn.o
00000000 l    df *ABS*	00000000              crtstuff.c
00010468 l     O .jcr	00000000              __JCR_LIST__
00008380 l     F .text	00000000              __do_global_dtors_aux
00010592 l     O .bss	00000001              completed.5637
00010464 l     O .fini_array	00000000              __do_global_dtors_aux_fini_array_entry
0000839c l     F .text	00000000              frame_dummy
00010460 l     O .init_array	00000000              __frame_dummy_init_array_entry
00000000 l    df *ABS*	00000000              /tmp/ccZ3q9gW.o
00010584 l       .data	00000000              hello_world_message
00000000 l    df *ABS*	00000000              elf-init.oS
00000000 l    df *ABS*	00000000              crtstuff.c
0000845c l     O .eh_frame	00000000              __FRAME_END__
00010468 l     O .jcr	00000000              __JCR_END__
00000000 l    df *ABS*	00000000              
00010464 l       .init_array	00000000              __init_array_end
0001046c l     O .dynamic	00000000              _DYNAMIC
00010460 l       .init_array	00000000              __init_array_start
0001055c l     O .got	00000000              _GLOBAL_OFFSET_TABLE_
00008444 g     F .text	00000004              __libc_csu_fini
0001057c  w      .data	00000000              data_start
00000000       F *UND*	00000000              printf@@GLIBC_2.4
00010592 g       .bss	00000000              __bss_start__
00010594 g       .bss	00000000              _bss_end__
00010592 g       .data	00000000              _edata
00008448 g     F .fini	00000000              _fini
00010594 g       .bss	00000000              __bss_end__
0001057c g       .data	00000000              __data_start
00000000       F *UND*	00000000              __libc_start_main@@GLIBC_2.4
00000000  w      *UND*	00000000              __gmon_start__
00010580 g     O .data	00000000              .hidden __dso_handle
00008450 g     O .rodata	00000004              _IO_stdin_used
000083e4 g     F .text	00000060              __libc_csu_init
00010594 g       .bss	00000000              _end
00008320 g     F .text	00000000              _start
00010594 g       .bss	00000000              __end__
00010592 g       .bss	00000000              __bss_start
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
    82ec:	00008270 	.word	0x00008270

000082f0 <printf@plt>:
    82f0:	e28fc600 	add	ip, pc, #0, 12
    82f4:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    82f8:	e5bcf270 	ldr	pc, [ip, #624]!	; 0x270

000082fc <__libc_start_main@plt>:
    82fc:	e28fc600 	add	ip, pc, #0, 12
    8300:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    8304:	e5bcf268 	ldr	pc, [ip, #616]!	; 0x268

00008308 <__gmon_start__@plt>:
    8308:	e28fc600 	add	ip, pc, #0, 12
    830c:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    8310:	e5bcf260 	ldr	pc, [ip, #608]!	; 0x260

00008314 <abort@plt>:
    8314:	e28fc600 	add	ip, pc, #0, 12
    8318:	e28cca08 	add	ip, ip, #8, 20	; 0x8000
    831c:	e5bcf258 	ldr	pc, [ip, #600]!	; 0x258

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
    8350:	00008444 	.word	0x00008444
    8354:	000083cc 	.word	0x000083cc
    8358:	000083e4 	.word	0x000083e4

0000835c <call_gmon_start>:
    835c:	e59f3014 	ldr	r3, [pc, #20]	; 8378 <call_gmon_start+0x1c>
    8360:	e59f2014 	ldr	r2, [pc, #20]	; 837c <call_gmon_start+0x20>
    8364:	e08f3003 	add	r3, pc, r3
    8368:	e7933002 	ldr	r3, [r3, r2]
    836c:	e3530000 	cmp	r3, #0
    8370:	012fff1e 	bxeq	lr
    8374:	eaffffe3 	b	8308 <__gmon_start__@plt>
    8378:	000081f0 	.word	0x000081f0
    837c:	0000001c 	.word	0x0000001c

00008380 <__do_global_dtors_aux>:
    8380:	e59f3010 	ldr	r3, [pc, #16]	; 8398 <__do_global_dtors_aux+0x18>
    8384:	e5d32000 	ldrb	r2, [r3]
    8388:	e3520000 	cmp	r2, #0
    838c:	03a02001 	moveq	r2, #1
    8390:	05c32000 	strbeq	r2, [r3]
    8394:	e12fff1e 	bx	lr
    8398:	00010592 	.word	0x00010592

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
    83c4:	00010468 	.word	0x00010468
    83c8:	00000000 	.word	0x00000000

000083cc <main>:
    83cc:	e92d4000 	stmfd	sp!, {lr}
    83d0:	e59f0008 	ldr	r0, [pc, #8]	; 83e0 <main+0x14>
    83d4:	ebffffc5 	bl	82f0 <printf@plt>
    83d8:	e3a0002a 	mov	r0, #42	; 0x2a
    83dc:	e8bd8000 	ldmfd	sp!, {pc}
    83e0:	00010584 	.word	0x00010584

000083e4 <__libc_csu_init>:
    83e4:	e92d45f8 	push	{r3, r4, r5, r6, r7, r8, sl, lr}
    83e8:	e1a06000 	mov	r6, r0
    83ec:	e59f5048 	ldr	r5, [pc, #72]	; 843c <__libc_csu_init+0x58>
    83f0:	e59fa048 	ldr	sl, [pc, #72]	; 8440 <__libc_csu_init+0x5c>
    83f4:	e08f5005 	add	r5, pc, r5
    83f8:	e08fa00a 	add	sl, pc, sl
    83fc:	e065a00a 	rsb	sl, r5, sl
    8400:	e1a07001 	mov	r7, r1
    8404:	e1a08002 	mov	r8, r2
    8408:	ebffffb0 	bl	82d0 <_init>
    840c:	e1b0a14a 	asrs	sl, sl, #2
    8410:	08bd85f8 	popeq	{r3, r4, r5, r6, r7, r8, sl, pc}
    8414:	e3a04000 	mov	r4, #0
    8418:	e4953004 	ldr	r3, [r5], #4
    841c:	e1a00006 	mov	r0, r6
    8420:	e1a01007 	mov	r1, r7
    8424:	e1a02008 	mov	r2, r8
    8428:	e2844001 	add	r4, r4, #1
    842c:	e12fff33 	blx	r3
    8430:	e154000a 	cmp	r4, sl
    8434:	1afffff7 	bne	8418 <__libc_csu_init+0x34>
    8438:	e8bd85f8 	pop	{r3, r4, r5, r6, r7, r8, sl, pc}
    843c:	00008064 	.word	0x00008064
    8440:	00008064 	.word	0x00008064

00008444 <__libc_csu_fini>:
    8444:	e12fff1e 	bx	lr

Disassembly of section .fini:

00008448 <_fini>:
    8448:	e92d4008 	push	{r3, lr}
    844c:	e8bd8008 	pop	{r3, pc}
