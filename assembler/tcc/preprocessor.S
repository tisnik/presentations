# asmsyntax=as

# Sablona pro zdrojovy kod Linuxoveho programu naprogramovaneho
# v assembleru tcc.
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
#include "syscalls.s"

#ifdef XYZZY
naprosto cizí text
naprosto cizí text
naprosto cizí text
#endif

.section .text
        .global main            # tento symbol ma byt dostupny i linkeru

main:
	mov  $sys_write, %rax   # cislo sycallu pro funkci "write"
	mov  $1, %rdi           # handle, 1 = STDOUT
	mov  $message, %rsi     # adresa zpravy
	mov  $length, %rdx      # delka zpravy
	syscall

        mov  $sys_exit, %eax    # cislo sycallu pro funkci "exit"
        mov  $0,%edi            # exit code = 0
        syscall                 # volani Linuxoveho kernelu

message:
	.ascii "Hello, world!\n"
	length = . - message
