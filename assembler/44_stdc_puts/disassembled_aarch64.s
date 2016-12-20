
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x0000000000400470

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .interp       0000001b  0000000000400200  0000000000400200  00000200  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .note.ABI-tag 00000020  000000000040021c  000000000040021c  0000021c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .note.gnu.build-id 00000024  000000000040023c  000000000040023c  0000023c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  3 .gnu.hash     00000030  0000000000400260  0000000000400260  00000260  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .dynsym       00000078  0000000000400290  0000000000400290  00000290  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynstr       00000042  0000000000400308  0000000000400308  00000308  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .gnu.version  0000000a  000000000040034a  000000000040034a  0000034a  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version_r 00000020  0000000000400358  0000000000400358  00000358  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .rela.dyn     00000018  0000000000400378  0000000000400378  00000378  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rela.plt     00000060  0000000000400390  0000000000400390  00000390  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .init         00000014  00000000004003f0  00000000004003f0  000003f0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 11 .plt          00000060  0000000000400410  0000000000400410  00000410  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .text         000001dc  0000000000400470  0000000000400470  00000470  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .fini         00000010  000000000040064c  000000000040064c  0000064c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .rodata       00000028  0000000000400660  0000000000400660  00000660  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 15 .eh_frame_hdr 0000003c  0000000000400688  0000000000400688  00000688  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .eh_frame     000000ec  00000000004006c8  00000000004006c8  000006c8  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 17 .init_array   00000008  00000000004107b8  00000000004107b8  000007b8  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 18 .fini_array   00000008  00000000004107c0  00000000004107c0  000007c0  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 19 .jcr          00000008  00000000004107c8  00000000004107c8  000007c8  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 20 .dynamic      000001d0  00000000004107d0  00000000004107d0  000007d0  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 21 .got          00000010  00000000004109a0  00000000004109a0  000009a0  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 22 .got.plt      00000038  00000000004109b0  00000000004109b0  000009b0  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         00000012  00000000004109e8  00000000004109e8  000009e8  2**0
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000006  00000000004109fa  00000000004109fa  000009fa  2**0
                  ALLOC
 25 .comment      0000002c  0000000000000000  0000000000000000  000009fa  2**0
                  CONTENTS, READONLY
