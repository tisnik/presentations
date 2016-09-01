# asmsyntax=as

# Makro pro ukonceni procesu v Linuxu.
#
# Autor: Pavel Tisnovsky

sys_exit   = 1

# Deklarace makra pro ukonceni aplikace
.macro exit
        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu
.endm

