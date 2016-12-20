
a.out:     file format elf64-littleaarch64
architecture: aarch64, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x0000000000400420

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .interp       0000001b  0000000000400200  0000000000400200  00000200  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .note.ABI-tag 00000020  000000000040021c  000000000040021c  0000021c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .note.gnu.build-id 00000024  000000000040023c  000000000040023c  0000023c  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  3 .gnu.hash     00000028  0000000000400260  0000000000400260  00000260  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .dynsym       00000060  0000000000400288  0000000000400288  00000288  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynstr       0000003d  00000000004002e8  00000000004002e8  000002e8  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .gnu.version  00000008  0000000000400326  0000000000400326  00000326  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version_r 00000020  0000000000400330  0000000000400330  00000330  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .rela.dyn     00000018  0000000000400350  0000000000400350  00000350  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rela.plt     00000048  0000000000400368  0000000000400368  00000368  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .init         00000014  00000000004003b0  00000000004003b0  000003b0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 11 .plt          00000050  00000000004003d0  00000000004003d0  000003d0  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .text         000001c4  0000000000400420  0000000000400420  00000420  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .fini         00000010  00000000004005e4  00000000004005e4  000005e4  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .rodata       00000028  00000000004005f8  00000000004005f8  000005f8  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 15 .eh_frame_hdr 0000003c  0000000000400620  0000000000400620  00000620  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .eh_frame     000000ec  0000000000400660  0000000000400660  00000660  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 17 .init_array   00000008  0000000000410750  0000000000410750  00000750  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 18 .fini_array   00000008  0000000000410758  0000000000410758  00000758  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 19 .jcr          00000008  0000000000410760  0000000000410760  00000760  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 20 .dynamic      000001d0  0000000000410768  0000000000410768  00000768  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 21 .got          00000010  0000000000410938  0000000000410938  00000938  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 22 .got.plt      00000030  0000000000410948  0000000000410948  00000948  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         00000004  0000000000410978  0000000000410978  00000978  2**0
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000004  000000000041097c  000000000041097c  0000097c  2**0
                  ALLOC
 25 .comment      0000002c  0000000000000000  0000000000000000  0000097c  2**0
                  CONTENTS, READONLY
