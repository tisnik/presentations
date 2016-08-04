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
  12 0000 55       		push	rbp
  13              		.cfi_def_cfa_offset 16
  14              		.cfi_offset 6, -16
  15 0001 4889E5   		mov	rbp, rsp
  16              		.cfi_def_cfa_register 6
  17 0004 897DFC   		mov	DWORD PTR [rbp-4], edi
  18 0007 8975F8   		mov	DWORD PTR [rbp-8], esi
   3:test.c        ****     return x+y;
  19              		.loc 1 3 0
  20 000a 8B45F8   		mov	eax, DWORD PTR [rbp-8]
  21 000d 8B55FC   		mov	edx, DWORD PTR [rbp-4]
  22 0010 01D0     		add	eax, edx
   4:test.c        **** }
  23              		.loc 1 4 0
  24 0012 5D       		pop	rbp
  25              		.cfi_def_cfa 7, 8
  26 0013 C3       		ret
  27              		.cfi_endproc
  28              	.LFE0:
  30              		.globl	add3
  32              	add3:
  33              	.LFB1:
   5:test.c        **** 
   6:test.c        **** int add3(int x, int y, int z)
   7:test.c        **** {
  34              		.loc 1 7 0
  35              		.cfi_startproc
  36 0014 55       		push	rbp
  37              		.cfi_def_cfa_offset 16
  38              		.cfi_offset 6, -16
  39 0015 4889E5   		mov	rbp, rsp
  40              		.cfi_def_cfa_register 6
  41 0018 897DFC   		mov	DWORD PTR [rbp-4], edi
  42 001b 8975F8   		mov	DWORD PTR [rbp-8], esi
  43 001e 8955F4   		mov	DWORD PTR [rbp-12], edx
   8:test.c        ****     return x+y+z;
  44              		.loc 1 8 0
  45 0021 8B45F8   		mov	eax, DWORD PTR [rbp-8]
  46 0024 8B55FC   		mov	edx, DWORD PTR [rbp-4]
  47 0027 01C2     		add	edx, eax
  48 0029 8B45F4   		mov	eax, DWORD PTR [rbp-12]
  49 002c 01D0     		add	eax, edx
   9:test.c        **** }
  50              		.loc 1 9 0
  51 002e 5D       		pop	rbp
  52              		.cfi_def_cfa 7, 8
  53 002f C3       		ret
  54              		.cfi_endproc
  55              	.LFE1:
  57              	.Letext0:
