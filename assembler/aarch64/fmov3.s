# asmsyntax=as

# Načtení FP konstanty do registru s1 - chybný příklad
# v assembleru GNU AS pro architekturu AArch64.
#
# Autor: Pavel Tišnovský



# Linux kernel system call table
sys_exit=93

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol má být dostupný i z linkeru

_start:
        fmov s1, #0.00          // načtení konstanty do registru

        mov  x8, #sys_exit      // číslo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volání Linuxového kernelu

