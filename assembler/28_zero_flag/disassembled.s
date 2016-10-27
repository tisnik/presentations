
zero_flag.o:     file format elf32-i386
architecture: i386, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x00000000

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000003ec  00000000  00000000  00000034  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000088  00000000  00000000  00000420  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  000004a8  2**0
                  ALLOC
  3 .debug_line   00000095  00000000  00000000  000004a8  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  4 .debug_info   0000006c  00000000  00000000  0000053d  2**0
                  CONTENTS, RELOC, READONLY, DEBUGGING
  5 .debug_abbrev 00000014  00000000  00000000  000005a9  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_aranges 00000020  00000000  00000000  000005c0  2**3
                  CONTENTS, RELOC, READONLY, DEBUGGING
SYMBOL TABLE:
00000000 l    d  .text	00000000 .text
00000000 l    d  .data	00000000 .data
00000000 l    d  .bss	00000000 .bss
00000001 l       *ABS*	00000000 sys_exit
00000004 l       *ABS*	00000000 sys_write
00000001 l       *ABS*	00000000 std_output
00000000 l       .text	00000000 write_message
00000000 l       .data	00000000 messageZeroSet
0000000f l       *ABS*	00000000 messageZeroSetLen
0000000f l       .data	00000000 messageZeroNotSet
00000013 l       *ABS*	00000000 messageZeroNotSetLen
00000022 l       .data	00000000 messageCmp
00000013 l       *ABS*	00000000 messageCmpLen
00000035 l       .data	00000000 messageAdd
00000013 l       *ABS*	00000000 messageAddLen
00000048 l       .data	00000000 messagePositiveValues
00000012 l       *ABS*	00000000 messagePositiveValuesLen
0000005a l       .data	00000000 messageNegativeValues
00000012 l       *ABS*	00000000 messageNegativeValuesLen
0000006c l       .data	00000000 message0x7fffffffand0x80000000
0000001c l       *ABS*	00000000 message0x7fffffffand0x80000000Len
0000004a l       .text	00000000 zero_set2
00000059 l       .text	00000000 end_compare2
00000078 l       .text	00000000 zero_set5
00000087 l       .text	00000000 end_compare5
000000a6 l       .text	00000000 zero_set8
000000b5 l       .text	00000000 end_compare8
000000d4 l       .text	00000000 zero_set11
000000e3 l       .text	00000000 end_compare11
00000111 l       .text	00000000 zero_set15
00000120 l       .text	00000000 end_compare15
0000013f l       .text	00000000 zero_set18
0000014e l       .text	00000000 end_compare18
0000016d l       .text	00000000 zero_set21
0000017c l       .text	00000000 end_compare21
000001b9 l       .text	00000000 zero_set26
000001c8 l       .text	00000000 end_add26
000001e7 l       .text	00000000 zero_set29
000001f6 l       .text	00000000 end_add29
00000215 l       .text	00000000 zero_set32
00000224 l       .text	00000000 end_add32
00000243 l       .text	00000000 zero_set35
00000252 l       .text	00000000 end_add35
00000280 l       .text	00000000 zero_set39
0000028f l       .text	00000000 end_add39
000002ae l       .text	00000000 zero_set42
000002bd l       .text	00000000 end_add42
000002dc l       .text	00000000 zero_set45
000002eb l       .text	00000000 end_add45
0000030a l       .text	00000000 zero_set48
00000319 l       .text	00000000 end_add48
00000347 l       .text	00000000 zero_set52
00000356 l       .text	00000000 end_add52
00000375 l       .text	00000000 zero_set55
00000384 l       .text	00000000 end_add55
000003a3 l       .text	00000000 zero_set58
000003b2 l       .text	00000000 end_add58
000003d1 l       .text	00000000 zero_set61
000003e0 l       .text	00000000 end_add61
00000000 l    d  .debug_info	00000000 .debug_info
00000000 l    d  .debug_abbrev	00000000 .debug_abbrev
00000000 l    d  .debug_line	00000000 .debug_line
00000000 l    d  .debug_aranges	00000000 .debug_aranges
0000000d g       .text	00000000 _start



Disassembly of section .text:

00000000 <write_message>:
   0:	b8 04 00 00 00       	mov    eax,0x4
   5:	bb 01 00 00 00       	mov    ebx,0x1
   a:	cd 80                	int    0x80
   c:	c3                   	ret    

