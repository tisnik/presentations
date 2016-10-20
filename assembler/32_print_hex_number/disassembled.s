
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         00000214  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         0000001a  00000000  00000000  00000248  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  00000262  2**0
                  ALLOC
  3 .debug_line   00000096  00000000  00000000  00000262  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000073  00000000  00000000  000002f8  2**0
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
0000001e l       .text	00000000 alpha_digit
0000001a l       .text	00000000 numeric_digit
00000020 l       .text	00000000 store_digit
00000000 l    d  .debug_info	00000000 .debug_info
00000000 l    d  .debug_abbrev	00000000 .debug_abbrev
00000000 l    d  .debug_line	00000000 .debug_line
00000000 l    d  .debug_aranges	00000000 .debug_aranges
00000028 g       .text	00000000 _start



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
  18:	7d 04                	jge    1e <alpha_digit>

0000001a <numeric_digit>:
  1a:	04 30                	add    al,0x30
  1c:	eb 02                	jmp    20 <store_digit>

0000001e <alpha_digit>:
  1e:	04 37                	add    al,0x37

00000020 <store_digit>:
  20:	88 03                	mov    BYTE PTR [ebx],al
  22:	43                   	inc    ebx
  23:	fe c9                	dec    cl
  25:	75 e8                	jne    f <print_one_digit>
  27:	c3                   	ret    

