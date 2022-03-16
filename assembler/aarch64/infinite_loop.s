# asmsyntax=as

# Nekonečná smyčka
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

message:
        .string "Diamons are forever!\n"
end_string:

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol má být dostupný i linkeru

_start:

loop:
        mov  x8, #sys_write     // číslo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =message       // adresa řetězce, ktery se ma vytisknout
        mov  x2, #(end_string-message)   // počet znaku, ktere se maji vytisknout
        svc  0                  // volání Linuxového kernelu

        b    loop               // dokolecka dokola