SYMBOL TABLE:
0000000000400200 l    d  .interp	0000000000000000              .interp
000000000040021c l    d  .note.ABI-tag	0000000000000000              .note.ABI-tag
000000000040023c l    d  .note.gnu.build-id	0000000000000000              .note.gnu.build-id
0000000000400260 l    d  .gnu.hash	0000000000000000              .gnu.hash
0000000000400290 l    d  .dynsym	0000000000000000              .dynsym
0000000000400308 l    d  .dynstr	0000000000000000              .dynstr
000000000040034a l    d  .gnu.version	0000000000000000              .gnu.version
0000000000400358 l    d  .gnu.version_r	0000000000000000              .gnu.version_r
0000000000400378 l    d  .rela.dyn	0000000000000000              .rela.dyn
0000000000400390 l    d  .rela.plt	0000000000000000              .rela.plt
00000000004003f0 l    d  .init	0000000000000000              .init
0000000000400410 l    d  .plt	0000000000000000              .plt
0000000000400470 l    d  .text	0000000000000000              .text
000000000040064c l    d  .fini	0000000000000000              .fini
0000000000400660 l    d  .rodata	0000000000000000              .rodata
0000000000400688 l    d  .eh_frame_hdr	0000000000000000              .eh_frame_hdr
00000000004006c8 l    d  .eh_frame	0000000000000000              .eh_frame
00000000004107b8 l    d  .init_array	0000000000000000              .init_array
00000000004107c0 l    d  .fini_array	0000000000000000              .fini_array
00000000004107c8 l    d  .jcr	0000000000000000              .jcr
00000000004107d0 l    d  .dynamic	0000000000000000              .dynamic
00000000004109a0 l    d  .got	0000000000000000              .got
00000000004109b0 l    d  .got.plt	0000000000000000              .got.plt
00000000004109e8 l    d  .data	0000000000000000              .data
00000000004109fa l    d  .bss	0000000000000000              .bss
0000000000000000 l    d  .comment	0000000000000000              .comment
0000000000000000 l    df *ABS*	0000000000000000              /usr/lib/gcc/aarch64-redhat-linux/6.2.1/../../../../lib64/crt1.o
0000000000000000 l    df *ABS*	0000000000000000              /usr/lib/gcc/aarch64-redhat-linux/6.2.1/../../../../lib64/crti.o
00000000004004b8 l     F .text	0000000000000014              call_weak_fn
0000000000000000 l    df *ABS*	0000000000000000              /usr/lib/gcc/aarch64-redhat-linux/6.2.1/../../../../lib64/crtn.o
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
00000000004107c8 l     O .jcr	0000000000000000              __JCR_LIST__
00000000004004d0 l     F .text	0000000000000000              deregister_tm_clones
0000000000400508 l     F .text	0000000000000000              register_tm_clones
0000000000400548 l     F .text	0000000000000000              __do_global_dtors_aux
00000000004109fa l     O .bss	0000000000000001              completed.7407
00000000004107c0 l     O .fini_array	0000000000000000              __do_global_dtors_aux_fini_array_entry
0000000000400578 l     F .text	0000000000000000              frame_dummy
00000000004107b8 l     O .init_array	0000000000000000              __frame_dummy_init_array_entry
0000000000000000 l    df *ABS*	0000000000000000              /tmp/ccMqBffy.o
00000000004109ec l       .data	0000000000000000              hello_world_message
0000000000000000 l    df *ABS*	0000000000000000              elf-init.oS
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
00000000004007b0 l     O .eh_frame	0000000000000000              __FRAME_END__
00000000004107c8 l     O .jcr	0000000000000000              __JCR_END__
0000000000000000 l    df *ABS*	0000000000000000              
00000000004107c0 l       .init_array	0000000000000000              __init_array_end
00000000004107d0 l     O .dynamic	0000000000000000              _DYNAMIC
00000000004107b8 l       .init_array	0000000000000000              __init_array_start
0000000000400688 l       .eh_frame_hdr	0000000000000000              __GNU_EH_FRAME_HDR
00000000004109a0 l     O .got	0000000000000000              _GLOBAL_OFFSET_TABLE_
0000000000400648 g     F .text	0000000000000004              __libc_csu_fini
0000000000000000  w      *UND*	0000000000000000              _ITM_deregisterTMCloneTable
00000000004109e8  w      .data	0000000000000000              data_start
00000000004109fa g       .bss	0000000000000000              __bss_start__
0000000000410a00 g       .bss	0000000000000000              _bss_end__
00000000004109fa g       .data	0000000000000000              _edata
000000000040064c g     F .fini	0000000000000000              _fini
0000000000410a00 g       .bss	0000000000000000              __bss_end__
0000000000000000       F *UND*	0000000000000000              __libc_start_main@@GLIBC_2.17
00000000004109e8 g       .data	0000000000000000              __data_start
0000000000000000  w      *UND*	0000000000000000              __gmon_start__
0000000000400680 g     O .rodata	0000000000000000              .hidden __dso_handle
0000000000000000       F *UND*	0000000000000000              abort@@GLIBC_2.17
0000000000400660 g     O .rodata	0000000000000004              _IO_stdin_used
0000000000000000       F *UND*	0000000000000000              puts@@GLIBC_2.17
00000000004005d0 g     F .text	0000000000000078              __libc_csu_init
0000000000410a00 g       .bss	0000000000000000              _end
0000000000400470 g     F .text	0000000000000000              _start
0000000000410a00 g       .bss	0000000000000000              __end__
00000000004109fa g       .bss	0000000000000000              __bss_start
00000000004005b0 g       .text	0000000000000000              main
0000000000000000  w      *UND*	0000000000000000              _Jv_RegisterClasses
0000000000410a00 g     O .data	0000000000000000              .hidden __TMC_END__
0000000000000000  w      *UND*	0000000000000000              _ITM_registerTMCloneTable
00000000004003f0 g     F .init	0000000000000000              _init



Disassembly of section .init:

00000000004003f0 <_init>:
  4003f0:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  4003f4:	910003fd 	mov	x29, sp
  4003f8:	94000030 	bl	4004b8 <call_weak_fn>
  4003fc:	a8c17bfd 	ldp	x29, x30, [sp],#16
  400400:	d65f03c0 	ret

Disassembly of section .plt:

