
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000112:
EXEC_P, HAS_SYMS, D_PAGED
start address 0x0000000000400400

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
  4 .dynsym       00000048  00000000004002b8  00000000004002b8  000002b8  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .dynstr       00000038  0000000000400300  0000000000400300  00000300  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .gnu.version  00000006  0000000000400338  0000000000400338  00000338  2**1
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .gnu.version_r 00000020  0000000000400340  0000000000400340  00000340  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  8 .rela.dyn     00000018  0000000000400360  0000000000400360  00000360  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  9 .rela.plt     00000030  0000000000400378  0000000000400378  00000378  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 10 .init         0000001a  00000000004003a8  00000000004003a8  000003a8  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 11 .plt          00000030  00000000004003d0  00000000004003d0  000003d0  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 12 .text         00000162  0000000000400400  0000000000400400  00000400  2**4
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 13 .fini         00000009  0000000000400564  0000000000400564  00000564  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
 14 .rodata       00000004  0000000000400570  0000000000400570  00000570  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 15 .eh_frame_hdr 0000002c  0000000000400574  0000000000400574  00000574  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
 16 .eh_frame     000000d4  00000000004005a0  00000000004005a0  000005a0  2**3
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
 22 .got.plt      00000028  0000000000601000  0000000000601000  00001000  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 23 .data         00000010  0000000000601028  0000000000601028  00001028  2**3
                  CONTENTS, ALLOC, LOAD, DATA
 24 .bss          00000008  0000000000601038  0000000000601038  00001038  2**0
                  ALLOC
 25 .comment      0000002b  0000000000000000  0000000000000000  00001038  2**0
                  CONTENTS, READONLY
