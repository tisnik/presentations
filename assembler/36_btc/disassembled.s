
main.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000003fe  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000029  00000000  00000000  00000432  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  0000045b  2**0
                  ALLOC
  3 .debug_line   0000008e  00000000  00000000  0000045b  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   00000066  00000000  00000000  000004e9  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  0000054f  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  00000568  2**3
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
  26:	bb 01 00 00 00       	mov    ebx,0x1
  2b:	60                   	pusha  
  2c:	89 da                	mov    edx,ebx
  2e:	bb 10 00 00 00       	mov    ebx,0x10
  33:	e8 d5 ff ff ff       	call   d <hex2string>
  38:	b9 02 00 00 00       	mov    ecx,0x2
  3d:	ba 18 00 00 00       	mov    edx,0x18
  42:	e8 b9 ff ff ff       	call   0 <write_message>
  47:	61                   	popa   
  48:	b0 30                	mov    al,0x30
  4a:	0f ba fb 00          	btc    ebx,0x0
  4e:	53                   	push   ebx
  4f:	14 00                	adc    al,0x0
  51:	a2 26 00 00 00       	mov    ds:0x26,al
  56:	b9 1a 00 00 00       	mov    ecx,0x1a
  5b:	ba 0f 00 00 00       	mov    edx,0xf
  60:	e8 9b ff ff ff       	call   0 <write_message>
  65:	5b                   	pop    ebx
  66:	60                   	pusha  
  67:	89 da                	mov    edx,ebx
  69:	bb 10 00 00 00       	mov    ebx,0x10
  6e:	e8 9a ff ff ff       	call   d <hex2string>
  73:	b9 02 00 00 00       	mov    ecx,0x2
  78:	ba 18 00 00 00       	mov    edx,0x18
  7d:	e8 7e ff ff ff       	call   0 <write_message>
  82:	61                   	popa   
  83:	b9 00 00 00 00       	mov    ecx,0x0
  88:	ba 02 00 00 00       	mov    edx,0x2
  8d:	e8 6e ff ff ff       	call   0 <write_message>
  92:	bb 01 00 00 00       	mov    ebx,0x1
  97:	60                   	pusha  
  98:	89 da                	mov    edx,ebx
  9a:	bb 10 00 00 00       	mov    ebx,0x10
  9f:	e8 69 ff ff ff       	call   d <hex2string>
  a4:	b9 02 00 00 00       	mov    ecx,0x2
  a9:	ba 18 00 00 00       	mov    edx,0x18
  ae:	e8 4d ff ff ff       	call   0 <write_message>
  b3:	61                   	popa   
  b4:	b0 30                	mov    al,0x30
  b6:	0f ba fb 01          	btc    ebx,0x1
  ba:	53                   	push   ebx
  bb:	14 00                	adc    al,0x0
  bd:	a2 26 00 00 00       	mov    ds:0x26,al
  c2:	b9 1a 00 00 00       	mov    ecx,0x1a
  c7:	ba 0f 00 00 00       	mov    edx,0xf
  cc:	e8 2f ff ff ff       	call   0 <write_message>
  d1:	5b                   	pop    ebx
  d2:	60                   	pusha  
  d3:	89 da                	mov    edx,ebx
  d5:	bb 10 00 00 00       	mov    ebx,0x10
  da:	e8 2e ff ff ff       	call   d <hex2string>
  df:	b9 02 00 00 00       	mov    ecx,0x2
  e4:	ba 18 00 00 00       	mov    edx,0x18
  e9:	e8 12 ff ff ff       	call   0 <write_message>
  ee:	61                   	popa   
  ef:	b9 00 00 00 00       	mov    ecx,0x0
  f4:	ba 02 00 00 00       	mov    edx,0x2
  f9:	e8 02 ff ff ff       	call   0 <write_message>
  fe:	bb 01 00 00 00       	mov    ebx,0x1
 103:	60                   	pusha  
 104:	89 da                	mov    edx,ebx
 106:	bb 10 00 00 00       	mov    ebx,0x10
 10b:	e8 fd fe ff ff       	call   d <hex2string>
 110:	b9 02 00 00 00       	mov    ecx,0x2
 115:	ba 18 00 00 00       	mov    edx,0x18
 11a:	e8 e1 fe ff ff       	call   0 <write_message>
 11f:	61                   	popa   
 120:	b0 30                	mov    al,0x30
 122:	0f ba fb 1f          	btc    ebx,0x1f
 126:	53                   	push   ebx
 127:	14 00                	adc    al,0x0
 129:	a2 26 00 00 00       	mov    ds:0x26,al
 12e:	b9 1a 00 00 00       	mov    ecx,0x1a
 133:	ba 0f 00 00 00       	mov    edx,0xf
 138:	e8 c3 fe ff ff       	call   0 <write_message>
 13d:	5b                   	pop    ebx
 13e:	60                   	pusha  
 13f:	89 da                	mov    edx,ebx
 141:	bb 10 00 00 00       	mov    ebx,0x10
 146:	e8 c2 fe ff ff       	call   d <hex2string>
 14b:	b9 02 00 00 00       	mov    ecx,0x2
 150:	ba 18 00 00 00       	mov    edx,0x18
 155:	e8 a6 fe ff ff       	call   0 <write_message>
 15a:	61                   	popa   
 15b:	b9 00 00 00 00       	mov    ecx,0x0
 160:	ba 02 00 00 00       	mov    edx,0x2
 165:	e8 96 fe ff ff       	call   0 <write_message>
 16a:	bb 00 00 00 80       	mov    ebx,0x80000000
 16f:	60                   	pusha  
 170:	89 da                	mov    edx,ebx
 172:	bb 10 00 00 00       	mov    ebx,0x10
 177:	e8 91 fe ff ff       	call   d <hex2string>
 17c:	b9 02 00 00 00       	mov    ecx,0x2
 181:	ba 18 00 00 00       	mov    edx,0x18
 186:	e8 75 fe ff ff       	call   0 <write_message>
 18b:	61                   	popa   
 18c:	b0 30                	mov    al,0x30
 18e:	0f ba fb 00          	btc    ebx,0x0
 192:	53                   	push   ebx
 193:	14 00                	adc    al,0x0
 195:	a2 26 00 00 00       	mov    ds:0x26,al
 19a:	b9 1a 00 00 00       	mov    ecx,0x1a
 19f:	ba 0f 00 00 00       	mov    edx,0xf
 1a4:	e8 57 fe ff ff       	call   0 <write_message>
 1a9:	5b                   	pop    ebx
 1aa:	60                   	pusha  
 1ab:	89 da                	mov    edx,ebx
 1ad:	bb 10 00 00 00       	mov    ebx,0x10
 1b2:	e8 56 fe ff ff       	call   d <hex2string>
 1b7:	b9 02 00 00 00       	mov    ecx,0x2
 1bc:	ba 18 00 00 00       	mov    edx,0x18
 1c1:	e8 3a fe ff ff       	call   0 <write_message>
 1c6:	61                   	popa   
 1c7:	b9 00 00 00 00       	mov    ecx,0x0
 1cc:	ba 02 00 00 00       	mov    edx,0x2
 1d1:	e8 2a fe ff ff       	call   0 <write_message>
 1d6:	bb 00 00 00 80       	mov    ebx,0x80000000
 1db:	60                   	pusha  
 1dc:	89 da                	mov    edx,ebx
 1de:	bb 10 00 00 00       	mov    ebx,0x10
 1e3:	e8 25 fe ff ff       	call   d <hex2string>
 1e8:	b9 02 00 00 00       	mov    ecx,0x2
 1ed:	ba 18 00 00 00       	mov    edx,0x18
 1f2:	e8 09 fe ff ff       	call   0 <write_message>
 1f7:	61                   	popa   
 1f8:	b0 30                	mov    al,0x30
 1fa:	0f ba fb 01          	btc    ebx,0x1
 1fe:	53                   	push   ebx
 1ff:	14 00                	adc    al,0x0
 201:	a2 26 00 00 00       	mov    ds:0x26,al
 206:	b9 1a 00 00 00       	mov    ecx,0x1a
 20b:	ba 0f 00 00 00       	mov    edx,0xf
 210:	e8 eb fd ff ff       	call   0 <write_message>
 215:	5b                   	pop    ebx
 216:	60                   	pusha  
 217:	89 da                	mov    edx,ebx
 219:	bb 10 00 00 00       	mov    ebx,0x10
 21e:	e8 ea fd ff ff       	call   d <hex2string>
 223:	b9 02 00 00 00       	mov    ecx,0x2
 228:	ba 18 00 00 00       	mov    edx,0x18
 22d:	e8 ce fd ff ff       	call   0 <write_message>
 232:	61                   	popa   
 233:	b9 00 00 00 00       	mov    ecx,0x0
 238:	ba 02 00 00 00       	mov    edx,0x2
 23d:	e8 be fd ff ff       	call   0 <write_message>
 242:	bb 00 00 00 80       	mov    ebx,0x80000000
 247:	60                   	pusha  
 248:	89 da                	mov    edx,ebx
 24a:	bb 10 00 00 00       	mov    ebx,0x10
 24f:	e8 b9 fd ff ff       	call   d <hex2string>
 254:	b9 02 00 00 00       	mov    ecx,0x2
 259:	ba 18 00 00 00       	mov    edx,0x18
 25e:	e8 9d fd ff ff       	call   0 <write_message>
 263:	61                   	popa   
 264:	b0 30                	mov    al,0x30
 266:	0f ba fb 1f          	btc    ebx,0x1f
 26a:	53                   	push   ebx
 26b:	14 00                	adc    al,0x0
 26d:	a2 26 00 00 00       	mov    ds:0x26,al
 272:	b9 1a 00 00 00       	mov    ecx,0x1a
 277:	ba 0f 00 00 00       	mov    edx,0xf
 27c:	e8 7f fd ff ff       	call   0 <write_message>
 281:	5b                   	pop    ebx
 282:	60                   	pusha  
 283:	89 da                	mov    edx,ebx
 285:	bb 10 00 00 00       	mov    ebx,0x10
 28a:	e8 7e fd ff ff       	call   d <hex2string>
 28f:	b9 02 00 00 00       	mov    ecx,0x2
 294:	ba 18 00 00 00       	mov    edx,0x18
 299:	e8 62 fd ff ff       	call   0 <write_message>
 29e:	61                   	popa   
 29f:	b9 00 00 00 00       	mov    ecx,0x0
 2a4:	ba 02 00 00 00       	mov    edx,0x2
 2a9:	e8 52 fd ff ff       	call   0 <write_message>
 2ae:	bb ff ff ff ff       	mov    ebx,0xffffffff
 2b3:	60                   	pusha  
 2b4:	89 da                	mov    edx,ebx
 2b6:	bb 10 00 00 00       	mov    ebx,0x10
 2bb:	e8 4d fd ff ff       	call   d <hex2string>
 2c0:	b9 02 00 00 00       	mov    ecx,0x2
 2c5:	ba 18 00 00 00       	mov    edx,0x18
 2ca:	e8 31 fd ff ff       	call   0 <write_message>
 2cf:	61                   	popa   
 2d0:	b0 30                	mov    al,0x30
 2d2:	0f ba fb 00          	btc    ebx,0x0
 2d6:	53                   	push   ebx
 2d7:	14 00                	adc    al,0x0
 2d9:	a2 26 00 00 00       	mov    ds:0x26,al
 2de:	b9 1a 00 00 00       	mov    ecx,0x1a
 2e3:	ba 0f 00 00 00       	mov    edx,0xf
 2e8:	e8 13 fd ff ff       	call   0 <write_message>
 2ed:	5b                   	pop    ebx
 2ee:	60                   	pusha  
 2ef:	89 da                	mov    edx,ebx
 2f1:	bb 10 00 00 00       	mov    ebx,0x10
 2f6:	e8 12 fd ff ff       	call   d <hex2string>
 2fb:	b9 02 00 00 00       	mov    ecx,0x2
 300:	ba 18 00 00 00       	mov    edx,0x18
 305:	e8 f6 fc ff ff       	call   0 <write_message>
 30a:	61                   	popa   
 30b:	b9 00 00 00 00       	mov    ecx,0x0
 310:	ba 02 00 00 00       	mov    edx,0x2
 315:	e8 e6 fc ff ff       	call   0 <write_message>
 31a:	bb ff ff ff ff       	mov    ebx,0xffffffff
 31f:	60                   	pusha  
 320:	89 da                	mov    edx,ebx
 322:	bb 10 00 00 00       	mov    ebx,0x10
 327:	e8 e1 fc ff ff       	call   d <hex2string>
 32c:	b9 02 00 00 00       	mov    ecx,0x2
 331:	ba 18 00 00 00       	mov    edx,0x18
 336:	e8 c5 fc ff ff       	call   0 <write_message>
 33b:	61                   	popa   
 33c:	b0 30                	mov    al,0x30
 33e:	0f ba fb 01          	btc    ebx,0x1
 342:	53                   	push   ebx
 343:	14 00                	adc    al,0x0
 345:	a2 26 00 00 00       	mov    ds:0x26,al
 34a:	b9 1a 00 00 00       	mov    ecx,0x1a
 34f:	ba 0f 00 00 00       	mov    edx,0xf
 354:	e8 a7 fc ff ff       	call   0 <write_message>
 359:	5b                   	pop    ebx
 35a:	60                   	pusha  
 35b:	89 da                	mov    edx,ebx
 35d:	bb 10 00 00 00       	mov    ebx,0x10
 362:	e8 a6 fc ff ff       	call   d <hex2string>
 367:	b9 02 00 00 00       	mov    ecx,0x2
 36c:	ba 18 00 00 00       	mov    edx,0x18
 371:	e8 8a fc ff ff       	call   0 <write_message>
 376:	61                   	popa   
 377:	b9 00 00 00 00       	mov    ecx,0x0
 37c:	ba 02 00 00 00       	mov    edx,0x2
 381:	e8 7a fc ff ff       	call   0 <write_message>
 386:	bb ff ff ff ff       	mov    ebx,0xffffffff
 38b:	60                   	pusha  
 38c:	89 da                	mov    edx,ebx
 38e:	bb 10 00 00 00       	mov    ebx,0x10
 393:	e8 75 fc ff ff       	call   d <hex2string>
 398:	b9 02 00 00 00       	mov    ecx,0x2
 39d:	ba 18 00 00 00       	mov    edx,0x18
 3a2:	e8 59 fc ff ff       	call   0 <write_message>
 3a7:	61                   	popa   
 3a8:	b0 30                	mov    al,0x30
 3aa:	0f ba fb 1f          	btc    ebx,0x1f
 3ae:	53                   	push   ebx
 3af:	14 00                	adc    al,0x0
 3b1:	a2 26 00 00 00       	mov    ds:0x26,al
 3b6:	b9 1a 00 00 00       	mov    ecx,0x1a
 3bb:	ba 0f 00 00 00       	mov    edx,0xf
 3c0:	e8 3b fc ff ff       	call   0 <write_message>
 3c5:	5b                   	pop    ebx
 3c6:	60                   	pusha  
 3c7:	89 da                	mov    edx,ebx
 3c9:	bb 10 00 00 00       	mov    ebx,0x10
 3ce:	e8 3a fc ff ff       	call   d <hex2string>
 3d3:	b9 02 00 00 00       	mov    ecx,0x2
 3d8:	ba 18 00 00 00       	mov    edx,0x18
 3dd:	e8 1e fc ff ff       	call   0 <write_message>
 3e2:	61                   	popa   
 3e3:	b9 00 00 00 00       	mov    ecx,0x0
 3e8:	ba 02 00 00 00       	mov    edx,0x2
 3ed:	e8 0e fc ff ff       	call   0 <write_message>
 3f2:	b8 01 00 00 00       	mov    eax,0x1
 3f7:	bb 00 00 00 00       	mov    ebx,0x0
 3fc:	cd 80                	int    0x80
