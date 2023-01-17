
a.out:     file format elf64-x86-64
architecture: i386:x86-64, flags 0x00000102:
EXEC_P, D_PAGED
start address 0x0000000000401000

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000022  0000000000401000  0000000000401000  00001000  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .section_c    0000000a  0000000000402000  0000000000402000  00002000  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .data         0000000e  000000000040300a  000000000040300a  0000200a  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  3 .section_a    0000000a  0000000000000000  0000000000000000  00002018  2**0
                  CONTENTS, READONLY
  4 .section_b    0000000a  0000000000000000  0000000000000000  00002022  2**0
                  CONTENTS, READONLY, CODE
  5 .section_d    0000000a  0000000000000000  0000000000000000  0000202c  2**0
                  CONTENTS, READONLY
  6 .section_e    0000000a  0000000000000000  0000000000000000  00002036  2**0
                  CONTENTS
SYMBOL TABLE:
no symbols



Disassembly of section .text:

0000000000401000 <.text>:
  401000:	b8 04 00 00 00       	mov    eax,0x4
  401005:	bb 01 00 00 00       	mov    ebx,0x1
  40100a:	b9 0a 30 40 00       	mov    ecx,0x40300a
  40100f:	ba 0d 00 00 00       	mov    edx,0xd
  401014:	cd 80                	int    0x80
  401016:	b8 01 00 00 00       	mov    eax,0x1
  40101b:	bb 00 00 00 00       	mov    ebx,0x0
  401020:	cd 80                	int    0x80

Disassembly of section .section_b:

0000000000000000 <.section_b>:
   0:	53                   	push   rbx
   1:	45                   	rex.RB
   2:	43 54                	rex.XB push r12
   4:	49                   	rex.WB
   5:	4f                   	rex.WRXB
   6:	4e 20 42 00          	rex.WRX and BYTE PTR [rdx+0x0],r8b