0000000d <_start>:
   d:	b9 22 00 00 00       	mov    ecx,0x22
  12:	ba 13 00 00 00       	mov    edx,0x13
  17:	e8 e4 ff ff ff       	call   0 <write_message>
  1c:	b9 48 00 00 00       	mov    ecx,0x48
  21:	ba 12 00 00 00       	mov    edx,0x12
  26:	e8 d5 ff ff ff       	call   0 <write_message>
  2b:	b8 00 00 00 00       	mov    eax,0x0
  30:	bb 00 00 00 00       	mov    ebx,0x0
  35:	39 d8                	cmp    eax,ebx
  37:	74 11                	je     4a <zero_set2>
  39:	b9 0f 00 00 00       	mov    ecx,0xf
  3e:	ba 13 00 00 00       	mov    edx,0x13
  43:	e8 b8 ff ff ff       	call   0 <write_message>
  48:	eb 0f                	jmp    59 <end_compare2>

0000004a <zero_set2>:
  4a:	b9 00 00 00 00       	mov    ecx,0x0
  4f:	ba 0f 00 00 00       	mov    edx,0xf
  54:	e8 a7 ff ff ff       	call   0 <write_message>

00000059 <end_compare2>:
  59:	b8 64 00 00 00       	mov    eax,0x64
  5e:	bb 00 00 00 00       	mov    ebx,0x0
  63:	39 d8                	cmp    eax,ebx
  65:	74 11                	je     78 <zero_set5>
  67:	b9 0f 00 00 00       	mov    ecx,0xf
  6c:	ba 13 00 00 00       	mov    edx,0x13
  71:	e8 8a ff ff ff       	call   0 <write_message>
  76:	eb 0f                	jmp    87 <end_compare5>

00000078 <zero_set5>:
  78:	b9 00 00 00 00       	mov    ecx,0x0
  7d:	ba 0f 00 00 00       	mov    edx,0xf
  82:	e8 79 ff ff ff       	call   0 <write_message>

00000087 <end_compare5>:
  87:	b8 00 00 00 00       	mov    eax,0x0
  8c:	bb 64 00 00 00       	mov    ebx,0x64
  91:	39 d8                	cmp    eax,ebx
  93:	74 11                	je     a6 <zero_set8>
  95:	b9 0f 00 00 00       	mov    ecx,0xf
  9a:	ba 13 00 00 00       	mov    edx,0x13
  9f:	e8 5c ff ff ff       	call   0 <write_message>
  a4:	eb 0f                	jmp    b5 <end_compare8>

000000a6 <zero_set8>:
  a6:	b9 00 00 00 00       	mov    ecx,0x0
  ab:	ba 0f 00 00 00       	mov    edx,0xf
  b0:	e8 4b ff ff ff       	call   0 <write_message>

000000b5 <end_compare8>:
  b5:	b8 64 00 00 00       	mov    eax,0x64
  ba:	bb 64 00 00 00       	mov    ebx,0x64
  bf:	39 d8                	cmp    eax,ebx
  c1:	74 11                	je     d4 <zero_set11>
  c3:	b9 0f 00 00 00       	mov    ecx,0xf
  c8:	ba 13 00 00 00       	mov    edx,0x13
  cd:	e8 2e ff ff ff       	call   0 <write_message>
  d2:	eb 0f                	jmp    e3 <end_compare11>

000000d4 <zero_set11>:
  d4:	b9 00 00 00 00       	mov    ecx,0x0
  d9:	ba 0f 00 00 00       	mov    edx,0xf
  de:	e8 1d ff ff ff       	call   0 <write_message>

000000e3 <end_compare11>:
  e3:	b9 5a 00 00 00       	mov    ecx,0x5a
  e8:	ba 12 00 00 00       	mov    edx,0x12
  ed:	e8 0e ff ff ff       	call   0 <write_message>
  f2:	b8 9c ff ff ff       	mov    eax,0xffffff9c
  f7:	bb 00 00 00 00       	mov    ebx,0x0
  fc:	39 d8                	cmp    eax,ebx
  fe:	74 11                	je     111 <zero_set15>
 100:	b9 0f 00 00 00       	mov    ecx,0xf
 105:	ba 13 00 00 00       	mov    edx,0x13
 10a:	e8 f1 fe ff ff       	call   0 <write_message>
 10f:	eb 0f                	jmp    120 <end_compare15>

