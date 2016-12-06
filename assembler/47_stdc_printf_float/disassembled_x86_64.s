
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x0000000000400440

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .interp       0000001c  0000000000400238  0000000000400238  00000238  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .note.ABI-tag 00000020  0000000000400254  0000000000400254  00000254  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .note.gnu.build-id 00000024  0000000000400274  0000000000400274  00000274  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  3 .gnu.hash     0000001c  0000000000400298  0000000000400298  00000298  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .dynsym       00000060  00000000004002b8  00000000004002b8  000002b8  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynstr       0000003f  0000000000400318  0000000000400318  00000318  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .gnu.version  00000008  0000000000400358  0000000000400358  00000358  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version_r 00000020  0000000000400360  0000000000400360  00000360  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .rela.dyn     00000018  0000000000400380  0000000000400380  00000380  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rela.plt     00000048  0000000000400398  0000000000400398  00000398  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .init         0000001a  00000000004003e0  00000000004003e0  000003e0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 11 .plt          00000040  0000000000400400  0000000000400400  00000400  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .text         00000192  0000000000400440  0000000000400440  00000440  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .fini         00000009  00000000004005d4  00000000004005d4  000005d4  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .rodata       00000004  00000000004005e0  00000000004005e0  000005e0  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 15 .eh_frame_hdr 0000002c  00000000004005e4  00000000004005e4  000005e4  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .eh_frame     000000d4  0000000000400610  0000000000400610  00000610  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 17 .init_array   00000008  0000000000600e10  0000000000600e10  00000e10  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 18 .fini_array   00000008  0000000000600e18  0000000000600e18  00000e18  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 19 .jcr          00000008  0000000000600e20  0000000000600e20  00000e20  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 20 .dynamic      000001d0  0000000000600e28  0000000000600e28  00000e28  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 21 .got          00000008  0000000000600ff8  0000000000600ff8  00000ff8  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 22 .got.plt      00000030  0000000000601000  0000000000601000  00001000  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         0000001c  0000000000601030  0000000000601030  00001030  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000010  0000000000601050  0000000000601050  0000104c  2**3
                  ALLOC
 25 .comment      0000002b  0000000000000000  0000000000000000  0000104c  2**0
                  CONTENTS, READONLY
