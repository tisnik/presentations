# asmsyntax=as

# Jednoducha aplikace typu "Hello world!" naprogramovana
# v assembleru GNU as - je pouzita "AT&T" syntaxe
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
sys_write = 4
sys_exit = 1



#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Hello World!\n"     # string, ktery JE ukoncen nulou

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        mov   $sys_write, %eax  # cislo syscallu pro funkci "write"
        mov   $1,%ebx           # standardni vystup
        mov   $hello_lbl,%ecx   # adresa retezce, ktery se ma vytisknout
        mov   $13,%edx          # pocet znaku, ktere se maji vytisknout
        int   $0x80             # volani Linuxoveho kernelu

        movl  $sys_exit,%eax    # cislo sycallu pro funkci "exit"
        movl  $0,%ebx           # exit code = 0
        int   $0x80             # volani Linuxoveho kernelu