00000111 <zero_set15>:
 111:	b9 00 00 00 00       	mov    ecx,0x0
 116:	ba 0f 00 00 00       	mov    edx,0xf
 11b:	e8 e0 fe ff ff       	call   0 <write_message>

00000120 <end_compare15>:
 120:	b8 00 00 00 00       	mov    eax,0x0
 125:	bb 9c ff ff ff       	mov    ebx,0xffffff9c
 12a:	39 d8                	cmp    eax,ebx
 12c:	74 11                	je     13f <zero_set18>
 12e:	b9 0f 00 00 00       	mov    ecx,0xf
 133:	ba 13 00 00 00       	mov    edx,0x13
 138:	e8 c3 fe ff ff       	call   0 <write_message>
 13d:	eb 0f                	jmp    14e <end_compare18>

0000013f <zero_set18>:
 13f:	b9 00 00 00 00       	mov    ecx,0x0
 144:	ba 0f 00 00 00       	mov    edx,0xf
 149:	e8 b2 fe ff ff       	call   0 <write_message>

0000014e <end_compare18>:
 14e:	b8 9c ff ff ff       	mov    eax,0xffffff9c
 153:	bb 9c ff ff ff       	mov    ebx,0xffffff9c
 158:	39 d8                	cmp    eax,ebx
 15a:	74 11                	je     16d <zero_set21>
 15c:	b9 0f 00 00 00       	mov    ecx,0xf
 161:	ba 13 00 00 00       	mov    edx,0x13
 166:	e8 95 fe ff ff       	call   0 <write_message>
 16b:	eb 0f                	jmp    17c <end_compare21>

0000016d <zero_set21>:
 16d:	b9 00 00 00 00       	mov    ecx,0x0
 172:	ba 0f 00 00 00       	mov    edx,0xf
 177:	e8 84 fe ff ff       	call   0 <write_message>

0000017c <end_compare21>:
 17c:	b9 35 00 00 00       	mov    ecx,0x35
 181:	ba 13 00 00 00       	mov    edx,0x13
 186:	e8 75 fe ff ff       	call   0 <write_message>
 18b:	b9 48 00 00 00       	mov    ecx,0x48
 190:	ba 12 00 00 00       	mov    edx,0x12
 195:	e8 66 fe ff ff       	call   0 <write_message>
 19a:	b8 00 00 00 00       	mov    eax,0x0
 19f:	bb 00 00 00 00       	mov    ebx,0x0
 1a4:	01 d8                	add    eax,ebx
 1a6:	74 11                	je     1b9 <zero_set26>
 1a8:	b9 0f 00 00 00       	mov    ecx,0xf
 1ad:	ba 13 00 00 00       	mov    edx,0x13
 1b2:	e8 49 fe ff ff       	call   0 <write_message>
 1b7:	eb 0f                	jmp    1c8 <end_add26>

000001b9 <zero_set26>:
 1b9:	b9 00 00 00 00       	mov    ecx,0x0
 1be:	ba 0f 00 00 00       	mov    edx,0xf
 1c3:	e8 38 fe ff ff       	call   0 <write_message>

000001c8 <end_add26>:
 1c8:	b8 64 00 00 00       	mov    eax,0x64
 1cd:	bb 00 00 00 00       	mov    ebx,0x0
 1d2:	01 d8                	add    eax,ebx
 1d4:	74 11                	je     1e7 <zero_set29>
 1d6:	b9 0f 00 00 00       	mov    ecx,0xf
 1db:	ba 13 00 00 00       	mov    edx,0x13
 1e0:	e8 1b fe ff ff       	call   0 <write_message>
 1e5:	eb 0f                	jmp    1f6 <end_add29>

000001e7 <zero_set29>:
 1e7:	b9 00 00 00 00       	mov    ecx,0x0
 1ec:	ba 0f 00 00 00       	mov    edx,0xf
 1f1:	e8 0a fe ff ff       	call   0 <write_message>

