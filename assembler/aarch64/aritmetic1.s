# asmsyntax=as

# Zakladni aritmeticke instrukce
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

result_lbl:
        .string "x=?\ny=?\n"

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol má být dostupný i linkeru

_start:
        ldr  x3, =result_lbl    // adresa řetězce, ktery se ma vytisknout

        mov  x0, #1             // prvni operand
        mov  x1, #2             // druhy operand
        add  x0, x0, x1         // operace souctu

        mov  x2, #'0'           // prvni cifra v ASCII kodu
        add  x0, x0, x2         // převod na ASCII
        strb w0, [x3, 2]        // zapis znaku s vyuzitim offsetu

        mov  x0, #1000          // prvni operand
        mov  x1, #995           // druhy operand
        sub  x0, x0, x1         // operace souctu

        mov  x2, #'0'           // prvni cifra v ASCII kodu
        add  x0, x0, x2         // převod na ASCII
        strb w0, [x3, 6]        // zapis znaku s vyuzitim offsetu

        mov  x8, #sys_write     // číslo sycallu pro funkci "write"
        mov  x0, #1             // standardni vystup
        ldr  x1, =result_lbl    // adresa řetězce, ktery se ma vytisknout
        mov  x2, #8             // počet znaku, ktere se maji vytisknout
        svc  0                  // volání Linuxového kernelu

        mov  x8, #sys_exit      // číslo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volání Linuxového kernelu
