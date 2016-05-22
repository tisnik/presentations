# asmsyntax=as

# Sablona pro zdrojovy kod Linuxoveho programu naprogramovaneho
# v assembleru GNU AS.
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
sys_exit=1



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          @ tento symbol ma byt dostupny i z linkeru

_start:
        mov   r7,$sys_exit      @ cislo sycallu pro funkci "exit"
        mov   r0,#0             @ exit code = 0
        svc   0                 @ volani Linuxoveho kernelu

