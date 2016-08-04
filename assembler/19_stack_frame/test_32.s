   1              		.file	"test.c"
   2              		.intel_syntax noprefix
   3              		.text
   4              	.Ltext0:
   5              		.globl	add
   7              	add:
   8              	.LFB0:
   9              		.file 1 "test.c"
   1:test.c        **** int add(int x, int y)
   2:test.c        **** {
  10              		.loc 1 2 0
  11              		.cfi_startproc
  12 0000 55       		push	ebp
  13              		.cfi_def_cfa_offset 8
  14              		.cfi_offset 5, -8
  15 0001 89E5     		mov	ebp, esp
  16              		.cfi_def_cfa_register 5
   3:test.c        ****     return x+y;
  17              		.loc 1 3 0
  18 0003 8B450C   		mov	eax, DWORD PTR [ebp+12]
  19 0006 8B5508   		mov	edx, DWORD PTR [ebp+8]
  20 0009 01D0     		add	eax, edx
   4:test.c        **** }
  21              		.loc 1 4 0
  22 000b 5D       		pop	ebp
  23              		.cfi_restore 5
  24              		.cfi_def_cfa 4, 4
  25 000c C3       		ret
  26              		.cfi_endproc
  27              	.LFE0:
  29              		.globl	add3
  31              	add3:
  32              	.LFB1:
   5:test.c        **** 
   6:test.c        **** int add3(int x, int y, int z)
   7:test.c        **** {
  33              		.loc 1 7 0
  34              		.cfi_startproc
  35 000d 55       		push	ebp
  36              		.cfi_def_cfa_offset 8
  37              		.cfi_offset 5, -8
  38 000e 89E5     		mov	ebp, esp
  39              		.cfi_def_cfa_register 5
   8:test.c        ****     return x+y+z;
  40              		.loc 1 8 0
  41 0010 8B450C   		mov	eax, DWORD PTR [ebp+12]
  42 0013 8B5508   		mov	edx, DWORD PTR [ebp+8]
  43 0016 01C2     		add	edx, eax
  44 0018 8B4510   		mov	eax, DWORD PTR [ebp+16]
  45 001b 01D0     		add	eax, edx
   9:test.c        **** }
  46              		.loc 1 9 0
  47 001d 5D       		pop	ebp
  48              		.cfi_restore 5
  49              		.cfi_def_cfa 4, 4
  50 001e C3       		ret
  51              		.cfi_endproc
  52              	.LFE1:
  54              	.Letext0:
