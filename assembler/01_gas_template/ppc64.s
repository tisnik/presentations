# asmsyntax=as

# Sablona pro zdrojovy kod Linuxoveho programu naprogramovaneho
# v assembleru GNU AS.
#
# Author: Pavel Tisnovsky
#         Rafael Fonseca




# Linux kernel system call table
sys_exit=1

#------------------------------------------------------------------------------
.section .data


#------------------------------------------------------------------------------
.section .text
.global _start
.section ".opd", "aw"
.balign 8
_start:
        .quad ._start, .TOC.@tocbase, 0
        .previous

.global ._start
._start:
    li      0,sys_exit  # cislo syscallu pro funkci "exit"
    la      3,0         # exit code = 0
    sc                  # volani Linuxoveho kernelu
