
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000001f1  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         0000001e  00000000  00000000  00000225  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  00000243  2**0
                  ALLOC
  3 .debug_line   00000093  00000000  00000000  00000243  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000077  00000000  00000000  000002d6  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000034d  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000368  2**3
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
00000002 l       .data	00000000 decimalValueMessage
00000012 l       .data	00000000 decimalValueTemplate
0000001c l       *ABS*	00000000 decimalValueMessageLen
0000000d l       .text	00000000 decimal2string
00000014 l       .text	00000000 next_digit
00000000 l    d  .debug_info	00000000 .debug_info
00000000 l    d  .debug_abbrev	00000000 .debug_abbrev
00000000 l    d  .debug_line	00000000 .debug_line
00000000 l    d  .debug_aranges	00000000 .debug_aranges
00000023 g       .text	00000000 _start



Disassembly of section .text:

00000000 <write_message>:
   0:	b8 04 00 00 00       	mov    eax,0x4
   5:	bb 01 00 00 00       	mov    ebx,0x1
   a:	cd 80                	int    0x80
   c:	c3                   	ret    

0000000d <decimal2string>:
   d:	b9 0a 00 00 00       	mov    ecx,0xa
  12:	89 cf                	mov    edi,ecx

00000014 <next_digit>:
  14:	31 d2                	xor    edx,edx
  16:	f7 f7                	div    edi
  18:	80 c2 30             	add    dl,0x30
  1b:	88 54 0b ff          	mov    BYTE PTR [ebx+ecx*1-0x1],dl
  1f:	49                   	dec    ecx
  20:	75 f2                	jne    14 <next_digit>
  22:	c3                   	ret    