SYMBOL TABLE:
0000000000400200 l    d  .interp	0000000000000000              .interp
000000000040021c l    d  .note.ABI-tag	0000000000000000              .note.ABI-tag
000000000040023c l    d  .note.gnu.build-id	0000000000000000              .note.gnu.build-id
0000000000400260 l    d  .gnu.hash	0000000000000000              .gnu.hash
0000000000400288 l    d  .dynsym	0000000000000000              .dynsym
00000000004002e8 l    d  .dynstr	0000000000000000              .dynstr
0000000000400326 l    d  .gnu.version	0000000000000000              .gnu.version
0000000000400330 l    d  .gnu.version_r	0000000000000000              .gnu.version_r
0000000000400350 l    d  .rela.dyn	0000000000000000              .rela.dyn
0000000000400368 l    d  .rela.plt	0000000000000000              .rela.plt
00000000004003b0 l    d  .init	0000000000000000              .init
00000000004003d0 l    d  .plt	0000000000000000              .plt
0000000000400420 l    d  .text	0000000000000000              .text
00000000004005e4 l    d  .fini	0000000000000000              .fini
00000000004005f8 l    d  .rodata	0000000000000000              .rodata
0000000000400620 l    d  .eh_frame_hdr	0000000000000000              .eh_frame_hdr
0000000000400660 l    d  .eh_frame	0000000000000000              .eh_frame
0000000000410750 l    d  .init_array	0000000000000000              .init_array
0000000000410758 l    d  .fini_array	0000000000000000              .fini_array
0000000000410760 l    d  .jcr	0000000000000000              .jcr
0000000000410768 l    d  .dynamic	0000000000000000              .dynamic
0000000000410938 l    d  .got	0000000000000000              .got
0000000000410948 l    d  .got.plt	0000000000000000              .got.plt
0000000000410978 l    d  .data	0000000000000000              .data
000000000041097c l    d  .bss	0000000000000000              .bss
0000000000000000 l    d  .comment	0000000000000000              .comment
0000000000000000 l    df *ABS*	0000000000000000              /usr/lib/gcc/aarch64-redhat-linux/6.2.1/../../../../lib64/crt1.o
0000000000000000 l    df *ABS*	0000000000000000              /usr/lib/gcc/aarch64-redhat-linux/6.2.1/../../../../lib64/crti.o
0000000000400468 l     F .text	0000000000000014              call_weak_fn
0000000000000000 l    df *ABS*	0000000000000000              /usr/lib/gcc/aarch64-redhat-linux/6.2.1/../../../../lib64/crtn.o
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
0000000000410760 l     O .jcr	0000000000000000              __JCR_LIST__
0000000000400480 l     F .text	0000000000000000              deregister_tm_clones
00000000004004b8 l     F .text	0000000000000000              register_tm_clones
00000000004004f8 l     F .text	0000000000000000              __do_global_dtors_aux
000000000041097c l     O .bss	0000000000000001              completed.7407
0000000000410758 l     O .fini_array	0000000000000000              __do_global_dtors_aux_fini_array_entry
0000000000400528 l     F .text	0000000000000000              frame_dummy
0000000000410750 l     O .init_array	0000000000000000              __frame_dummy_init_array_entry
0000000000000000 l    df *ABS*	0000000000000000              /tmp/ccisEBFT.o
0000000000000000 l    df *ABS*	0000000000000000              elf-init.oS
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
0000000000400748 l     O .eh_frame	0000000000000000              __FRAME_END__
0000000000410760 l     O .jcr	0000000000000000              __JCR_END__
0000000000000000 l    df *ABS*	0000000000000000              
0000000000410758 l       .init_array	0000000000000000              __init_array_end
0000000000410768 l     O .dynamic	0000000000000000              _DYNAMIC
0000000000410750 l       .init_array	0000000000000000              __init_array_start
0000000000400620 l       .eh_frame_hdr	0000000000000000              __GNU_EH_FRAME_HDR
0000000000410938 l     O .got	0000000000000000              _GLOBAL_OFFSET_TABLE_
00000000004005e0 g     F .text	0000000000000004              __libc_csu_fini
0000000000000000  w      *UND*	0000000000000000              _ITM_deregisterTMCloneTable
0000000000410978  w      .data	0000000000000000              data_start
000000000041097c g       .bss	0000000000000000              __bss_start__
0000000000410980 g       .bss	0000000000000000              _bss_end__
000000000041097c g       .data	0000000000000000              _edata
00000000004005e4 g     F .fini	0000000000000000              _fini
0000000000410980 g       .bss	0000000000000000              __bss_end__
0000000000000000       F *UND*	0000000000000000              __libc_start_main@@GLIBC_2.17
0000000000410978 g       .data	0000000000000000              __data_start
0000000000000000  w      *UND*	0000000000000000              __gmon_start__
0000000000400618 g     O .rodata	0000000000000000              .hidden __dso_handle
0000000000000000       F *UND*	0000000000000000              abort@@GLIBC_2.17
00000000004005f8 g     O .rodata	0000000000000004              _IO_stdin_used
0000000000400568 g     F .text	0000000000000078              __libc_csu_init
0000000000410980 g       .bss	0000000000000000              _end
0000000000400420 g     F .text	0000000000000000              _start
0000000000410980 g       .bss	0000000000000000              __end__
000000000041097c g       .bss	0000000000000000              __bss_start
0000000000400560 g       .text	0000000000000000              main
0000000000000000  w      *UND*	0000000000000000              _Jv_RegisterClasses
0000000000410980 g     O .data	0000000000000000              .hidden __TMC_END__
0000000000000000  w      *UND*	0000000000000000              _ITM_registerTMCloneTable
00000000004003b0 g     F .init	0000000000000000              _init



Disassembly of section .init:

00000000004003b0 <_init>:
  4003b0:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  4003b4:	910003fd 	mov	x29, sp
  4003b8:	9400002c 	bl	400468 <call_weak_fn>
  4003bc:	a8c17bfd 	ldp	x29, x30, [sp],#16
  4003c0:	d65f03c0 	ret

Disassembly of section .plt:

