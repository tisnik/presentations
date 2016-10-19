
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000000ec  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         0000002c  00000000  00000000  00000120  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000004  00000000  00000000  0000014c  2**2
                  ALLOC
  3 .debug_line   00000088  00000000  00000000  0000014c  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000070  00000000  00000000  000001d4  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  00000244  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000258  2**3
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
0000001a l       .data	00000000 fpuValueZeroMessage
00000006 l       *ABS*	00000000 fpuValueZeroMessageLength
00000020 l       .data	00000000 fpuValueOneMessage
00000006 l       *ABS*	00000000 fpuValueOneMessageLength
00000026 l       .data	00000000 fpuValuePiMessage
00000006 l       *ABS*	00000000 fpuValuePiMessageLength
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
  2b:	ba 06 00 00 00       	mov    edx,0x6
  30:	e8 cb ff ff ff       	call   0 <write_message>
  35:	d9 ee                	fldz   
  37:	d9 1d 00 00 00 00    	fstp   DWORD PTR ds:0x0
  3d:	a1 00 00 00 00       	mov    eax,ds:0x0
  42:	60                   	pusha  
  43:	89 c2                	mov    edx,eax
  45:	bb 10 00 00 00       	mov    ebx,0x10
  4a:	e8 be ff ff ff       	call   d <hex2string>
  4f:	b9 02 00 00 00       	mov    ecx,0x2
  54:	ba 18 00 00 00       	mov    edx,0x18
  59:	e8 a2 ff ff ff       	call   0 <write_message>
  5e:	61                   	popa   
  5f:	b9 20 00 00 00       	mov    ecx,0x20
  64:	ba 06 00 00 00       	mov    edx,0x6
  69:	e8 92 ff ff ff       	call   0 <write_message>
  6e:	d9 e8                	fld1   
  70:	d9 1d 00 00 00 00    	fstp   DWORD PTR ds:0x0
  76:	a1 00 00 00 00       	mov    eax,ds:0x0
  7b:	60                   	pusha  
  7c:	89 c2                	mov    edx,eax
  7e:	bb 10 00 00 00       	mov    ebx,0x10
  83:	e8 85 ff ff ff       	call   d <hex2string>
  88:	b9 02 00 00 00       	mov    ecx,0x2
  8d:	ba 18 00 00 00       	mov    edx,0x18
  92:	e8 69 ff ff ff       	call   0 <write_message>
  97:	61                   	popa   
  98:	b9 26 00 00 00       	mov    ecx,0x26
  9d:	ba 06 00 00 00       	mov    edx,0x6
  a2:	e8 59 ff ff ff       	call   0 <write_message>
  a7:	d9 eb                	fldpi  
  a9:	d9 1d 00 00 00 00    	fstp   DWORD PTR ds:0x0
  af:	a1 00 00 00 00       	mov    eax,ds:0x0
  b4:	60                   	pusha  
  b5:	89 c2                	mov    edx,eax
  b7:	bb 10 00 00 00       	mov    ebx,0x10
  bc:	e8 4c ff ff ff       	call   d <hex2string>
  c1:	b9 02 00 00 00       	mov    ecx,0x2
  c6:	ba 18 00 00 00       	mov    edx,0x18
  cb:	e8 30 ff ff ff       	call   0 <write_message>
  d0:	61                   	popa   
  d1:	b9 00 00 00 00       	mov    ecx,0x0
  d6:	ba 02 00 00 00       	mov    edx,0x2
  db:	e8 20 ff ff ff       	call   0 <write_message>
  e0:	b8 01 00 00 00       	mov    eax,0x1
  e5:	bb 00 00 00 00       	mov    ebx,0x0
  ea:	cd 80                	int    0x80
