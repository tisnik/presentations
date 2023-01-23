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
        nop
        jmp   .L1

.L4:     
        nop
        int   0x80                   # volani Linuxoveho kernelu

.L2:    
        mov   ebx, 1                 # exit code = 1
        nop
        jmp   .L3

.L1:    
        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        nop
        jmp   .L2

.L3:    dec    ebx                   # zmena exit code 
        nop
        jmp   .L4
 
