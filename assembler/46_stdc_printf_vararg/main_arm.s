# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'printf' s vetsim poctem parametru
# - varianta urcena pro klasickou 32bitovou architekturu ARM
#
# Autor: Pavel Tisnovsky



#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "char=%c code=%d\n" @ zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main                    @ tento symbol ma byt dostupny i linkeru

main:
        stmfd sp!, {lr}                 @ ulozeni zvolenych registru na zasobnik

        ldr   r0, =hello_world_message  @ adresa zpravy, ktera se ma vytisknout
        mov   r1, #'*'                  @ druhym parametrem je kod znaku
        mov   r2, #42                   @ tretim parametrem je cele cislo

        bl    printf                    @ zavolani knihovni funkce printf()

        mov   r0, #42                   @ navratova hodnota (exit status)
        ldmfd sp!, {pc}                 @ obnova registru, ukonceni aplikace
                                        @ (rizeni se vrati na adresu ulozenou v LR)

