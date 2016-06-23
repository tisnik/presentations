# asmsyntax=as
 
# Ukazka spagetoveho kodu s instrukci typu JMP
# - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky
 
.intel_syntax noprefix
 
 
 
# Linux kernel system call table
sys_exit=1
 
 
 
#-----------------------------------------------------------------------------
.section .data
 
 
 
#-----------------------------------------------------------------------------
.section .bss
 
 
 
#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru
 
_start:
        jmp   l1
l4:     
        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu

l2:     jmp   l3

l1:     jmp   l2

l3:     jmp   l4
 
