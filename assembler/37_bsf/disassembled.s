
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         0000027f  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000036  00000000  00000000  000002b3  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  000002e9  2**0
                  ALLOC
  3 .debug_line   000000cb  00000000  00000000  000002e9  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000066  00000000  00000000  000003b4  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000041a  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000430  2**3
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
0000001a l       .data	00000000 decimalValueMessage
0000002a l       .data	00000000 decimalValueTemplate
0000001c l       *ABS*	00000000 decimalValueMessageLen
00000026 l       .text	00000000 decimal2string
0000002d l       .text	00000000 next_digit
00000000 l    d  .debug_info	00000000 .debug_info
00000000 l    d  .debug_abbrev	00000000 .debug_abbrev
00000000 l    d  .debug_line	00000000 .debug_line
00000000 l    d  .debug_aranges	00000000 .debug_aranges
0000003c g       .text	00000000 _start



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

00000026 <decimal2string>:
  26:	b9 0a 00 00 00       	mov    ecx,0xa
  2b:	89 cf                	mov    edi,ecx

0000002d <next_digit>:
  2d:	31 d2                	xor    edx,edx
  2f:	f7 f7                	div    edi
  31:	80 c2 30             	add    dl,0x30
  34:	88 54 0b ff          	mov    BYTE PTR [ebx+ecx*1-0x1],dl
  38:	49                   	dec    ecx
  39:	75 f2                	jne    2d <next_digit>
  3b:	c3                   	ret    