SYMBOL TABLE:
0000000000400238 l    d  .interp	0000000000000000              .interp
0000000000400254 l    d  .note.ABI-tag	0000000000000000              .note.ABI-tag
0000000000400274 l    d  .note.gnu.build-id	0000000000000000              .note.gnu.build-id
0000000000400298 l    d  .gnu.hash	0000000000000000              .gnu.hash
00000000004002b8 l    d  .dynsym	0000000000000000              .dynsym
0000000000400300 l    d  .dynstr	0000000000000000              .dynstr
0000000000400338 l    d  .gnu.version	0000000000000000              .gnu.version
0000000000400340 l    d  .gnu.version_r	0000000000000000              .gnu.version_r
0000000000400360 l    d  .rela.dyn	0000000000000000              .rela.dyn
0000000000400378 l    d  .rela.plt	0000000000000000              .rela.plt
00000000004003a8 l    d  .init	0000000000000000              .init
00000000004003d0 l    d  .plt	0000000000000000              .plt
0000000000400400 l    d  .text	0000000000000000              .text
0000000000400564 l    d  .fini	0000000000000000              .fini
0000000000400570 l    d  .rodata	0000000000000000              .rodata
0000000000400574 l    d  .eh_frame_hdr	0000000000000000              .eh_frame_hdr
00000000004005a0 l    d  .eh_frame	0000000000000000              .eh_frame
0000000000600e10 l    d  .init_array	0000000000000000              .init_array
0000000000600e18 l    d  .fini_array	0000000000000000              .fini_array
0000000000600e20 l    d  .jcr	0000000000000000              .jcr
0000000000600e28 l    d  .dynamic	0000000000000000              .dynamic
0000000000600ff8 l    d  .got	0000000000000000              .got
0000000000601000 l    d  .got.plt	0000000000000000              .got.plt
0000000000601028 l    d  .data	0000000000000000              .data
0000000000601038 l    d  .bss	0000000000000000              .bss
0000000000000000 l    d  .comment	0000000000000000              .comment
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
0000000000600e20 l     O .jcr	0000000000000000              __JCR_LIST__
0000000000400430 l     F .text	0000000000000000              deregister_tm_clones
0000000000400460 l     F .text	0000000000000000              register_tm_clones
00000000004004a0 l     F .text	0000000000000000              __do_global_dtors_aux
0000000000601038 l     O .bss	0000000000000001              completed.6973
0000000000600e18 l     O .fini_array	0000000000000000              __do_global_dtors_aux_fini_array_entry
00000000004004c0 l     F .text	0000000000000000              frame_dummy
0000000000600e10 l     O .init_array	0000000000000000              __frame_dummy_init_array_entry
0000000000000000 l    df *ABS*	0000000000000000              crtstuff.c
0000000000400670 l     O .eh_frame	0000000000000000              __FRAME_END__
0000000000600e20 l     O .jcr	0000000000000000              __JCR_END__
0000000000000000 l    df *ABS*	0000000000000000              
0000000000600e18 l       .init_array	0000000000000000              __init_array_end
0000000000600e28 l     O .dynamic	0000000000000000              _DYNAMIC
0000000000600e10 l       .init_array	0000000000000000              __init_array_start
0000000000601000 l     O .got.plt	0000000000000000              _GLOBAL_OFFSET_TABLE_
0000000000400560 g     F .text	0000000000000002              __libc_csu_fini
0000000000000000  w      *UND*	0000000000000000              _ITM_deregisterTMCloneTable
0000000000601028  w      .data	0000000000000000              data_start
0000000000601038 g       .data	0000000000000000              _edata
0000000000400564 g     F .fini	0000000000000000              _fini
0000000000000000       F *UND*	0000000000000000              __libc_start_main@@GLIBC_2.2.5
0000000000601028 g       .data	0000000000000000              __data_start
0000000000000000  w      *UND*	0000000000000000              __gmon_start__
0000000000601030 g     O .data	0000000000000000              .hidden __dso_handle
0000000000400570 g     O .rodata	0000000000000004              _IO_stdin_used
00000000004004f0 g     F .text	0000000000000065              __libc_csu_init
0000000000601040 g       .bss	0000000000000000              _end
0000000000400400 g     F .text	0000000000000000              _start
0000000000601038 g       .bss	0000000000000000              __bss_start
00000000004004ed g       .text	0000000000000000              main
0000000000000000  w      *UND*	0000000000000000              _Jv_RegisterClasses
0000000000601038 g     O .data	0000000000000000              .hidden __TMC_END__
0000000000000000  w      *UND*	0000000000000000              _ITM_registerTMCloneTable
00000000004003a8 g     F .init	0000000000000000              _init



Disassembly of section .init:

00000000004003a8 <_init>:
  4003a8:	48 83 ec 08          	sub    rsp,0x8
  4003ac:	48 8b 05 45 0c 20 00 	mov    rax,QWORD PTR [rip+0x200c45]        # 600ff8 <_DYNAMIC+0x1d0>
  4003b3:	48 85 c0             	test   rax,rax
  4003b6:	74 05                	je     4003bd <_init+0x15>
  4003b8:	e8 33 00 00 00       	call   4003f0 <__gmon_start__@plt>
  4003bd:	48 83 c4 08          	add    rsp,0x8
  4003c1:	c3                   	ret    

Disassembly of section .plt:

00000000004003d0 <__libc_start_main@plt-0x10>:
  4003d0:	ff 35 32 0c 20 00    	push   QWORD PTR [rip+0x200c32]        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  4003d6:	ff 25 34 0c 20 00    	jmp    QWORD PTR [rip+0x200c34]        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  4003dc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

00000000004003e0 <__libc_start_main@plt>:
  4003e0:	ff 25 32 0c 20 00    	jmp    QWORD PTR [rip+0x200c32]        # 601018 <_GLOBAL_OFFSET_TABLE_+0x18>
  4003e6:	68 00 00 00 00       	push   0x0
  4003eb:	e9 e0 ff ff ff       	jmp    4003d0 <_init+0x28>