00000028 <_start>:
  28:	ba 00 00 00 00       	mov    edx,0x0
  2d:	bb 10 00 00 00       	mov    ebx,0x10
  32:	e8 d6 ff ff ff       	call   d <hex2string>
  37:	b9 02 00 00 00       	mov    ecx,0x2
  3c:	ba 18 00 00 00       	mov    edx,0x18
  41:	e8 ba ff ff ff       	call   0 <write_message>
  46:	ba 01 00 00 00       	mov    edx,0x1
  4b:	bb 10 00 00 00       	mov    ebx,0x10
  50:	e8 b8 ff ff ff       	call   d <hex2string>
  55:	b9 02 00 00 00       	mov    ecx,0x2
  5a:	ba 18 00 00 00       	mov    edx,0x18
  5f:	e8 9c ff ff ff       	call   0 <write_message>
  64:	ba 02 00 00 00       	mov    edx,0x2
  69:	bb 10 00 00 00       	mov    ebx,0x10
  6e:	e8 9a ff ff ff       	call   d <hex2string>
  73:	b9 02 00 00 00       	mov    ecx,0x2
  78:	ba 18 00 00 00       	mov    edx,0x18
  7d:	e8 7e ff ff ff       	call   0 <write_message>
  82:	b9 00 00 00 00       	mov    ecx,0x0
  87:	ba 02 00 00 00       	mov    edx,0x2
  8c:	e8 6f ff ff ff       	call   0 <write_message>
  91:	ba 09 00 00 00       	mov    edx,0x9
  96:	bb 10 00 00 00       	mov    ebx,0x10
  9b:	e8 6d ff ff ff       	call   d <hex2string>
  a0:	b9 02 00 00 00       	mov    ecx,0x2
  a5:	ba 18 00 00 00       	mov    edx,0x18
  aa:	e8 51 ff ff ff       	call   0 <write_message>
  af:	ba 0a 00 00 00       	mov    edx,0xa
  b4:	bb 10 00 00 00       	mov    ebx,0x10
  b9:	e8 4f ff ff ff       	call   d <hex2string>
  be:	b9 02 00 00 00       	mov    ecx,0x2
  c3:	ba 18 00 00 00       	mov    edx,0x18
  c8:	e8 33 ff ff ff       	call   0 <write_message>
  cd:	b9 00 00 00 00       	mov    ecx,0x0
  d2:	ba 02 00 00 00       	mov    edx,0x2
  d7:	e8 24 ff ff ff       	call   0 <write_message>
  dc:	ba 0f 00 00 00       	mov    edx,0xf
  e1:	bb 10 00 00 00       	mov    ebx,0x10
  e6:	e8 22 ff ff ff       	call   d <hex2string>
  eb:	b9 02 00 00 00       	mov    ecx,0x2
  f0:	ba 18 00 00 00       	mov    edx,0x18
  f5:	e8 06 ff ff ff       	call   0 <write_message>
  fa:	ba 10 00 00 00       	mov    edx,0x10
  ff:	bb 10 00 00 00       	mov    ebx,0x10
 104:	e8 04 ff ff ff       	call   d <hex2string>
 109:	b9 02 00 00 00       	mov    ecx,0x2
 10e:	ba 18 00 00 00       	mov    edx,0x18
 113:	e8 e8 fe ff ff       	call   0 <write_message>
 118:	b9 00 00 00 00       	mov    ecx,0x0
 11d:	ba 02 00 00 00       	mov    edx,0x2
 122:	e8 d9 fe ff ff       	call   0 <write_message>
 127:	ba 7f 00 00 00       	mov    edx,0x7f
 12c:	bb 10 00 00 00       	mov    ebx,0x10
 131:	e8 d7 fe ff ff       	call   d <hex2string>
 136:	b9 02 00 00 00       	mov    ecx,0x2
 13b:	ba 18 00 00 00       	mov    edx,0x18
 140:	e8 bb fe ff ff       	call   0 <write_message>
 145:	ba 80 00 00 00       	mov    edx,0x80
 14a:	bb 10 00 00 00       	mov    ebx,0x10
 14f:	e8 b9 fe ff ff       	call   d <hex2string>
 154:	b9 02 00 00 00       	mov    ecx,0x2
 159:	ba 18 00 00 00       	mov    edx,0x18
 15e:	e8 9d fe ff ff       	call   0 <write_message>
 163:	ba ff 00 00 00       	mov    edx,0xff
 168:	bb 10 00 00 00       	mov    ebx,0x10
 16d:	e8 9b fe ff ff       	call   d <hex2string>
 172:	b9 02 00 00 00       	mov    ecx,0x2
 177:	ba 18 00 00 00       	mov    edx,0x18
 17c:	e8 7f fe ff ff       	call   0 <write_message>
 181:	ba 00 01 00 00       	mov    edx,0x100
 186:	bb 10 00 00 00       	mov    ebx,0x10
 18b:	e8 7d fe ff ff       	call   d <hex2string>
 190:	b9 02 00 00 00       	mov    ecx,0x2
 195:	ba 18 00 00 00       	mov    edx,0x18
 19a:	e8 61 fe ff ff       	call   0 <write_message>
 19f:	b9 00 00 00 00       	mov    ecx,0x0
 1a4:	ba 02 00 00 00       	mov    edx,0x2
 1a9:	e8 52 fe ff ff       	call   0 <write_message>
 1ae:	ba ff ff ff ff       	mov    edx,0xffffffff
 1b3:	bb 10 00 00 00       	mov    ebx,0x10
 1b8:	e8 50 fe ff ff       	call   d <hex2string>
 1bd:	b9 02 00 00 00       	mov    ecx,0x2
 1c2:	ba 18 00 00 00       	mov    edx,0x18
 1c7:	e8 34 fe ff ff       	call   0 <write_message>
 1cc:	ba fe ff ff ff       	mov    edx,0xfffffffe
 1d1:	bb 10 00 00 00       	mov    ebx,0x10
 1d6:	e8 32 fe ff ff       	call   d <hex2string>
 1db:	b9 02 00 00 00       	mov    ecx,0x2
 1e0:	ba 18 00 00 00       	mov    edx,0x18
 1e5:	e8 16 fe ff ff       	call   0 <write_message>
 1ea:	ba 00 ff ff ff       	mov    edx,0xffffff00
 1ef:	bb 10 00 00 00       	mov    ebx,0x10
 1f4:	e8 14 fe ff ff       	call   d <hex2string>
 1f9:	b9 02 00 00 00       	mov    ecx,0x2
 1fe:	ba 18 00 00 00       	mov    edx,0x18
 203:	e8 f8 fd ff ff       	call   0 <write_message>
 208:	b8 01 00 00 00       	mov    eax,0x1
 20d:	bb 00 00 00 00       	mov    ebx,0x0
 212:	cd 80                	int    0x80