0000003c <_start>:
  3c:	bb 01 00 00 00       	mov    ebx,0x1
  41:	60                   	pusha  
  42:	89 da                	mov    edx,ebx
  44:	bb 10 00 00 00       	mov    ebx,0x10
  49:	e8 bf ff ff ff       	call   d <hex2string>
  4e:	b9 02 00 00 00       	mov    ecx,0x2
  53:	ba 18 00 00 00       	mov    edx,0x18
  58:	e8 a3 ff ff ff       	call   0 <write_message>
  5d:	61                   	popa   
  5e:	0f bc c3             	bsf    eax,ebx
  61:	60                   	pusha  
  62:	89 c0                	mov    eax,eax
  64:	bb 2a 00 00 00       	mov    ebx,0x2a
  69:	e8 b8 ff ff ff       	call   26 <decimal2string>
  6e:	b9 1a 00 00 00       	mov    ecx,0x1a
  73:	ba 1c 00 00 00       	mov    edx,0x1c
  78:	e8 83 ff ff ff       	call   0 <write_message>
  7d:	61                   	popa   
  7e:	b9 00 00 00 00       	mov    ecx,0x0
  83:	ba 02 00 00 00       	mov    edx,0x2
  88:	e8 73 ff ff ff       	call   0 <write_message>
  8d:	bb 02 00 00 00       	mov    ebx,0x2
  92:	60                   	pusha  
  93:	89 da                	mov    edx,ebx
  95:	bb 10 00 00 00       	mov    ebx,0x10
  9a:	e8 6e ff ff ff       	call   d <hex2string>
  9f:	b9 02 00 00 00       	mov    ecx,0x2
  a4:	ba 18 00 00 00       	mov    edx,0x18
  a9:	e8 52 ff ff ff       	call   0 <write_message>
  ae:	61                   	popa   
  af:	0f bc c3             	bsf    eax,ebx
  b2:	60                   	pusha  
  b3:	89 c0                	mov    eax,eax
  b5:	bb 2a 00 00 00       	mov    ebx,0x2a
  ba:	e8 67 ff ff ff       	call   26 <decimal2string>
  bf:	b9 1a 00 00 00       	mov    ecx,0x1a
  c4:	ba 1c 00 00 00       	mov    edx,0x1c
  c9:	e8 32 ff ff ff       	call   0 <write_message>
  ce:	61                   	popa   
  cf:	b9 00 00 00 00       	mov    ecx,0x0
  d4:	ba 02 00 00 00       	mov    edx,0x2
  d9:	e8 22 ff ff ff       	call   0 <write_message>
  de:	bb 00 f0 00 00       	mov    ebx,0xf000
  e3:	60                   	pusha  
  e4:	89 da                	mov    edx,ebx
  e6:	bb 10 00 00 00       	mov    ebx,0x10
  eb:	e8 1d ff ff ff       	call   d <hex2string>
  f0:	b9 02 00 00 00       	mov    ecx,0x2
  f5:	ba 18 00 00 00       	mov    edx,0x18
  fa:	e8 01 ff ff ff       	call   0 <write_message>
  ff:	61                   	popa   
 100:	0f bc c3             	bsf    eax,ebx
 103:	60                   	pusha  
 104:	89 c0                	mov    eax,eax
 106:	bb 2a 00 00 00       	mov    ebx,0x2a
 10b:	e8 16 ff ff ff       	call   26 <decimal2string>
 110:	b9 1a 00 00 00       	mov    ecx,0x1a
 115:	ba 1c 00 00 00       	mov    edx,0x1c
 11a:	e8 e1 fe ff ff       	call   0 <write_message>
 11f:	61                   	popa   
 120:	b9 00 00 00 00       	mov    ecx,0x0
 125:	ba 02 00 00 00       	mov    edx,0x2
 12a:	e8 d1 fe ff ff       	call   0 <write_message>
 12f:	bb 00 00 01 00       	mov    ebx,0x10000
 134:	60                   	pusha  
 135:	89 da                	mov    edx,ebx
 137:	bb 10 00 00 00       	mov    ebx,0x10
 13c:	e8 cc fe ff ff       	call   d <hex2string>
 141:	b9 02 00 00 00       	mov    ecx,0x2
 146:	ba 18 00 00 00       	mov    edx,0x18
 14b:	e8 b0 fe ff ff       	call   0 <write_message>
 150:	61                   	popa   
 151:	0f bc c3             	bsf    eax,ebx
 154:	60                   	pusha  
 155:	89 c0                	mov    eax,eax
 157:	bb 2a 00 00 00       	mov    ebx,0x2a
 15c:	e8 c5 fe ff ff       	call   26 <decimal2string>
 161:	b9 1a 00 00 00       	mov    ecx,0x1a
 166:	ba 1c 00 00 00       	mov    edx,0x1c
 16b:	e8 90 fe ff ff       	call   0 <write_message>
 170:	61                   	popa   
 171:	b9 00 00 00 00       	mov    ecx,0x0
 176:	ba 02 00 00 00       	mov    edx,0x2
 17b:	e8 80 fe ff ff       	call   0 <write_message>
 180:	bb 00 00 00 80       	mov    ebx,0x80000000
 185:	60                   	pusha  
 186:	89 da                	mov    edx,ebx
 188:	bb 10 00 00 00       	mov    ebx,0x10
 18d:	e8 7b fe ff ff       	call   d <hex2string>
 192:	b9 02 00 00 00       	mov    ecx,0x2
 197:	ba 18 00 00 00       	mov    edx,0x18
 19c:	e8 5f fe ff ff       	call   0 <write_message>
 1a1:	61                   	popa   
 1a2:	0f bc c3             	bsf    eax,ebx
 1a5:	60                   	pusha  
 1a6:	89 c0                	mov    eax,eax
 1a8:	bb 2a 00 00 00       	mov    ebx,0x2a
 1ad:	e8 74 fe ff ff       	call   26 <decimal2string>
 1b2:	b9 1a 00 00 00       	mov    ecx,0x1a
 1b7:	ba 1c 00 00 00       	mov    edx,0x1c
 1bc:	e8 3f fe ff ff       	call   0 <write_message>
 1c1:	61                   	popa   
 1c2:	b9 00 00 00 00       	mov    ecx,0x0
 1c7:	ba 02 00 00 00       	mov    edx,0x2
 1cc:	e8 2f fe ff ff       	call   0 <write_message>
 1d1:	bb 01 00 00 80       	mov    ebx,0x80000001
 1d6:	60                   	pusha  
 1d7:	89 da                	mov    edx,ebx
 1d9:	bb 10 00 00 00       	mov    ebx,0x10
 1de:	e8 2a fe ff ff       	call   d <hex2string>
 1e3:	b9 02 00 00 00       	mov    ecx,0x2
 1e8:	ba 18 00 00 00       	mov    edx,0x18
 1ed:	e8 0e fe ff ff       	call   0 <write_message>
 1f2:	61                   	popa   
 1f3:	0f bc c3             	bsf    eax,ebx
 1f6:	60                   	pusha  
 1f7:	89 c0                	mov    eax,eax
 1f9:	bb 2a 00 00 00       	mov    ebx,0x2a
 1fe:	e8 23 fe ff ff       	call   26 <decimal2string>
 203:	b9 1a 00 00 00       	mov    ecx,0x1a
 208:	ba 1c 00 00 00       	mov    edx,0x1c
 20d:	e8 ee fd ff ff       	call   0 <write_message>
 212:	61                   	popa   
 213:	b9 00 00 00 00       	mov    ecx,0x0
 218:	ba 02 00 00 00       	mov    edx,0x2
 21d:	e8 de fd ff ff       	call   0 <write_message>
 222:	bb 00 00 00 00       	mov    ebx,0x0
 227:	60                   	pusha  
 228:	89 da                	mov    edx,ebx
 22a:	bb 10 00 00 00       	mov    ebx,0x10
 22f:	e8 d9 fd ff ff       	call   d <hex2string>
 234:	b9 02 00 00 00       	mov    ecx,0x2
 239:	ba 18 00 00 00       	mov    edx,0x18
 23e:	e8 bd fd ff ff       	call   0 <write_message>
 243:	61                   	popa   
 244:	0f bc c3             	bsf    eax,ebx
 247:	60                   	pusha  
 248:	89 c0                	mov    eax,eax
 24a:	bb 2a 00 00 00       	mov    ebx,0x2a
 24f:	e8 d2 fd ff ff       	call   26 <decimal2string>
 254:	b9 1a 00 00 00       	mov    ecx,0x1a
 259:	ba 1c 00 00 00       	mov    edx,0x1c
 25e:	e8 9d fd ff ff       	call   0 <write_message>
 263:	61                   	popa   
 264:	b9 00 00 00 00       	mov    ecx,0x0
 269:	ba 02 00 00 00       	mov    edx,0x2
 26e:	e8 8d fd ff ff       	call   0 <write_message>
 273:	b8 01 00 00 00       	mov    eax,0x1
 278:	bb 00 00 00 00       	mov    ebx,0x0
 27d:	cd 80                	int    0x80
