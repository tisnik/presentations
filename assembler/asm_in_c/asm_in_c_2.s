	.file	"asm_in_c_2.c"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
#APP
# 5 "asm_in_c_2.c" 1
	nop   
	
# 0 "" 2
#NO_APP
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.8.4-2ubuntu1~14.04.4) 4.8.4"
	.section	.note.GNU-stack,"",@progbits
