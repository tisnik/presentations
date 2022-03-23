# asmsyntax=as

# Přesuny mezi celočíselnými a FP registry
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
        mov  x1, #0x1234        // načtení celočíselné konstanty
        fmov d1, x1             // přenos do FP registru
        fmov x2, d1             // zpětný přenos do celočíselného registru

        mov  x8, #sys_exit      // číslo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volání Linuxového kernelu
