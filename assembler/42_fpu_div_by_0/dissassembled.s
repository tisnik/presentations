
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000000fa  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000032  00000000  00000000  0000012e  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000004  00000000  00000000  00000160  2**2
                  ALLOC
  3 .debug_line   0000008f  00000000  00000000  00000160  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   0000006f  00000000  00000000  000001ef  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000025e  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000278  2**3
                  CONTENTS, RELOC, READONLY, DEBUGGING
SYMBOL TABLE:
00000000 l    d  .text	00000000 .text
00000000 l    d  .data	00000000 .data
00000000 l    d  .bss	00000000 .bss
00000001 l       *ABS*	00000000 sys_exit
00000004 l       *ABS*	00000000 sys_write
00000001 l       *ABS*	00000000 std_output
00000000 l       .text	00000000 write_message
00000000 l       .data	00000000 printlnMessage
00000002 l       *ABS*	00000000 printlnLength
00000002 l       .data	00000000 hexValueMessage
00000010 l       .data	00000000 hexValueTemplate
00000018 l       *ABS*	00000000 hexValueMessageLen
0000000d l       .text	00000000 hex2string
0000000f l       .text	00000000 print_one_digit
0000001c l       .text	00000000 store_digit
0000001a l       .text	00000000 alpha_digit
0000001a l       .data	00000000 fpuDivideByZeroMessage
00000008 l       *ABS*	00000000 fpuDivideByZeroMessageLength
00000022 l       .data	00000000 fpuDivideByNegativeZeroMessage
00000008 l       *ABS*	00000000 fpuDivideByNegativeZeroMessageLength
0000002a l       .data	00000000 fpuDivideZeroByZeroMessage
00000008 l       *ABS*	00000000 fpuDivideZeroByZeroMessageLength
00000000 l     O .bss	00000004 number
00000000 l    d  .debug_info	00000000 .debug_info
00000000 l    d  .debug_abbrev	00000000 .debug_abbrev
00000000 l    d  .debug_line	00000000 .debug_line
00000000 l    d  .debug_aranges	00000000 .debug_aranges
00000026 g       .text	00000000 _start



Disassembly of section .text:

00000000 <write_message>:
   0:	b8 04 00 00 00       	mov    eax,0x4
   5:	bb 01 00 00 00       	mov    ebx,0x1
   a:	cd 80                	int    0x80
   c:	c3                   	ret    

0000000d <hex2string>:
   d:	b1 08                	mov    cl,0x8

0000000f <print_one_digit>:
   f:	c1 c2 04             	rol    edx,0x4
  12:	88 d0                	mov    al,dl
  14:	24 0f                	and    al,0xf
  16:	3c 0a                	cmp    al,0xa
  18:	7c 02                	jl     1c <store_digit>

0000001a <alpha_digit>:
  1a:	04 07                	add    al,0x7

0000001c <store_digit>:
  1c:	04 30                	add    al,0x30
  1e:	88 03                	mov    BYTE PTR [ebx],al
  20:	43                   	inc    ebx
  21:	fe c9                	dec    cl
  23:	75 ea                	jne    f <print_one_digit>
  25:	c3                   	ret    

00000026 <_start>:
  26:	b9 1a 00 00 00       	mov    ecx,0x1a
  2b:	ba 08 00 00 00       	mov    edx,0x8
  30:	e8 cb ff ff ff       	call   0 <write_message>
  35:	d9 e8                	fld1   
  37:	d9 ee                	fldz   
  39:	de f9                	fdivp  st(1),st
  3b:	d9 1d 00 00 00 00    	fstp   DWORD PTR ds:0x0
  41:	a1 00 00 00 00       	mov    eax,ds:0x0
  46:	60                   	pusha  
  47:	89 c2                	mov    edx,eax
  49:	bb 10 00 00 00       	mov    ebx,0x10
  4e:	e8 ba ff ff ff       	call   d <hex2string>
  53:	b9 02 00 00 00       	mov    ecx,0x2
  58:	ba 18 00 00 00       	mov    edx,0x18
  5d:	e8 9e ff ff ff       	call   0 <write_message>
  62:	61                   	popa   
  63:	b9 22 00 00 00       	mov    ecx,0x22
  68:	ba 08 00 00 00       	mov    edx,0x8
  6d:	e8 8e ff ff ff       	call   0 <write_message>
  72:	d9 e8                	fld1   
  74:	d9 ee                	fldz   
  76:	d9 e0                	fchs   
  78:	de f9                	fdivp  st(1),st
  7a:	d9 1d 00 00 00 00    	fstp   DWORD PTR ds:0x0
  80:	a1 00 00 00 00       	mov    eax,ds:0x0
  85:	60                   	pusha  
  86:	89 c2                	mov    edx,eax
  88:	bb 10 00 00 00       	mov    ebx,0x10
  8d:	e8 7b ff ff ff       	call   d <hex2string>
  92:	b9 02 00 00 00       	mov    ecx,0x2
  97:	ba 18 00 00 00       	mov    edx,0x18
  9c:	e8 5f ff ff ff       	call   0 <write_message>
  a1:	61                   	popa   
  a2:	b9 2a 00 00 00       	mov    ecx,0x2a
  a7:	ba 08 00 00 00       	mov    edx,0x8
  ac:	e8 4f ff ff ff       	call   0 <write_message>
  b1:	d9 ee                	fldz   
  b3:	d9 ee                	fldz   
  b5:	de f9                	fdivp  st(1),st
  b7:	d9 1d 00 00 00 00    	fstp   DWORD PTR ds:0x0
  bd:	a1 00 00 00 00       	mov    eax,ds:0x0
  c2:	60                   	pusha  
  c3:	89 c2                	mov    edx,eax
  c5:	bb 10 00 00 00       	mov    ebx,0x10
  ca:	e8 3e ff ff ff       	call   d <hex2string>
  cf:	b9 02 00 00 00       	mov    ecx,0x2
  d4:	ba 18 00 00 00       	mov    edx,0x18
  d9:	e8 22 ff ff ff       	call   0 <write_message>
  de:	61                   	popa   
  df:	b9 00 00 00 00       	mov    ecx,0x0
  e4:	ba 02 00 00 00       	mov    edx,0x2
  e9:	e8 12 ff ff ff       	call   0 <write_message>
  ee:	b8 01 00 00 00       	mov    eax,0x1
  f3:	bb 00 00 00 00       	mov    ebx,0x0
  f8:	cd 80                	int    0x80
