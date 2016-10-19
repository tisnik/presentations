
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         00000110  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         0000001a  00000000  00000000  00000144  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  0000015e  2**0
                  ALLOC
  3 .debug_line   00000089  00000000  00000000  0000015e  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000068  00000000  00000000  000001e7  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000024f  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000268  2**3
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
  26:	b8 78 56 34 12       	mov    eax,0x12345678
  2b:	60                   	pusha  
  2c:	89 c2                	mov    edx,eax
  2e:	bb 10 00 00 00       	mov    ebx,0x10
  33:	e8 d5 ff ff ff       	call   d <hex2string>
  38:	b9 02 00 00 00       	mov    ecx,0x2
  3d:	ba 18 00 00 00       	mov    edx,0x18
  42:	e8 b9 ff ff ff       	call   0 <write_message>
  47:	61                   	popa   
  48:	0f c8                	bswap  eax
  4a:	60                   	pusha  
  4b:	89 c2                	mov    edx,eax
  4d:	bb 10 00 00 00       	mov    ebx,0x10
  52:	e8 b6 ff ff ff       	call   d <hex2string>
  57:	b9 02 00 00 00       	mov    ecx,0x2
  5c:	ba 18 00 00 00       	mov    edx,0x18
  61:	e8 9a ff ff ff       	call   0 <write_message>
  66:	61                   	popa   
  67:	0f c8                	bswap  eax
  69:	60                   	pusha  
  6a:	89 c2                	mov    edx,eax
  6c:	bb 10 00 00 00       	mov    ebx,0x10
  71:	e8 97 ff ff ff       	call   d <hex2string>
  76:	b9 02 00 00 00       	mov    ecx,0x2
  7b:	ba 18 00 00 00       	mov    edx,0x18
  80:	e8 7b ff ff ff       	call   0 <write_message>
  85:	61                   	popa   
  86:	b9 00 00 00 00       	mov    ecx,0x0
  8b:	ba 02 00 00 00       	mov    edx,0x2
  90:	e8 6b ff ff ff       	call   0 <write_message>
  95:	b8 ff 00 00 00       	mov    eax,0xff
  9a:	60                   	pusha  
  9b:	89 c2                	mov    edx,eax
  9d:	bb 10 00 00 00       	mov    ebx,0x10
  a2:	e8 66 ff ff ff       	call   d <hex2string>
  a7:	b9 02 00 00 00       	mov    ecx,0x2
  ac:	ba 18 00 00 00       	mov    edx,0x18
  b1:	e8 4a ff ff ff       	call   0 <write_message>
  b6:	61                   	popa   
  b7:	0f c8                	bswap  eax
  b9:	60                   	pusha  
  ba:	89 c2                	mov    edx,eax
  bc:	bb 10 00 00 00       	mov    ebx,0x10
  c1:	e8 47 ff ff ff       	call   d <hex2string>
  c6:	b9 02 00 00 00       	mov    ecx,0x2
  cb:	ba 18 00 00 00       	mov    edx,0x18
  d0:	e8 2b ff ff ff       	call   0 <write_message>
  d5:	61                   	popa   
  d6:	0f c8                	bswap  eax
  d8:	60                   	pusha  
  d9:	89 c2                	mov    edx,eax
  db:	bb 10 00 00 00       	mov    ebx,0x10
  e0:	e8 28 ff ff ff       	call   d <hex2string>
  e5:	b9 02 00 00 00       	mov    ecx,0x2
  ea:	ba 18 00 00 00       	mov    edx,0x18
  ef:	e8 0c ff ff ff       	call   0 <write_message>
  f4:	61                   	popa   
  f5:	b9 00 00 00 00       	mov    ecx,0x0
  fa:	ba 02 00 00 00       	mov    edx,0x2
  ff:	e8 fc fe ff ff       	call   0 <write_message>
 104:	b8 01 00 00 00       	mov    eax,0x1
 109:	bb 00 00 00 00       	mov    ebx,0x0
 10e:	cd 80                	int    0x80