000001f6 <end_add29>:
 1f6:	b8 00 00 00 00       	mov    eax,0x0
 1fb:	bb 64 00 00 00       	mov    ebx,0x64
 200:	01 d8                	add    eax,ebx
 202:	74 11                	je     215 <zero_set32>
 204:	b9 0f 00 00 00       	mov    ecx,0xf
 209:	ba 13 00 00 00       	mov    edx,0x13
 20e:	e8 ed fd ff ff       	call   0 <write_message>
 213:	eb 0f                	jmp    224 <end_add32>

00000215 <zero_set32>:
 215:	b9 00 00 00 00       	mov    ecx,0x0
 21a:	ba 0f 00 00 00       	mov    edx,0xf
 21f:	e8 dc fd ff ff       	call   0 <write_message>

00000224 <end_add32>:
 224:	b8 64 00 00 00       	mov    eax,0x64
 229:	bb 64 00 00 00       	mov    ebx,0x64
 22e:	01 d8                	add    eax,ebx
 230:	74 11                	je     243 <zero_set35>
 232:	b9 0f 00 00 00       	mov    ecx,0xf
 237:	ba 13 00 00 00       	mov    edx,0x13
 23c:	e8 bf fd ff ff       	call   0 <write_message>
 241:	eb 0f                	jmp    252 <end_add35>

00000243 <zero_set35>:
 243:	b9 00 00 00 00       	mov    ecx,0x0
 248:	ba 0f 00 00 00       	mov    edx,0xf
 24d:	e8 ae fd ff ff       	call   0 <write_message>

00000252 <end_add35>:
 252:	b9 5a 00 00 00       	mov    ecx,0x5a
 257:	ba 12 00 00 00       	mov    edx,0x12
 25c:	e8 9f fd ff ff       	call   0 <write_message>
 261:	b8 9c ff ff ff       	mov    eax,0xffffff9c
 266:	bb 00 00 00 00       	mov    ebx,0x0
 26b:	01 d8                	add    eax,ebx
 26d:	74 11                	je     280 <zero_set39>
 26f:	b9 0f 00 00 00       	mov    ecx,0xf
 274:	ba 13 00 00 00       	mov    edx,0x13
 279:	e8 82 fd ff ff       	call   0 <write_message>
 27e:	eb 0f                	jmp    28f <end_add39>

00000280 <zero_set39>:
 280:	b9 00 00 00 00       	mov    ecx,0x0
 285:	ba 0f 00 00 00       	mov    edx,0xf
 28a:	e8 71 fd ff ff       	call   0 <write_message>

0000028f <end_add39>:
 28f:	b8 64 00 00 00       	mov    eax,0x64
 294:	bb 9c ff ff ff       	mov    ebx,0xffffff9c
 299:	01 d8                	add    eax,ebx
 29b:	74 11                	je     2ae <zero_set42>
 29d:	b9 0f 00 00 00       	mov    ecx,0xf
 2a2:	ba 13 00 00 00       	mov    edx,0x13
 2a7:	e8 54 fd ff ff       	call   0 <write_message>
 2ac:	eb 0f                	jmp    2bd <end_add42>

000002ae <zero_set42>:
 2ae:	b9 00 00 00 00       	mov    ecx,0x0
 2b3:	ba 0f 00 00 00       	mov    edx,0xf
 2b8:	e8 43 fd ff ff       	call   0 <write_message>

000002bd <end_add42>:
 2bd:	b8 9c ff ff ff       	mov    eax,0xffffff9c
 2c2:	bb 64 00 00 00       	mov    ebx,0x64
 2c7:	01 d8                	add    eax,ebx
 2c9:	74 11                	je     2dc <zero_set45>
 2cb:	b9 0f 00 00 00       	mov    ecx,0xf
 2d0:	ba 13 00 00 00       	mov    edx,0x13
 2d5:	e8 26 fd ff ff       	call   0 <write_message>
 2da:	eb 0f                	jmp    2eb <end_add45>

000002dc <zero_set45>:
 2dc:	b9 00 00 00 00       	mov    ecx,0x0
 2e1:	ba 0f 00 00 00       	mov    edx,0xf
 2e6:	e8 15 fd ff ff       	call   0 <write_message>

