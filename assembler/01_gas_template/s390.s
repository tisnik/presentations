# asmsyntax=as

# Sablona pro zdrojovy kod Linuxoveho programu naprogramovaneho
# v assembleru GNU AS.
#
# Autor: Pavel Tisnovsky
#        Dan Horak



# Linux kernel system call table
sys_exit=1



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        la    1,sys_exit        # cislo sycallu pro funkci "exit"
        la    2,0               # exit code = 0
        svc   0                 # volani Linuxoveho kernelu

	# pro syscally < 256 funguje i nasledujici
#	la	2,0
#	svc	sys_exit

