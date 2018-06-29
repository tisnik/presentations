	.file	"asm_in_c_3.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%Ld\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
#APP
# 7 "asm_in_c_3.c" 1
	mov    $42, %rbx;   
	mov    %rbx, %rdx;    
	
# 0 "" 2
#NO_APP
	movl	$.LC0, %esi
	movl	$1, %edi
	xorl	%eax, %eax
	movq	%rdx, result(%rip)
	call	__printf_chk
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.comm	result,8,8
	.ident	"GCC: (Ubuntu 4.8.4-2ubuntu1~14.04.4) 4.8.4"
	.section	.note.GNU-stack,"",@progbits