SYMBOL TABLE:
0000000000400238 l    d  .interp	0000000000000000              .interp
0000000000400254 l    d  .note.ABI-tag	0000000000000000              .note.ABI-tag
0000000000400274 l    d  .note.gnu.build-id	0000000000000000              .note.gnu.build-id
0000000000400298 l    d  .gnu.hash	0000000000000000              .gnu.hash
00000000004002b8 l    d  .dynsym	0000000000000000              .dynsym
0000000000400318 l    d  .dynstr	0000000000000000              .dynstr
0000000000400358 l    d  .gnu.version	0000000000000000              .gnu.version
0000000000400360 l    d  .gnu.version_r	0000000000000000              .gnu.version_r
0000000000400380 l    d  .rela.dyn	0000000000000000              .rela.dyn
0000000000400398 l    d  .rela.plt	0000000000000000              .rela.plt
00000000004003e0 l    d  .init	0000000000000000              .init
0000000000400400 l    d  .plt	0000000000000000              .plt
0000000000400440 l    d  .text	0000000000000000              .text
00000000004005d4 l    d  .fini	0000000000000000              .fini
00000000004005e0 l    d  .rodata	0000000000000000              .rodata
00000000004005e4 l    d  .eh_frame_hdr	0000000000000000              .eh_frame_hdr
0000000000400610 l    d  .eh_frame	0000000000000000              .eh_frame
0000000000600e10 l    d  .init_array	0000000000000000              .init_array
0000000000600e18 l    d  .fini_array	0000000000000000              .fini_array
0000000000600e20 l    d  .jcr	0000000000000000              .jcr
0000000000600e28 l    d  .dynamic	0000000000000000              .dynamic
0000000000600ff8 l    d  .got	0000000000000000              .got
0000000000601000 l    d  .got.plt	0000000000000000              .got.plt
0000000000601030 l    d  .data	0000000000000000              .data
0000000000601050 l    d  .bss	0000000000000000              .bss
0000000000000000 l    d  .comment	0000000000000000              .comment
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
0000000000600e20 l     O .jcr	0000000000000000              __JCR_LIST__
0000000000400470 l     F .text	0000000000000000              deregister_tm_clones
00000000004004a0 l     F .text	0000000000000000              register_tm_clones
00000000004004e0 l     F .text	0000000000000000              __do_global_dtors_aux
0000000000601050 l     O .bss	0000000000000001              completed.6973
0000000000600e18 l     O .fini_array	0000000000000000              __do_global_dtors_aux_fini_array_entry
0000000000400500 l     F .text	0000000000000000              frame_dummy
0000000000600e10 l     O .init_array	0000000000000000              __frame_dummy_init_array_entry
0000000000000000 l    df *ABS*	0000000000000000              /tmp/ccY2udek.o
0000000000601040 l       .data	0000000000000000              hello_world_message
0000000000601058 l     O .bss	0000000000000008              number
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
00000000004006e0 l     O .eh_frame	0000000000000000              __FRAME_END__
0000000000600e20 l     O .jcr	0000000000000000              __JCR_END__
0000000000000000 l    df *ABS*	0000000000000000              
0000000000600e18 l       .init_array	0000000000000000              __init_array_end
0000000000600e28 l     O .dynamic	0000000000000000              _DYNAMIC
0000000000600e10 l       .init_array	0000000000000000              __init_array_start
0000000000601000 l     O .got.plt	0000000000000000              _GLOBAL_OFFSET_TABLE_
00000000004005d0 g     F .text	0000000000000002              __libc_csu_fini
0000000000000000  w      *UND*	0000000000000000              _ITM_deregisterTMCloneTable
0000000000601030  w      .data	0000000000000000              data_start
000000000060104c g       .data	0000000000000000              _edata
00000000004005d4 g     F .fini	0000000000000000              _fini
0000000000000000       F *UND*	0000000000000000              printf@@GLIBC_2.2.5
0000000000000000       F *UND*	0000000000000000              __libc_start_main@@GLIBC_2.2.5
0000000000601030 g       .data	0000000000000000              __data_start
0000000000000000  w      *UND*	0000000000000000              __gmon_start__
0000000000601038 g     O .data	0000000000000000              .hidden __dso_handle
00000000004005e0 g     O .rodata	0000000000000004              _IO_stdin_used
0000000000400560 g     F .text	0000000000000065              __libc_csu_init
0000000000601060 g       .bss	0000000000000000              _end
0000000000400440 g     F .text	0000000000000000              _start
000000000060104c g       .bss	0000000000000000              __bss_start
000000000040052d g       .text	0000000000000000              main
0000000000000000  w      *UND*	0000000000000000              _Jv_RegisterClasses
0000000000601050 g     O .data	0000000000000000              .hidden __TMC_END__
0000000000000000  w      *UND*	0000000000000000              _ITM_registerTMCloneTable
00000000004003e0 g     F .init	0000000000000000              _init



Disassembly of section .init:

00000000004003e0 <_init>:
  4003e0:	48 83 ec 08          	sub    rsp,0x8
  4003e4:	48 8b 05 0d 0c 20 00 	mov    rax,QWORD PTR [rip+0x200c0d]        # 600ff8 <_DYNAMIC+0x1d0>
  4003eb:	48 85 c0             	test   rax,rax
  4003ee:	74 05                	je     4003f5 <_init+0x15>
  4003f0:	e8 3b 00 00 00       	call   400430 <__gmon_start__@plt>
  4003f5:	48 83 c4 08          	add    rsp,0x8
  4003f9:	c3                   	ret    

Disassembly of section .plt:

0000000000400400 <printf@plt-0x10>:
  400400:	ff 35 02 0c 20 00    	push   QWORD PTR [rip+0x200c02]        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400406:	ff 25 04 0c 20 00    	jmp    QWORD PTR [rip+0x200c04]        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40040c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000400410 <printf@plt>:
  400410:	ff 25 02 0c 20 00    	jmp    QWORD PTR [rip+0x200c02]        # 601018 <_GLOBAL_OFFSET_TABLE_+0x18>
  400416:	68 00 00 00 00       	push   0x0
  40041b:	e9 e0 ff ff ff       	jmp    400400 <_init+0x20>

0000000000400420 <__libc_start_main@plt>:
  400420:	ff 25 fa 0b 20 00    	jmp    QWORD PTR [rip+0x200bfa]        # 601020 <_GLOBAL_OFFSET_TABLE_+0x20>
  400426:	68 01 00 00 00       	push   0x1
  40042b:	e9 d0 ff ff ff       	jmp    400400 <_init+0x20>

