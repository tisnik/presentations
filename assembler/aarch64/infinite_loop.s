# asmsyntax=as

# Nekonečná smyčka
# v assembleru GNU as.
#
# Autor: Pavel Tisnovsky



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
        .global _start          // tento symbol ma byt dostupny i linkeru

_start:

loop:
        mov  x8, #sys_write     // cislo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =message       // adresa retezce, ktery se ma vytisknout
        mov  x2, #(end_string-message)   // pocet znaku, ktere se maji vytisknout
        svc  0                  // volani Linuxoveho kernelu

        b    loop               // dokolecka dokola
