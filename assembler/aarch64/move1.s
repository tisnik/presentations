# asmsyntax=as

# Presun bloku dat.
#
# Autor: Pavel Tišnovský



# Linux kernel system call table
sys_exit=93
sys_write=64

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h

# počet bajtu
rep_count  = 13


#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Hello World!\n"

buffer:
        .string "************\n"

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol má být dostupný i linkeru

_start:
        mov  x8, #sys_write     // číslo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =buffer        // adresa řetězce, ktery se ma vytisknout
        mov  x2, #rep_count     // počet znaku, ktere se maji vytisknout
        svc  0                  // volání Linuxového kernelu

        ldr   x1, =hello_lbl    // adresa bloku pro cteni
        ldr   x2, =buffer       // adresa bloku pro zapis
        mov   x4, #rep_count    // počet bajtu
loop:
        ldrb  w3, [x1], 1       // cteni bajtu
        strb  w3, [x2], 1       // zapis bajtu
        sub   x4, x4, #1        // zmenseni pocitadla
        cbnz  x4, loop          // pokud jsme se nedostali k nule, skok na zacatek smycky

        mov  x8, #sys_write     // číslo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =buffer        // adresa řetězce, ktery se ma vytisknout
        mov  x2, #rep_count     // počet znaku, ktere se maji vytisknout
        svc  0                  // volání Linuxového kernelu

        mov  x8, #sys_exit      // číslo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volání Linuxového kernelu
