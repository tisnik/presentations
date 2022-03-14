# asmsyntax=as

# Jednoducha aplikace typu "Hello world!" naprogramovana
# v assembleru GNU as.
#
# Autor: Pavel Tišnovský



# Linux kernel system call table
sys_exit=93
sys_write=64

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h



#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Hello World!\n"

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol má být dostupný i linkeru

_start:
        mov  x8, #sys_write     // číslo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =hello_lbl     // adresa řetězce, ktery se ma vytisknout
        mov  x2, #13            // počet znaku, ktere se maji vytisknout
        svc  0                  // volání Linuxového kernelu

        mov  x8, #sys_exit      // číslo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volání Linuxového kernelu