0000000000400430 <__gmon_start__@plt>:
  400430:	ff 25 f2 0b 20 00    	jmp    QWORD PTR [rip+0x200bf2]        # 601028 <_GLOBAL_OFFSET_TABLE_+0x28>
  400436:	68 02 00 00 00       	push   0x2
  40043b:	e9 c0 ff ff ff       	jmp    400400 <_init+0x20>

Disassembly of section .text:

0000000000400440 <_start>:
  400440:	31 ed                	xor    ebp,ebp
  400442:	49 89 d1             	mov    r9,rdx
  400445:	5e                   	pop    rsi
  400446:	48 89 e2             	mov    rdx,rsp
  400449:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
  40044d:	50                   	push   rax
  40044e:	54                   	push   rsp
  40044f:	49 c7 c0 d0 05 40 00 	mov    r8,0x4005d0
  400456:	48 c7 c1 60 05 40 00 	mov    rcx,0x400560
  40045d:	48 c7 c7 2d 05 40 00 	mov    rdi,0x40052d
  400464:	e8 b7 ff ff ff       	call   400420 <__libc_start_main@plt>
  400469:	f4                   	hlt    
  40046a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]

0000000000400470 <deregister_tm_clones>:
  400470:	b8 57 10 60 00       	mov    eax,0x601057
  400475:	55                   	push   rbp
  400476:	48 2d 50 10 60 00    	sub    rax,0x601050
  40047c:	48 83 f8 0e          	cmp    rax,0xe
  400480:	48 89 e5             	mov    rbp,rsp
  400483:	77 02                	ja     400487 <deregister_tm_clones+0x17>
  400485:	5d                   	pop    rbp
  400486:	c3                   	ret    
  400487:	b8 00 00 00 00       	mov    eax,0x0
  40048c:	48 85 c0             	test   rax,rax
  40048f:	74 f4                	je     400485 <deregister_tm_clones+0x15>
  400491:	5d                   	pop    rbp
  400492:	bf 50 10 60 00       	mov    edi,0x601050
  400497:	ff e0                	jmp    rax
  400499:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

00000000004004a0 <register_tm_clones>:
  4004a0:	b8 50 10 60 00       	mov    eax,0x601050
  4004a5:	55                   	push   rbp
  4004a6:	48 2d 50 10 60 00    	sub    rax,0x601050
  4004ac:	48 c1 f8 03          	sar    rax,0x3
  4004b0:	48 89 e5             	mov    rbp,rsp
  4004b3:	48 89 c2             	mov    rdx,rax
  4004b6:	48 c1 ea 3f          	shr    rdx,0x3f
  4004ba:	48 01 d0             	add    rax,rdx
  4004bd:	48 d1 f8             	sar    rax,1
  4004c0:	75 02                	jne    4004c4 <register_tm_clones+0x24>
  4004c2:	5d                   	pop    rbp
  4004c3:	c3                   	ret    
  4004c4:	ba 00 00 00 00       	mov    edx,0x0
  4004c9:	48 85 d2             	test   rdx,rdx
  4004cc:	74 f4                	je     4004c2 <register_tm_clones+0x22>
  4004ce:	5d                   	pop    rbp
  4004cf:	48 89 c6             	mov    rsi,rax
  4004d2:	bf 50 10 60 00       	mov    edi,0x601050
  4004d7:	ff e2                	jmp    rdx
  4004d9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

