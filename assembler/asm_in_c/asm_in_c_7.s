	.file	"asm_in_c_7.c"
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
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movq	y(%rip), %rdx
	movq	x(%rip), %rax
#APP
# 9 "asm_in_c_7.c" 1
	mov    %rax, %rax;   
	add    %rdx, %rax;   
	
# 0 "" 2
#NO_APP
	movl	$.LC0, %esi
	movq	%rax, %rdx
	movq	%rax, result(%rip)
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.comm	result,8,8
	.globl	y
	.data
	.align 16
	.type	y, @object
	.size	y, 8
y:
	.quad	20
	.globl	x
	.align 16
	.type	x, @object
	.size	x, 8
x:
	.quad	10
	.ident	"GCC: (Ubuntu 4.8.4-2ubuntu1~14.04.4) 4.8.4"
	.section	.note.GNU-stack,"",@progbits