000002eb <end_add45>:
 2eb:	b8 9c ff ff ff       	mov    eax,0xffffff9c
 2f0:	bb 9c ff ff ff       	mov    ebx,0xffffff9c
 2f5:	01 d8                	add    eax,ebx
 2f7:	74 11                	je     30a <zero_set48>
 2f9:	b9 0f 00 00 00       	mov    ecx,0xf
 2fe:	ba 13 00 00 00       	mov    edx,0x13
 303:	e8 f8 fc ff ff       	call   0 <write_message>
 308:	eb 0f                	jmp    319 <end_add48>

0000030a <zero_set48>:
 30a:	b9 00 00 00 00       	mov    ecx,0x0
 30f:	ba 0f 00 00 00       	mov    edx,0xf
 314:	e8 e7 fc ff ff       	call   0 <write_message>

00000319 <end_add48>:
 319:	b9 6c 00 00 00       	mov    ecx,0x6c
 31e:	ba 1c 00 00 00       	mov    edx,0x1c
 323:	e8 d8 fc ff ff       	call   0 <write_message>
 328:	b8 ff ff ff 7f       	mov    eax,0x7fffffff
 32d:	bb ff ff ff 7f       	mov    ebx,0x7fffffff
 332:	01 d8                	add    eax,ebx
 334:	74 11                	je     347 <zero_set52>
 336:	b9 0f 00 00 00       	mov    ecx,0xf
 33b:	ba 13 00 00 00       	mov    edx,0x13
 340:	e8 bb fc ff ff       	call   0 <write_message>
 345:	eb 0f                	jmp    356 <end_add52>

00000347 <zero_set52>:
 347:	b9 00 00 00 00       	mov    ecx,0x0
 34c:	ba 0f 00 00 00       	mov    edx,0xf
 351:	e8 aa fc ff ff       	call   0 <write_message>

00000356 <end_add52>:
 356:	b8 ff ff ff 7f       	mov    eax,0x7fffffff
 35b:	bb 00 00 00 80       	mov    ebx,0x80000000
 360:	01 d8                	add    eax,ebx
 362:	74 11                	je     375 <zero_set55>
 364:	b9 0f 00 00 00       	mov    ecx,0xf
 369:	ba 13 00 00 00       	mov    edx,0x13
 36e:	e8 8d fc ff ff       	call   0 <write_message>
 373:	eb 0f                	jmp    384 <end_add55>

00000375 <zero_set55>:
 375:	b9 00 00 00 00       	mov    ecx,0x0
 37a:	ba 0f 00 00 00       	mov    edx,0xf
 37f:	e8 7c fc ff ff       	call   0 <write_message>

00000384 <end_add55>:
 384:	b8 00 00 00 80       	mov    eax,0x80000000
 389:	bb 00 00 00 80       	mov    ebx,0x80000000
 38e:	01 d8                	add    eax,ebx
 390:	74 11                	je     3a3 <zero_set58>
 392:	b9 0f 00 00 00       	mov    ecx,0xf
 397:	ba 13 00 00 00       	mov    edx,0x13
 39c:	e8 5f fc ff ff       	call   0 <write_message>
 3a1:	eb 0f                	jmp    3b2 <end_add58>

000003a3 <zero_set58>:
 3a3:	b9 00 00 00 00       	mov    ecx,0x0
 3a8:	ba 0f 00 00 00       	mov    edx,0xf
 3ad:	e8 4e fc ff ff       	call   0 <write_message>

000003b2 <end_add58>:
 3b2:	b8 00 00 00 80       	mov    eax,0x80000000
 3b7:	bb 01 00 00 80       	mov    ebx,0x80000001
 3bc:	01 d8                	add    eax,ebx
 3be:	74 11                	je     3d1 <zero_set61>
 3c0:	b9 0f 00 00 00       	mov    ecx,0xf
 3c5:	ba 13 00 00 00       	mov    edx,0x13
 3ca:	e8 31 fc ff ff       	call   0 <write_message>
 3cf:	eb 0f                	jmp    3e0 <end_add61>

000003d1 <zero_set61>:
 3d1:	b9 00 00 00 00       	mov    ecx,0x0
 3d6:	ba 0f 00 00 00       	mov    edx,0xf
 3db:	e8 20 fc ff ff       	call   0 <write_message>

000003e0 <end_add61>:
 3e0:	b8 01 00 00 00       	mov    eax,0x1
 3e5:	bb 00 00 00 00       	mov    ebx,0x0
 3ea:	cd 80                	int    0x80
