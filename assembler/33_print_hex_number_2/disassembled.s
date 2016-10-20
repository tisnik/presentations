
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         00000212  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         0000001a  00000000  00000000  00000246  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  00000260  2**0
                  ALLOC
  3 .debug_line   00000096  00000000  00000000  00000260  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000075  00000000  00000000  000002f6  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000036b  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000380  2**3
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
  26:	ba 00 00 00 00       	mov    edx,0x0
  2b:	bb 10 00 00 00       	mov    ebx,0x10
  30:	e8 d8 ff ff ff       	call   d <hex2string>
  35:	b9 02 00 00 00       	mov    ecx,0x2
  3a:	ba 18 00 00 00       	mov    edx,0x18
  3f:	e8 bc ff ff ff       	call   0 <write_message>
  44:	ba 01 00 00 00       	mov    edx,0x1
  49:	bb 10 00 00 00       	mov    ebx,0x10
  4e:	e8 ba ff ff ff       	call   d <hex2string>
  53:	b9 02 00 00 00       	mov    ecx,0x2
  58:	ba 18 00 00 00       	mov    edx,0x18
  5d:	e8 9e ff ff ff       	call   0 <write_message>
  62:	ba 02 00 00 00       	mov    edx,0x2
  67:	bb 10 00 00 00       	mov    ebx,0x10
  6c:	e8 9c ff ff ff       	call   d <hex2string>
  71:	b9 02 00 00 00       	mov    ecx,0x2
  76:	ba 18 00 00 00       	mov    edx,0x18
  7b:	e8 80 ff ff ff       	call   0 <write_message>
  80:	b9 00 00 00 00       	mov    ecx,0x0
  85:	ba 02 00 00 00       	mov    edx,0x2
  8a:	e8 71 ff ff ff       	call   0 <write_message>
  8f:	ba 09 00 00 00       	mov    edx,0x9
  94:	bb 10 00 00 00       	mov    ebx,0x10
  99:	e8 6f ff ff ff       	call   d <hex2string>
  9e:	b9 02 00 00 00       	mov    ecx,0x2
  a3:	ba 18 00 00 00       	mov    edx,0x18
  a8:	e8 53 ff ff ff       	call   0 <write_message>
  ad:	ba 0a 00 00 00       	mov    edx,0xa
  b2:	bb 10 00 00 00       	mov    ebx,0x10
  b7:	e8 51 ff ff ff       	call   d <hex2string>
  bc:	b9 02 00 00 00       	mov    ecx,0x2
  c1:	ba 18 00 00 00       	mov    edx,0x18
  c6:	e8 35 ff ff ff       	call   0 <write_message>
  cb:	b9 00 00 00 00       	mov    ecx,0x0
  d0:	ba 02 00 00 00       	mov    edx,0x2
  d5:	e8 26 ff ff ff       	call   0 <write_message>
  da:	ba 0f 00 00 00       	mov    edx,0xf
  df:	bb 10 00 00 00       	mov    ebx,0x10
  e4:	e8 24 ff ff ff       	call   d <hex2string>
  e9:	b9 02 00 00 00       	mov    ecx,0x2
  ee:	ba 18 00 00 00       	mov    edx,0x18
  f3:	e8 08 ff ff ff       	call   0 <write_message>
  f8:	ba 10 00 00 00       	mov    edx,0x10
  fd:	bb 10 00 00 00       	mov    ebx,0x10
 102:	e8 06 ff ff ff       	call   d <hex2string>
 107:	b9 02 00 00 00       	mov    ecx,0x2
 10c:	ba 18 00 00 00       	mov    edx,0x18
 111:	e8 ea fe ff ff       	call   0 <write_message>
 116:	b9 00 00 00 00       	mov    ecx,0x0
 11b:	ba 02 00 00 00       	mov    edx,0x2
 120:	e8 db fe ff ff       	call   0 <write_message>
 125:	ba 7f 00 00 00       	mov    edx,0x7f
 12a:	bb 10 00 00 00       	mov    ebx,0x10
 12f:	e8 d9 fe ff ff       	call   d <hex2string>
 134:	b9 02 00 00 00       	mov    ecx,0x2
 139:	ba 18 00 00 00       	mov    edx,0x18
 13e:	e8 bd fe ff ff       	call   0 <write_message>
 143:	ba 80 00 00 00       	mov    edx,0x80
 148:	bb 10 00 00 00       	mov    ebx,0x10
 14d:	e8 bb fe ff ff       	call   d <hex2string>
 152:	b9 02 00 00 00       	mov    ecx,0x2
 157:	ba 18 00 00 00       	mov    edx,0x18
 15c:	e8 9f fe ff ff       	call   0 <write_message>
 161:	ba ff 00 00 00       	mov    edx,0xff
 166:	bb 10 00 00 00       	mov    ebx,0x10
 16b:	e8 9d fe ff ff       	call   d <hex2string>
 170:	b9 02 00 00 00       	mov    ecx,0x2
 175:	ba 18 00 00 00       	mov    edx,0x18
 17a:	e8 81 fe ff ff       	call   0 <write_message>
 17f:	ba 00 01 00 00       	mov    edx,0x100
 184:	bb 10 00 00 00       	mov    ebx,0x10
 189:	e8 7f fe ff ff       	call   d <hex2string>
 18e:	b9 02 00 00 00       	mov    ecx,0x2
 193:	ba 18 00 00 00       	mov    edx,0x18
 198:	e8 63 fe ff ff       	call   0 <write_message>
 19d:	b9 00 00 00 00       	mov    ecx,0x0
 1a2:	ba 02 00 00 00       	mov    edx,0x2
 1a7:	e8 54 fe ff ff       	call   0 <write_message>
 1ac:	ba ff ff ff ff       	mov    edx,0xffffffff
 1b1:	bb 10 00 00 00       	mov    ebx,0x10
 1b6:	e8 52 fe ff ff       	call   d <hex2string>
 1bb:	b9 02 00 00 00       	mov    ecx,0x2
 1c0:	ba 18 00 00 00       	mov    edx,0x18
 1c5:	e8 36 fe ff ff       	call   0 <write_message>
 1ca:	ba fe ff ff ff       	mov    edx,0xfffffffe
 1cf:	bb 10 00 00 00       	mov    ebx,0x10
 1d4:	e8 34 fe ff ff       	call   d <hex2string>
 1d9:	b9 02 00 00 00       	mov    ecx,0x2
 1de:	ba 18 00 00 00       	mov    edx,0x18
 1e3:	e8 18 fe ff ff       	call   0 <write_message>
 1e8:	ba 00 ff ff ff       	mov    edx,0xffffff00
 1ed:	bb 10 00 00 00       	mov    ebx,0x10
 1f2:	e8 16 fe ff ff       	call   d <hex2string>
 1f7:	b9 02 00 00 00       	mov    ecx,0x2
 1fc:	ba 18 00 00 00       	mov    edx,0x18
 201:	e8 fa fd ff ff       	call   0 <write_message>
 206:	b8 01 00 00 00       	mov    eax,0x1
 20b:	bb 00 00 00 00       	mov    ebx,0x0
 210:	cd 80                	int    0x80