00000000004003d0 <__libc_start_main@plt-0x20>:
  4003d0:	a9bf7bf0 	stp	x16, x30, [sp,#-16]!
  4003d4:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf8b8>
  4003d8:	f944ae11 	ldr	x17, [x16,#2392]
  4003dc:	91256210 	add	x16, x16, #0x958
  4003e0:	d61f0220 	br	x17
  4003e4:	d503201f 	nop
  4003e8:	d503201f 	nop
  4003ec:	d503201f 	nop

00000000004003f0 <__libc_start_main@plt>:
  4003f0:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf8b8>
  4003f4:	f944b211 	ldr	x17, [x16,#2400]
  4003f8:	91258210 	add	x16, x16, #0x960
  4003fc:	d61f0220 	br	x17

0000000000400400 <__gmon_start__@plt>:
  400400:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf8b8>
  400404:	f944b611 	ldr	x17, [x16,#2408]
  400408:	9125a210 	add	x16, x16, #0x968
  40040c:	d61f0220 	br	x17

0000000000400410 <abort@plt>:
  400410:	90000090 	adrp	x16, 410000 <__FRAME_END__+0xf8b8>
  400414:	f944ba11 	ldr	x17, [x16,#2416]
  400418:	9125c210 	add	x16, x16, #0x970
  40041c:	d61f0220 	br	x17

Disassembly of section .text:

0000000000400420 <_start>:
  400420:	d280001d 	mov	x29, #0x0                   	// #0
  400424:	d280001e 	mov	x30, #0x0                   	// #0
  400428:	aa0003e5 	mov	x5, x0
  40042c:	f94003e1 	ldr	x1, [sp]
  400430:	910023e2 	add	x2, sp, #0x8
  400434:	910003e6 	mov	x6, sp
  400438:	580000c0 	ldr	x0, 400450 <_start+0x30>
  40043c:	580000e3 	ldr	x3, 400458 <_start+0x38>
  400440:	58000104 	ldr	x4, 400460 <_start+0x40>
  400444:	97ffffeb 	bl	4003f0 <__libc_start_main@plt>
  400448:	97fffff2 	bl	400410 <abort@plt>
  40044c:	00000000 	.word	0x00000000
  400450:	00400560 	.word	0x00400560
  400454:	00000000 	.word	0x00000000
  400458:	00400568 	.word	0x00400568
  40045c:	00000000 	.word	0x00000000
  400460:	004005e0 	.word	0x004005e0
  400464:	00000000 	.word	0x00000000

0000000000400468 <call_weak_fn>:
  400468:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf8b8>
  40046c:	f944a000 	ldr	x0, [x0,#2368]
  400470:	b4000040 	cbz	x0, 400478 <call_weak_fn+0x10>
  400474:	17ffffe3 	b	400400 <__gmon_start__@plt>
  400478:	d65f03c0 	ret
  40047c:	00000000 	.inst	0x00000000 ; undefined

0000000000400480 <deregister_tm_clones>:
  400480:	90000081 	adrp	x1, 410000 <__FRAME_END__+0xf8b8>
  400484:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf8b8>
  400488:	91260021 	add	x1, x1, #0x980
  40048c:	91260000 	add	x0, x0, #0x980
  400490:	91001c21 	add	x1, x1, #0x7
  400494:	cb000021 	sub	x1, x1, x0
  400498:	f100383f 	cmp	x1, #0xe
  40049c:	540000a9 	b.ls	4004b0 <deregister_tm_clones+0x30>
  4004a0:	90000001 	adrp	x1, 400000 <_init-0x3b0>
  4004a4:	f9430021 	ldr	x1, [x1,#1536]
  4004a8:	b4000041 	cbz	x1, 4004b0 <deregister_tm_clones+0x30>
  4004ac:	d61f0020 	br	x1
  4004b0:	d65f03c0 	ret
  4004b4:	d503201f 	nop

00000000004004b8 <register_tm_clones>:
  4004b8:	90000081 	adrp	x1, 410000 <__FRAME_END__+0xf8b8>
  4004bc:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf8b8>
  4004c0:	91260021 	add	x1, x1, #0x980
  4004c4:	91260000 	add	x0, x0, #0x980
  4004c8:	cb000021 	sub	x1, x1, x0
  4004cc:	9343fc21 	asr	x1, x1, #3
  4004d0:	8b41fc21 	add	x1, x1, x1, lsr #63
  4004d4:	9341fc21 	asr	x1, x1, #1
  4004d8:	b40000c1 	cbz	x1, 4004f0 <register_tm_clones+0x38>
  4004dc:	90000002 	adrp	x2, 400000 <_init-0x3b0>
  4004e0:	f9430442 	ldr	x2, [x2,#1544]
  4004e4:	b4000062 	cbz	x2, 4004f0 <register_tm_clones+0x38>
  4004e8:	d61f0040 	br	x2
  4004ec:	d503201f 	nop
  4004f0:	d65f03c0 	ret
  4004f4:	d503201f 	nop

00000000004004f8 <__do_global_dtors_aux>:
  4004f8:	a9be7bfd 	stp	x29, x30, [sp,#-32]!
  4004fc:	910003fd 	mov	x29, sp
  400500:	f9000bf3 	str	x19, [sp,#16]
  400504:	90000093 	adrp	x19, 410000 <__FRAME_END__+0xf8b8>
  400508:	3965f260 	ldrb	w0, [x19,#2428]
  40050c:	35000080 	cbnz	w0, 40051c <__do_global_dtors_aux+0x24>
  400510:	97ffffdc 	bl	400480 <deregister_tm_clones>
  400514:	52800020 	mov	w0, #0x1                   	// #1
  400518:	3925f260 	strb	w0, [x19,#2428]
  40051c:	f9400bf3 	ldr	x19, [sp,#16]
  400520:	a8c27bfd 	ldp	x29, x30, [sp],#32
  400524:	d65f03c0 	ret

0000000000400528 <frame_dummy>:
  400528:	90000080 	adrp	x0, 410000 <__FRAME_END__+0xf8b8>
  40052c:	911d8000 	add	x0, x0, #0x760
  400530:	f9400001 	ldr	x1, [x0]
  400534:	b5000061 	cbnz	x1, 400540 <frame_dummy+0x18>
  400538:	17ffffe0 	b	4004b8 <register_tm_clones>
  40053c:	d503201f 	nop
  400540:	90000001 	adrp	x1, 400000 <_init-0x3b0>
  400544:	f9430821 	ldr	x1, [x1,#1552]
  400548:	b4ffff81 	cbz	x1, 400538 <frame_dummy+0x10>
  40054c:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  400550:	910003fd 	mov	x29, sp
  400554:	d63f0020 	blr	x1
  400558:	a8c17bfd 	ldp	x29, x30, [sp],#16
  40055c:	17ffffd7 	b	4004b8 <register_tm_clones>

0000000000400560 <main>:
  400560:	d2800000 	mov	x0, #0x0                   	// #0
  400564:	d65f03c0 	ret

0000000000400568 <__libc_csu_init>:
  400568:	a9bc7bfd 	stp	x29, x30, [sp,#-64]!
  40056c:	910003fd 	mov	x29, sp
  400570:	a9025bf5 	stp	x21, x22, [sp,#32]
  400574:	90000095 	adrp	x21, 410000 <__FRAME_END__+0xf8b8>
  400578:	a90153f3 	stp	x19, x20, [sp,#16]
  40057c:	90000094 	adrp	x20, 410000 <__FRAME_END__+0xf8b8>
  400580:	911d42b5 	add	x21, x21, #0x750
  400584:	911d6294 	add	x20, x20, #0x758
  400588:	cb150294 	sub	x20, x20, x21
  40058c:	a90363f7 	stp	x23, x24, [sp,#48]
  400590:	aa0203f6 	mov	x22, x2
  400594:	2a0003f8 	mov	w24, w0
  400598:	aa0103f7 	mov	x23, x1
  40059c:	97ffff85 	bl	4003b0 <_init>
  4005a0:	9343fe94 	asr	x20, x20, #3
  4005a4:	b4000154 	cbz	x20, 4005cc <__libc_csu_init+0x64>
  4005a8:	d2800013 	mov	x19, #0x0                   	// #0
  4005ac:	f8737aa3 	ldr	x3, [x21,x19,lsl #3]
  4005b0:	aa1603e2 	mov	x2, x22
  4005b4:	aa1703e1 	mov	x1, x23
  4005b8:	2a1803e0 	mov	w0, w24
  4005bc:	91000673 	add	x19, x19, #0x1
  4005c0:	d63f0060 	blr	x3
  4005c4:	eb13029f 	cmp	x20, x19
  4005c8:	54ffff21 	b.ne	4005ac <__libc_csu_init+0x44>
  4005cc:	a94153f3 	ldp	x19, x20, [sp,#16]
  4005d0:	a9425bf5 	ldp	x21, x22, [sp,#32]
  4005d4:	a94363f7 	ldp	x23, x24, [sp,#48]
  4005d8:	a8c47bfd 	ldp	x29, x30, [sp],#64
  4005dc:	d65f03c0 	ret

00000000004005e0 <__libc_csu_fini>:
  4005e0:	d65f03c0 	ret

Disassembly of section .fini:

00000000004005e4 <_fini>:
  4005e4:	a9bf7bfd 	stp	x29, x30, [sp,#-16]!
  4005e8:	910003fd 	mov	x29, sp
  4005ec:	a8c17bfd 	ldp	x29, x30, [sp],#16
  4005f0:	d65f03c0 	ret
