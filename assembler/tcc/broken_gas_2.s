# Linux kernel system call table
sys_write = 1
sys_exit  = 60


.section .text
        .global _start             # tento symbol ma byt dostupny i linkeru

_start:
	mov  $sys_write, %rax      # cislo sycallu pro funkci "sys_write" na architekture x86-64
	mov  $1, %rdi              # handle, 1 = STDOUT
	mov  $message, %rsi        # adresa zpravy
	mvv  $length, %rdx         # delka zpravy (neznama instrukce)
	syscall                    # zavolat funkci Linuxoveho kernelu

        mov  $sys_exit, %rax       # cislo sycallu pro funkci "sys_exit" na architekture x86-64
        mov  $0, %rdi              # exit code = 0
        syscall                    # zavolat funkci Linuxoveho kernelu

message:
	.ascii "Hello, world!\n"   # zprava, ktera se ma vypsat
	length = . - message       # vypocet delky zpravy primo v prubehu preklad
