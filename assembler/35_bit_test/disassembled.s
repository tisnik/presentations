
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000001e8  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000029  00000000  00000000  0000021c  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  00000245  2**0
                  ALLOC
  3 .debug_line   0000008e  00000000  00000000  00000245  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   0000006b  00000000  00000000  000002d3  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000033e  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000358  2**3
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
0000001a l       .data	00000000 bitValueMessage
00000026 l       .data	00000000 bitValueTemplate
0000000f l       *ABS*	00000000 bitValueMessageLen
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
  26:	60                   	pusha  
  27:	ba 01 00 00 00       	mov    edx,0x1
  2c:	bb 10 00 00 00       	mov    ebx,0x10
  31:	e8 d7 ff ff ff       	call   d <hex2string>
  36:	b9 02 00 00 00       	mov    ecx,0x2
  3b:	ba 18 00 00 00       	mov    edx,0x18
  40:	e8 bb ff ff ff       	call   0 <write_message>
  45:	61                   	popa   
  46:	bb 01 00 00 00       	mov    ebx,0x1
  4b:	b0 30                	mov    al,0x30
  4d:	0f ba e3 00          	bt     ebx,0x0
  51:	14 00                	adc    al,0x0
  53:	a2 26 00 00 00       	mov    ds:0x26,al
  58:	b9 1a 00 00 00       	mov    ecx,0x1a
  5d:	ba 0f 00 00 00       	mov    edx,0xf
  62:	e8 99 ff ff ff       	call   0 <write_message>
  67:	bb 01 00 00 00       	mov    ebx,0x1
  6c:	b0 30                	mov    al,0x30
  6e:	0f ba e3 01          	bt     ebx,0x1
  72:	14 00                	adc    al,0x0
  74:	a2 26 00 00 00       	mov    ds:0x26,al
  79:	b9 1a 00 00 00       	mov    ecx,0x1a
  7e:	ba 0f 00 00 00       	mov    edx,0xf
  83:	e8 78 ff ff ff       	call   0 <write_message>
  88:	bb 01 00 00 00       	mov    ebx,0x1
  8d:	b0 30                	mov    al,0x30
  8f:	0f ba e3 1f          	bt     ebx,0x1f
  93:	14 00                	adc    al,0x0
  95:	a2 26 00 00 00       	mov    ds:0x26,al
  9a:	b9 1a 00 00 00       	mov    ecx,0x1a
  9f:	ba 0f 00 00 00       	mov    edx,0xf
  a4:	e8 57 ff ff ff       	call   0 <write_message>
  a9:	b9 00 00 00 00       	mov    ecx,0x0
  ae:	ba 02 00 00 00       	mov    edx,0x2
  b3:	e8 48 ff ff ff       	call   0 <write_message>
  b8:	60                   	pusha  
  b9:	ba 00 00 00 80       	mov    edx,0x80000000
  be:	bb 10 00 00 00       	mov    ebx,0x10
  c3:	e8 45 ff ff ff       	call   d <hex2string>
  c8:	b9 02 00 00 00       	mov    ecx,0x2
  cd:	ba 18 00 00 00       	mov    edx,0x18
  d2:	e8 29 ff ff ff       	call   0 <write_message>
  d7:	61                   	popa   
  d8:	bb 00 00 00 80       	mov    ebx,0x80000000
  dd:	b0 30                	mov    al,0x30
  df:	0f ba e3 00          	bt     ebx,0x0
  e3:	14 00                	adc    al,0x0
  e5:	a2 26 00 00 00       	mov    ds:0x26,al
  ea:	b9 1a 00 00 00       	mov    ecx,0x1a
  ef:	ba 0f 00 00 00       	mov    edx,0xf
  f4:	e8 07 ff ff ff       	call   0 <write_message>
  f9:	bb 00 00 00 80       	mov    ebx,0x80000000
  fe:	b0 30                	mov    al,0x30
 100:	0f ba e3 01          	bt     ebx,0x1
 104:	14 00                	adc    al,0x0
 106:	a2 26 00 00 00       	mov    ds:0x26,al
 10b:	b9 1a 00 00 00       	mov    ecx,0x1a
 110:	ba 0f 00 00 00       	mov    edx,0xf
 115:	e8 e6 fe ff ff       	call   0 <write_message>
 11a:	bb 00 00 00 80       	mov    ebx,0x80000000
 11f:	b0 30                	mov    al,0x30
 121:	0f ba e3 1f          	bt     ebx,0x1f
 125:	14 00                	adc    al,0x0
 127:	a2 26 00 00 00       	mov    ds:0x26,al
 12c:	b9 1a 00 00 00       	mov    ecx,0x1a
 131:	ba 0f 00 00 00       	mov    edx,0xf
 136:	e8 c5 fe ff ff       	call   0 <write_message>
 13b:	b9 00 00 00 00       	mov    ecx,0x0
 140:	ba 02 00 00 00       	mov    edx,0x2
 145:	e8 b6 fe ff ff       	call   0 <write_message>
 14a:	60                   	pusha  
 14b:	ba ff ff ff ff       	mov    edx,0xffffffff
 150:	bb 10 00 00 00       	mov    ebx,0x10
 155:	e8 b3 fe ff ff       	call   d <hex2string>
 15a:	b9 02 00 00 00       	mov    ecx,0x2
 15f:	ba 18 00 00 00       	mov    edx,0x18
 164:	e8 97 fe ff ff       	call   0 <write_message>
 169:	61                   	popa   
 16a:	bb ff ff ff ff       	mov    ebx,0xffffffff
 16f:	b0 30                	mov    al,0x30
 171:	0f ba e3 00          	bt     ebx,0x0
 175:	14 00                	adc    al,0x0
 177:	a2 26 00 00 00       	mov    ds:0x26,al
 17c:	b9 1a 00 00 00       	mov    ecx,0x1a
 181:	ba 0f 00 00 00       	mov    edx,0xf
 186:	e8 75 fe ff ff       	call   0 <write_message>
 18b:	bb ff ff ff ff       	mov    ebx,0xffffffff
 190:	b0 30                	mov    al,0x30
 192:	0f ba e3 01          	bt     ebx,0x1
 196:	14 00                	adc    al,0x0
 198:	a2 26 00 00 00       	mov    ds:0x26,al
 19d:	b9 1a 00 00 00       	mov    ecx,0x1a
 1a2:	ba 0f 00 00 00       	mov    edx,0xf
 1a7:	e8 54 fe ff ff       	call   0 <write_message>
 1ac:	bb ff ff ff ff       	mov    ebx,0xffffffff
 1b1:	b0 30                	mov    al,0x30
 1b3:	0f ba e3 1f          	bt     ebx,0x1f
 1b7:	14 00                	adc    al,0x0
 1b9:	a2 26 00 00 00       	mov    ds:0x26,al
 1be:	b9 1a 00 00 00       	mov    ecx,0x1a
 1c3:	ba 0f 00 00 00       	mov    edx,0xf
 1c8:	e8 33 fe ff ff       	call   0 <write_message>
 1cd:	b9 00 00 00 00       	mov    ecx,0x0
 1d2:	ba 02 00 00 00       	mov    edx,0x2
 1d7:	e8 24 fe ff ff       	call   0 <write_message>
 1dc:	b8 01 00 00 00       	mov    eax,0x1
 1e1:	bb 00 00 00 00       	mov    ebx,0x0
 1e6:	cd 80                	int    0x80
