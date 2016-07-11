# asmsyntax=as

# Jednoducha aplikace typu "Hello World!" naprogramovana
# v assembleru GNU as.
#
# Author: Pavel Tisnovsky
#         Rafael Fonseca

# Linux kernel system call table
sys_exit=1
sys_write=4



#------------------------------------------------------------------------------
.section .data
hello_lbl:
        .ascii "Hello World!\n"

hello_length = . - hello_lbl




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
        li      0,sys_write             # cislo syscallu pro funkci "write"
        li      3,1                     # fd = 1 (stdout)
        lis     4,hello_lbl@highest     # load buffer
        ori     4,4,hello_lbl@higher
        rldicr  4,4,32,31
        oris    4,4,hello_lbl@h
        ori     4,4,hello_lbl@l
        li      5,hello_length          # size
        sc                              # volani Linuxoveho kernelu

        li      0,sys_exit              # cislo syscallu pro funkci "exit"
        li      3,0                     # exit code = 0
        sc                              # volani Linuxoveho kernelu
