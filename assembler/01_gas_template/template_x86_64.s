# asmsyntax=as

# Sablona pro zdrojovy kod Linuxoveho programu naprogramovaneho
# v assembleru GNU AS.
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
sys_exit=60



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        movl  $sys_exit,%eax    # cislo sycallu pro funkci "exit"
        movl  $0,%edi           # exit code = 0
        syscall                 # volani Linuxoveho kernelu

