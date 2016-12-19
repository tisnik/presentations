
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x00000000004000b0

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000037  00000000004000b0  00000000004000b0  000000b0  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .bss          00000028  00000000006000e8  00000000006000e8  000000e8  2**3
                  ALLOC
SYMBOL TABLE:
no symbols



Disassembly of section .text:

00000000004000b0 <.text>:
  4000b0:	b9 e8 00 60 00       	mov    ecx,0x6000e8
  4000b5:	bb 28 00 00 00       	mov    ebx,0x28
  4000ba:	b0 2a                	mov    al,0x2a
  4000bc:	67 88 01             	mov    BYTE PTR [ecx],al
  4000bf:	ff c1                	inc    ecx
  4000c1:	ff cb                	dec    ebx
  4000c3:	75 f7                	jne    0x4000bc
  4000c5:	b8 04 00 00 00       	mov    eax,0x4
  4000ca:	bb 01 00 00 00       	mov    ebx,0x1
  4000cf:	b9 e8 00 60 00       	mov    ecx,0x6000e8
  4000d4:	ba 28 00 00 00       	mov    edx,0x28
  4000d9:	cd 80                	int    0x80
  4000db:	b8 01 00 00 00       	mov    eax,0x1
  4000e0:	bb 00 00 00 00       	mov    ebx,0x0
  4000e5:	cd 80                	int    0x80
