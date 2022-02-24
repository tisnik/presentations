# asmsyntax=as

# Jednoducha aplikace typu "Hello world!" naprogramovana
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

hello_lbl:
        .string "Hello World!\n"

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol ma byt dostupny i linkeru

_start:
        ldr  x1, =hello_lbl     // adresa retezce, ktery se ma vytisknout
        mov  w2, #'*'           // znak ktery zapiseme do retezce
        strb w2, [x1, 5]        // zapis znaku s vyuzitim offsetu

        mov  x8, #sys_write     // cislo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =hello_lbl     // adresa retezce, ktery se ma vytisknout
        mov  x2, #13            // pocet znaku, ktere se maji vytisknout
        svc  0                  // volani Linuxoveho kernelu

        mov  x8, #sys_exit      // cislo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volani Linuxoveho kernelu
