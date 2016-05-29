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
	basr  13,0		# nastaveni literal poolu
.L0:	ahi   13,.LT0-.L0
        la    1,sys_write       # cislo syscallu pro funkci "write"
        la    2,1               # standardni vystup
        l     3,.LC1-.LT0(13)   # adresa retezce, ktery se ma vytisknout
        la    4,13              # pocet znaku, ktere se maji vytisknout
        svc   0                 # volani Linuxoveho kernelu

        la    1,sys_exit        # cislo sycallu pro funkci "exit"
        la    2,0               # exit code = 0
        svc   0                 # volani Linuxoveho kernelu

# literal pool
.LT0:
.LC1:	.long	hello_lbl
