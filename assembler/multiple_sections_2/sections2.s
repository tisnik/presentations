# asmsyntax=as

.intel_syntax noprefix


# Linux kernel system call table
sys_exit=1
sys_write=4

#-----------------------------------------------------------------------------

# ruzne sekce (segmenty) se specifickymi atributy

.section .section_a
       .string "SECTION A"

.section .section_b,"x"
       .string "SECTION B"

.section .section_c,"a"
       .string "SECTION C"

.section .section_d,"l"
       .string "SECTION D"

.section .section_e,"w"
       .string "SECTION E"



#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Hello World!\n"     # string, ktery JE ukoncen nulou

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        mov   eax, sys_write         # cislo syscallu pro funkci "write"
        mov   ebx, 1                 # standardni vystup
        mov   ecx, offset hello_lbl  # adresa retezce, ktery se ma vytisknout
        mov   edx, 13                # pocet znaku, ktere se maji vytisknout
        int   0x80                   # volani Linuxoveho kernelu

        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu

