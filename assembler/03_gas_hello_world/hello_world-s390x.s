# asmsyntax=as

# Jednoducha aplikace typu "Hello world!" naprogramovana
# v assembleru GNU as.
#
# Autor: Pavel Tisnovsky
#        Dan Horak



# Linux kernel system call table
sys_exit=1
sys_write=4



#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Hello World!\n"

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        la    1,sys_write       # cislo syscallu pro funkci "write"
        la    2,1               # standardni vystup
        larl  3,hello_lbl       # adresa retezce, ktery se ma vytisknout
        la    4,13              # pocet znaku, ktere se maji vytisknout
        svc   0                 # volani Linuxoveho kernelu

        la    1,sys_exit        # cislo sycallu pro funkci "exit"
        la    2,0               # exit code = 0
        svc   0                 # volani Linuxoveho kernelu