00000000004003f0 <__gmon_start__@plt>:
  4003f0:	ff 25 2a 0c 20 00    	jmp    QWORD PTR [rip+0x200c2a]        # 601020 <_GLOBAL_OFFSET_TABLE_+0x20>
  4003f6:	68 01 00 00 00       	push   0x1
  4003fb:	e9 d0 ff ff ff       	jmp    4003d0 <_init+0x28>

Disassembly of section .text:

0000000000400400 <_start>:
  400400:	31 ed                	xor    ebp,ebp
  400402:	49 89 d1             	mov    r9,rdx
  400405:	5e                   	pop    rsi
  400406:	48 89 e2             	mov    rdx,rsp
  400409:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
  40040d:	50                   	push   rax
  40040e:	54                   	push   rsp
  40040f:	49 c7 c0 60 05 40 00 	mov    r8,0x400560
  400416:	48 c7 c1 f0 04 40 00 	mov    rcx,0x4004f0
  40041d:	48 c7 c7 ed 04 40 00 	mov    rdi,0x4004ed
  400424:	e8 b7 ff ff ff       	call   4003e0 <__libc_start_main@plt>
  400429:	f4                   	hlt    
  40042a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]

0000000000400430 <deregister_tm_clones>:
  400430:	b8 3f 10 60 00       	mov    eax,0x60103f
  400435:	55                   	push   rbp
  400436:	48 2d 38 10 60 00    	sub    rax,0x601038
  40043c:	48 83 f8 0e          	cmp    rax,0xe
  400440:	48 89 e5             	mov    rbp,rsp
  400443:	77 02                	ja     400447 <deregister_tm_clones+0x17>
  400445:	5d                   	pop    rbp
  400446:	c3                   	ret    
  400447:	b8 00 00 00 00       	mov    eax,0x0
  40044c:	48 85 c0             	test   rax,rax
  40044f:	74 f4                	je     400445 <deregister_tm_clones+0x15>
  400451:	5d                   	pop    rbp
  400452:	bf 38 10 60 00       	mov    edi,0x601038
  400457:	ff e0                	jmp    rax
  400459:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000400460 <register_tm_clones>:
  400460:	b8 38 10 60 00       	mov    eax,0x601038
  400465:	55                   	push   rbp
  400466:	48 2d 38 10 60 00    	sub    rax,0x601038
  40046c:	48 c1 f8 03          	sar    rax,0x3
  400470:	48 89 e5             	mov    rbp,rsp
  400473:	48 89 c2             	mov    rdx,rax
  400476:	48 c1 ea 3f          	shr    rdx,0x3f
  40047a:	48 01 d0             	add    rax,rdx
  40047d:	48 d1 f8             	sar    rax,1
  400480:	75 02                	jne    400484 <register_tm_clones+0x24>
  400482:	5d                   	pop    rbp
  400483:	c3                   	ret    
  400484:	ba 00 00 00 00       	mov    edx,0x0
  400489:	48 85 d2             	test   rdx,rdx
  40048c:	74 f4                	je     400482 <register_tm_clones+0x22>
  40048e:	5d                   	pop    rbp
  40048f:	48 89 c6             	mov    rsi,rax
  400492:	bf 38 10 60 00       	mov    edi,0x601038
  400497:	ff e2                	jmp    rdx
  400499:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

00000000004004a0 <__do_global_dtors_aux>:
  4004a0:	80 3d 91 0b 20 00 00 	cmp    BYTE PTR [rip+0x200b91],0x0        # 601038 <__TMC_END__>
  4004a7:	75 11                	jne    4004ba <__do_global_dtors_aux+0x1a>
  4004a9:	55                   	push   rbp
  4004aa:	48 89 e5             	mov    rbp,rsp
  4004ad:	e8 7e ff ff ff       	call   400430 <deregister_tm_clones>
  4004b2:	5d                   	pop    rbp
  4004b3:	c6 05 7e 0b 20 00 01 	mov    BYTE PTR [rip+0x200b7e],0x1        # 601038 <__TMC_END__>
  4004ba:	f3 c3                	repz ret 
  4004bc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

