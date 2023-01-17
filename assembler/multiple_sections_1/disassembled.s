
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x0000000000401000

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000022  0000000000401000  0000000000401000  00001000  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .data         0000000e  0000000000402000  0000000000402000  00002000  2**0
                  CONTENTS, ALLOC, LOAD, DATA
SYMBOL TABLE:
no symbols



Disassembly of section .text:

0000000000401000 <.text>:
  401000:	b8 04 00 00 00       	mov    eax,0x4
  401005:	bb 01 00 00 00       	mov    ebx,0x1
  40100a:	b9 00 20 40 00       	mov    ecx,0x402000
  40100f:	ba 0d 00 00 00       	mov    edx,0xd
  401014:	cd 80                	int    0x80
  401016:	b8 01 00 00 00       	mov    eax,0x1
  40101b:	bb 00 00 00 00       	mov    ebx,0x0
  401020:	cd 80                	int    0x80