00000023 <_start>:
  23:	b8 00 00 00 00       	mov    eax,0x0
  28:	bb 12 00 00 00       	mov    ebx,0x12
  2d:	e8 db ff ff ff       	call   d <decimal2string>
  32:	b9 02 00 00 00       	mov    ecx,0x2
  37:	ba 1c 00 00 00       	mov    edx,0x1c
  3c:	e8 bf ff ff ff       	call   0 <write_message>
  41:	b8 01 00 00 00       	mov    eax,0x1
  46:	bb 12 00 00 00       	mov    ebx,0x12
  4b:	e8 bd ff ff ff       	call   d <decimal2string>
  50:	b9 02 00 00 00       	mov    ecx,0x2
  55:	ba 1c 00 00 00       	mov    edx,0x1c
  5a:	e8 a1 ff ff ff       	call   0 <write_message>
  5f:	b8 02 00 00 00       	mov    eax,0x2
  64:	bb 12 00 00 00       	mov    ebx,0x12
  69:	e8 9f ff ff ff       	call   d <decimal2string>
  6e:	b9 02 00 00 00       	mov    ecx,0x2
  73:	ba 1c 00 00 00       	mov    edx,0x1c
  78:	e8 83 ff ff ff       	call   0 <write_message>
  7d:	b9 00 00 00 00       	mov    ecx,0x0
  82:	ba 02 00 00 00       	mov    edx,0x2
  87:	e8 74 ff ff ff       	call   0 <write_message>
  8c:	b8 09 00 00 00       	mov    eax,0x9
  91:	bb 12 00 00 00       	mov    ebx,0x12
  96:	e8 72 ff ff ff       	call   d <decimal2string>
  9b:	b9 02 00 00 00       	mov    ecx,0x2
  a0:	ba 1c 00 00 00       	mov    edx,0x1c
  a5:	e8 56 ff ff ff       	call   0 <write_message>
  aa:	b8 0a 00 00 00       	mov    eax,0xa
  af:	bb 12 00 00 00       	mov    ebx,0x12
  b4:	e8 54 ff ff ff       	call   d <decimal2string>
  b9:	b9 02 00 00 00       	mov    ecx,0x2
  be:	ba 1c 00 00 00       	mov    edx,0x1c
  c3:	e8 38 ff ff ff       	call   0 <write_message>
  c8:	b9 00 00 00 00       	mov    ecx,0x0
  cd:	ba 02 00 00 00       	mov    edx,0x2
  d2:	e8 29 ff ff ff       	call   0 <write_message>
  d7:	b8 63 00 00 00       	mov    eax,0x63
  dc:	bb 12 00 00 00       	mov    ebx,0x12
  e1:	e8 27 ff ff ff       	call   d <decimal2string>
  e6:	b9 02 00 00 00       	mov    ecx,0x2
  eb:	ba 1c 00 00 00       	mov    edx,0x1c
  f0:	e8 0b ff ff ff       	call   0 <write_message>
  f5:	b8 64 00 00 00       	mov    eax,0x64
  fa:	bb 12 00 00 00       	mov    ebx,0x12
  ff:	e8 09 ff ff ff       	call   d <decimal2string>
 104:	b9 02 00 00 00       	mov    ecx,0x2
 109:	ba 1c 00 00 00       	mov    edx,0x1c
 10e:	e8 ed fe ff ff       	call   0 <write_message>
 113:	b9 00 00 00 00       	mov    ecx,0x0
 118:	ba 02 00 00 00       	mov    edx,0x2
 11d:	e8 de fe ff ff       	call   0 <write_message>
 122:	b8 e7 03 00 00       	mov    eax,0x3e7
 127:	bb 12 00 00 00       	mov    ebx,0x12
 12c:	e8 dc fe ff ff       	call   d <decimal2string>
 131:	b9 02 00 00 00       	mov    ecx,0x2
 136:	ba 1c 00 00 00       	mov    edx,0x1c
 13b:	e8 c0 fe ff ff       	call   0 <write_message>
 140:	b8 e8 03 00 00       	mov    eax,0x3e8
 145:	bb 12 00 00 00       	mov    ebx,0x12
 14a:	e8 be fe ff ff       	call   d <decimal2string>
 14f:	b9 02 00 00 00       	mov    ecx,0x2
 154:	ba 1c 00 00 00       	mov    edx,0x1c
 159:	e8 a2 fe ff ff       	call   0 <write_message>
 15e:	b9 00 00 00 00       	mov    ecx,0x0
 163:	ba 02 00 00 00       	mov    edx,0x2
 168:	e8 93 fe ff ff       	call   0 <write_message>
 16d:	b8 ff ff ff ff       	mov    eax,0xffffffff
 172:	bb 12 00 00 00       	mov    ebx,0x12
 177:	e8 91 fe ff ff       	call   d <decimal2string>
 17c:	b9 02 00 00 00       	mov    ecx,0x2
 181:	ba 1c 00 00 00       	mov    edx,0x1c
 186:	e8 75 fe ff ff       	call   0 <write_message>
 18b:	b8 fe ff ff ff       	mov    eax,0xfffffffe
 190:	bb 12 00 00 00       	mov    ebx,0x12
 195:	e8 73 fe ff ff       	call   d <decimal2string>
 19a:	b9 02 00 00 00       	mov    ecx,0x2
 19f:	ba 1c 00 00 00       	mov    edx,0x1c
 1a4:	e8 57 fe ff ff       	call   0 <write_message>
 1a9:	b8 f7 ff ff ff       	mov    eax,0xfffffff7
 1ae:	bb 12 00 00 00       	mov    ebx,0x12
 1b3:	e8 55 fe ff ff       	call   d <decimal2string>
 1b8:	b9 02 00 00 00       	mov    ecx,0x2
 1bd:	ba 1c 00 00 00       	mov    edx,0x1c
 1c2:	e8 39 fe ff ff       	call   0 <write_message>
 1c7:	b8 f6 ff ff ff       	mov    eax,0xfffffff6
 1cc:	bb 12 00 00 00       	mov    ebx,0x12
 1d1:	e8 37 fe ff ff       	call   d <decimal2string>
 1d6:	b9 02 00 00 00       	mov    ecx,0x2
 1db:	ba 1c 00 00 00       	mov    edx,0x1c
 1e0:	e8 1b fe ff ff       	call   0 <write_message>
 1e5:	b8 01 00 00 00       	mov    eax,0x1
 1ea:	bb 00 00 00 00       	mov    ebx,0x0
 1ef:	cd 80                	int    0x80
