# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'printf' pro vypis hodnoty typu double
# - varianta urcena pro klasickou 32bitovou architekturu ARM
#
# Autor: Pavel Tisnovsky



#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "double = %f\n"          @ zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main                    @ tento symbol ma byt dostupny i linkeru

main:
        stmfd sp!, {lr}                 @ ulozeni zvolenych registru na zasobnik

        ldr   r0, =hello_world_message  @ adresa zpravy, ktera se ma vytisknout
        ldr   r1, number+4
        ldr   r2, number

        bl    printf                    @ zavolani knihovni funkce printf()

        mov   r0, #42                   @ navratova hodnota (exit status)
        ldmfd sp!, {pc}                 @ obnova registru, ukonceni aplikace
                                        @ (rizeni se vrati na adresu ulozenou v LR)
number:
	.word	0xbff00000              @ prvnich 32 bitu cisla
	.word	0x10010000              @ druhych 32 bitu cisla