00000000004004e0 <__do_global_dtors_aux>:
  4004e0:	80 3d 69 0b 20 00 00 	cmp    BYTE PTR [rip+0x200b69],0x0        # 601050 <__TMC_END__>
  4004e7:	75 11                	jne    4004fa <__do_global_dtors_aux+0x1a>
  4004e9:	55                   	push   rbp
  4004ea:	48 89 e5             	mov    rbp,rsp
  4004ed:	e8 7e ff ff ff       	call   400470 <deregister_tm_clones>
  4004f2:	5d                   	pop    rbp
  4004f3:	c6 05 56 0b 20 00 01 	mov    BYTE PTR [rip+0x200b56],0x1        # 601050 <__TMC_END__>
  4004fa:	f3 c3                	repz ret 
  4004fc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000400500 <frame_dummy>:
  400500:	48 83 3d 18 09 20 00 	cmp    QWORD PTR [rip+0x200918],0x0        # 600e20 <__JCR_END__>
  400507:	00 
  400508:	74 1e                	je     400528 <frame_dummy+0x28>
  40050a:	b8 00 00 00 00       	mov    eax,0x0
  40050f:	48 85 c0             	test   rax,rax
  400512:	74 14                	je     400528 <frame_dummy+0x28>
  400514:	55                   	push   rbp
  400515:	bf 20 0e 60 00       	mov    edi,0x600e20
  40051a:	48 89 e5             	mov    rbp,rsp
  40051d:	ff d0                	call   rax
  40051f:	5d                   	pop    rbp
  400520:	e9 7b ff ff ff       	jmp    4004a0 <register_tm_clones>
  400525:	0f 1f 00             	nop    DWORD PTR [rax]
  400528:	e9 73 ff ff ff       	jmp    4004a0 <register_tm_clones>

000000000040052d <main>:
  40052d:	48 83 ec 08          	sub    rsp,0x8
  400531:	48 c7 c7 40 10 60 00 	mov    rdi,0x601040
  400538:	d9 eb                	fldpi  
  40053a:	dd 1c 25 58 10 60 00 	fstp   QWORD PTR ds:0x601058
  400541:	f2 0f 10 04 25 58 10 	movsd  xmm0,QWORD PTR ds:0x601058
  400548:	60 00 
  40054a:	b8 01 00 00 00       	mov    eax,0x1
  40054f:	e8 bc fe ff ff       	call   400410 <printf@plt>
  400554:	48 83 c4 08          	add    rsp,0x8
  400558:	31 c0                	xor    eax,eax
  40055a:	c3                   	ret    
  40055b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000400560 <__libc_csu_init>:
  400560:	41 57                	push   r15
  400562:	41 89 ff             	mov    r15d,edi
  400565:	41 56                	push   r14
  400567:	49 89 f6             	mov    r14,rsi
  40056a:	41 55                	push   r13
  40056c:	49 89 d5             	mov    r13,rdx
  40056f:	41 54                	push   r12
  400571:	4c 8d 25 98 08 20 00 	lea    r12,[rip+0x200898]        # 600e10 <__frame_dummy_init_array_entry>
  400578:	55                   	push   rbp
  400579:	48 8d 2d 98 08 20 00 	lea    rbp,[rip+0x200898]        # 600e18 <__init_array_end>
  400580:	53                   	push   rbx
  400581:	4c 29 e5             	sub    rbp,r12
  400584:	31 db                	xor    ebx,ebx
  400586:	48 c1 fd 03          	sar    rbp,0x3
  40058a:	48 83 ec 08          	sub    rsp,0x8
  40058e:	e8 4d fe ff ff       	call   4003e0 <_init>
  400593:	48 85 ed             	test   rbp,rbp
  400596:	74 1e                	je     4005b6 <__libc_csu_init+0x56>
  400598:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
  40059f:	00 
  4005a0:	4c 89 ea             	mov    rdx,r13
  4005a3:	4c 89 f6             	mov    rsi,r14
  4005a6:	44 89 ff             	mov    edi,r15d
  4005a9:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
  4005ad:	48 83 c3 01          	add    rbx,0x1
  4005b1:	48 39 eb             	cmp    rbx,rbp
  4005b4:	75 ea                	jne    4005a0 <__libc_csu_init+0x40>
  4005b6:	48 83 c4 08          	add    rsp,0x8
  4005ba:	5b                   	pop    rbx
  4005bb:	5d                   	pop    rbp
  4005bc:	41 5c                	pop    r12
  4005be:	41 5d                	pop    r13
  4005c0:	41 5e                	pop    r14
  4005c2:	41 5f                	pop    r15
  4005c4:	c3                   	ret    
  4005c5:	66 66 2e 0f 1f 84 00 	data32 nop WORD PTR cs:[rax+rax*1+0x0]
  4005cc:	00 00 00 00 

00000000004005d0 <__libc_csu_fini>:
  4005d0:	f3 c3                	repz ret 

Disassembly of section .fini:

00000000004005d4 <_fini>:
  4005d4:	48 83 ec 08          	sub    rsp,0x8
  4005d8:	48 83 c4 08          	add    rsp,0x8
  4005dc:	c3                   	ret    