0000000000400410 <__libc_start_main@plt-0x20>:
  400410:	a9bf7bf0 	stp	x16, x30, [sp,#-16]!
  400414:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf850>
  400418:	f944e211 	ldr	x17, [x16,#2496]
  40041c:	91270210 	add	x16, x16, #0x9c0
  400420:	d61f0220 	br	x17
  400424:	d503201f 	nop
  400428:	d503201f 	nop
  40042c:	d503201f 	nop

0000000000400430 <__libc_start_main@plt>:
  400430:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf850>
  400434:	f944e611 	ldr	x17, [x16,#2504]
  400438:	91272210 	add	x16, x16, #0x9c8
  40043c:	d61f0220 	br	x17

0000000000400440 <__gmon_start__@plt>:
  400440:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf850>
  400444:	f944ea11 	ldr	x17, [x16,#2512]
  400448:	91274210 	add	x16, x16, #0x9d0
  40044c:	d61f0220 	br	x17

0000000000400450 <abort@plt>:
  400450:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf850>
  400454:	f944ee11 	ldr	x17, [x16,#2520]
  400458:	91276210 	add	x16, x16, #0x9d8
  40045c:	d61f0220 	br	x17

0000000000400460 <puts@plt>:
  400460:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf850>
  400464:	f944f211 	ldr	x17, [x16,#2528]
  400468:	91278210 	add	x16, x16, #0x9e0
  40046c:	d61f0220 	br	x17

Disassembly of section .text:

0000000000400470 <_start>:
  400470:	d280001d 	mov	x29, #0x0                   	// #0
  400474:	d280001e 	mov	x30, #0x0                   	// #0
  400478:	aa0003e5 	mov	x5, x0
  40047c:	f94003e1 	ldr	x1, [sp]
  400480:	910023e2 	add	x2, sp, #0x8
  400484:	910003e6 	mov	x6, sp
  400488:	580000c0 	ldr	x0, 4004a0 <_start+0x30>
  40048c:	580000e3 	ldr	x3, 4004a8 <_start+0x38>
  400490:	58000104 	ldr	x4, 4004b0 <_start+0x40>
  400494:	97ffffe7 	bl	400430 <__libc_start_main@plt>
  400498:	97ffffee 	bl	400450 <abort@plt>
  40049c:	00000000 	.word	0x00000000
  4004a0:	004005b0 	.word	0x004005b0
  4004a4:	00000000 	.word	0x00000000
  4004a8:	004005d0 	.word	0x004005d0
  4004ac:	00000000 	.word	0x00000000
  4004b0:	00400648 	.word	0x00400648
  4004b4:	00000000 	.word	0x00000000

00000000004004b8 <call_weak_fn>:
  4004b8:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf850>
  4004bc:	f944d400 	ldr	x0, [x0,#2472]
  4004c0:	b4000040 	cbz	x0, 4004c8 <call_weak_fn+0x10>
  4004c4:	17ffffdf 	b	400440 <__gmon_start__@plt>
  4004c8:	d65f03c0 	ret
  4004cc:	00000000 	.inst	0x00000000 ; undefined

00000000004004d0 <deregister_tm_clones>:
  4004d0:	90000081 	adrp	x1, 410000 <__FRAME_END__+0xf850>
  4004d4:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf850>
  4004d8:	91280021 	add	x1, x1, #0xa00
  4004dc:	91280000 	add	x0, x0, #0xa00
  4004e0:	91001c21 	add	x1, x1, #0x7
  4004e4:	cb000021 	sub	x1, x1, x0
  4004e8:	f100383f 	cmp	x1, #0xe
  4004ec:	540000a9 	b.ls	400500 <deregister_tm_clones+0x30>
  4004f0:	90000001 	adrp	x1, 400000 <_init-0x3f0>
  4004f4:	f9433421 	ldr	x1, [x1,#1640]
  4004f8:	b4000041 	cbz	x1, 400500 <deregister_tm_clones+0x30>
  4004fc:	d61f0020 	br	x1
  400500:	d65f03c0 	ret
  400504:	d503201f 	nop

0000000000400508 <register_tm_clones>:
  400508:	90000081 	adrp	x1, 410000 <__FRAME_END__+0xf850>
  40050c:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf850>
  400510:	91280021 	add	x1, x1, #0xa00
  400514:	91280000 	add	x0, x0, #0xa00
  400518:	cb000021 	sub	x1, x1, x0
  40051c:	9343fc21 	asr	x1, x1, #3
  400520:	8b41fc21 	add	x1, x1, x1, lsr #63
  400524:	9341fc21 	asr	x1, x1, #1
  400528:	b40000c1 	cbz	x1, 400540 <register_tm_clones+0x38>
  40052c:	90000002 	adrp	x2, 400000 <_init-0x3f0>
  400530:	f9433842 	ldr	x2, [x2,#1648]
  400534:	b4000062 	cbz	x2, 400540 <register_tm_clones+0x38>
  400538:	d61f0040 	br	x2
  40053c:	d503201f 	nop
  400540:	d65f03c0 	ret
  400544:	d503201f 	nop

0000000000400548 <__do_global_dtors_aux>:
  400548:	a9be7bfd 	stp	x29, x30, [sp,#-32]!
  40054c:	910003fd 	mov	x29, sp
  400550:	f9000bf3 	str	x19, [sp,#16]
  400554:	90000093 	adrp	x19, 410000 <__FRAME_END__+0xf850>
  400558:	3967ea60 	ldrb	w0, [x19,#2554]
  40055c:	35000080 	cbnz	w0, 40056c <__do_global_dtors_aux+0x24>
  400560:	97ffffdc 	bl	4004d0 <deregister_tm_clones>
  400564:	52800020 	mov	w0, #0x1                   	// #1
  400568:	3927ea60 	strb	w0, [x19,#2554]
  40056c:	f9400bf3 	ldr	x19, [sp,#16]
  400570:	a8c27bfd 	ldp	x29, x30, [sp],#32
  400574:	d65f03c0 	ret

0000000000400578 <frame_dummy>:
  400578:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf850>
  40057c:	911f2000 	add	x0, x0, #0x7c8
  400580:	f9400001 	ldr	x1, [x0]
  400584:	b5000061 	cbnz	x1, 400590 <frame_dummy+0x18>
  400588:	17ffffe0 	b	400508 <register_tm_clones>
  40058c:	d503201f 	nop
  400590:	90000001 	adrp	x1, 400000 <_init-0x3f0>
  400594:	f9433c21 	ldr	x1, [x1,#1656]
  400598:	b4ffff81 	cbz	x1, 400588 <frame_dummy+0x10>
  40059c:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  4005a0:	910003fd 	mov	x29, sp
  4005a4:	d63f0020 	blr	x1
  4005a8:	a8c17bfd 	ldp	x29, x30, [sp],#16
  4005ac:	17ffffd7 	b	400508 <register_tm_clones>

00000000004005b0 <main>:
  4005b0:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  4005b4:	580000a0 	ldr	x0, 4005c8 <main+0x18>
  4005b8:	97ffffaa 	bl	400460 <puts@plt>
  4005bc:	52800540 	mov	w0, #0x2a                  	// #42
  4005c0:	a8c17bfd 	ldp	x29, x30, [sp],#16
  4005c4:	d65f03c0 	ret
  4005c8:	004109ec 	.word	0x004109ec
  4005cc:	00000000 	.word	0x00000000

00000000004005d0 <__libc_csu_init>:
  4005d0:	a9bc7bfd 	stp	x29, x30, [sp,#-64]!
  4005d4:	910003fd 	mov	x29, sp
  4005d8:	a9025bf5 	stp	x21, x22, [sp,#32]
  4005dc:	90000095 	adrp	x21, 410000 <__FRAME_END__+0xf850>
  4005e0:	a90153f3 	stp	x19, x20, [sp,#16]
  4005e4:	90000094 	adrp	x20, 410000 <__FRAME_END__+0xf850>
  4005e8:	911ee2b5 	add	x21, x21, #0x7b8
  4005ec:	911f0294 	add	x20, x20, #0x7c0
  4005f0:	cb150294 	sub	x20, x20, x21
  4005f4:	a90363f7 	stp	x23, x24, [sp,#48]
  4005f8:	aa0203f6 	mov	x22, x2
  4005fc:	2a0003f8 	mov	w24, w0
  400600:	aa0103f7 	mov	x23, x1
  400604:	97ffff7b 	bl	4003f0 <_init>
  400608:	9343fe94 	asr	x20, x20, #3
  40060c:	b4000154 	cbz	x20, 400634 <__libc_csu_init+0x64>
  400610:	d2800013 	mov	x19, #0x0                   	// #0
  400614:	f8737aa3 	ldr	x3, [x21,x19,lsl #3]
  400618:	aa1603e2 	mov	x2, x22
  40061c:	aa1703e1 	mov	x1, x23
  400620:	2a1803e0 	mov	w0, w24
  400624:	91000673 	add	x19, x19, #0x1
  400628:	d63f0060 	blr	x3
  40062c:	eb13029f 	cmp	x20, x19
  400630:	54ffff21 	b.ne	400614 <__libc_csu_init+0x44>
  400634:	a94153f3 	ldp	x19, x20, [sp,#16]
  400638:	a9425bf5 	ldp	x21, x22, [sp,#32]
  40063c:	a94363f7 	ldp	x23, x24, [sp,#48]
  400640:	a8c47bfd 	ldp	x29, x30, [sp],#64
  400644:	d65f03c0 	ret

0000000000400648 <__libc_csu_fini>:
  400648:	d65f03c0 	ret

Disassembly of section .fini:

000000000040064c <_fini>:
  40064c:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  400650:	910003fd 	mov	x29, sp
  400654:	a8c17bfd 	ldp	x29, x30, [sp],#16
  400658:	d65f03c0 	ret