00000000004004c0 <frame_dummy>:
  4004c0:	48 83 3d 58 09 20 00 	cmp    QWORD PTR [rip+0x200958],0x0        # 600e20 <__JCR_END__>
  4004c7:	00 
  4004c8:	74 1e                	je     4004e8 <frame_dummy+0x28>
  4004ca:	b8 00 00 00 00       	mov    eax,0x0
  4004cf:	48 85 c0             	test   rax,rax
  4004d2:	74 14                	je     4004e8 <frame_dummy+0x28>
  4004d4:	55                   	push   rbp
  4004d5:	bf 20 0e 60 00       	mov    edi,0x600e20
  4004da:	48 89 e5             	mov    rbp,rsp
  4004dd:	ff d0                	call   rax
  4004df:	5d                   	pop    rbp
  4004e0:	e9 7b ff ff ff       	jmp    400460 <register_tm_clones>
  4004e5:	0f 1f 00             	nop    DWORD PTR [rax]
  4004e8:	e9 73 ff ff ff       	jmp    400460 <register_tm_clones>

00000000004004ed <main>:
  4004ed:	31 c0                	xor    eax,eax
  4004ef:	c3                   	ret    

00000000004004f0 <__libc_csu_init>:
  4004f0:	41 57                	push   r15
  4004f2:	41 89 ff             	mov    r15d,edi
  4004f5:	41 56                	push   r14
  4004f7:	49 89 f6             	mov    r14,rsi
  4004fa:	41 55                	push   r13
  4004fc:	49 89 d5             	mov    r13,rdx
  4004ff:	41 54                	push   r12
  400501:	4c 8d 25 08 09 20 00 	lea    r12,[rip+0x200908]        # 600e10 <__frame_dummy_init_array_entry>
  400508:	55                   	push   rbp
  400509:	48 8d 2d 08 09 20 00 	lea    rbp,[rip+0x200908]        # 600e18 <__init_array_end>
  400510:	53                   	push   rbx
  400511:	4c 29 e5             	sub    rbp,r12
  400514:	31 db                	xor    ebx,ebx
  400516:	48 c1 fd 03          	sar    rbp,0x3
  40051a:	48 83 ec 08          	sub    rsp,0x8
  40051e:	e8 85 fe ff ff       	call   4003a8 <_init>
  400523:	48 85 ed             	test   rbp,rbp
  400526:	74 1e                	je     400546 <__libc_csu_init+0x56>
  400528:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
  40052f:	00 
  400530:	4c 89 ea             	mov    rdx,r13
  400533:	4c 89 f6             	mov    rsi,r14
  400536:	44 89 ff             	mov    edi,r15d
  400539:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
  40053d:	48 83 c3 01          	add    rbx,0x1
  400541:	48 39 eb             	cmp    rbx,rbp
  400544:	75 ea                	jne    400530 <__libc_csu_init+0x40>
  400546:	48 83 c4 08          	add    rsp,0x8
  40054a:	5b                   	pop    rbx
  40054b:	5d                   	pop    rbp
  40054c:	41 5c                	pop    r12
  40054e:	41 5d                	pop    r13
  400550:	41 5e                	pop    r14
  400552:	41 5f                	pop    r15
  400554:	c3                   	ret    
  400555:	66 66 2e 0f 1f 84 00 	data32 nop WORD PTR cs:[rax+rax*1+0x0]
  40055c:	00 00 00 00 

0000000000400560 <__libc_csu_fini>:
  400560:	f3 c3                	repz ret 

Disassembly of section .fini:

0000000000400564 <_fini>:
  400564:	48 83 ec 08          	sub    rsp,0x8
  400568:	48 83 c4 08          	add    rsp,0x8
  40056c:	c3                   	ret    
