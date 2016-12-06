# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'printf' pro zobrazeni casti ASCII tabulky
# - varianta urcena pro klasickou 32bitovou architekturu ARM
#
# Autor: Pavel Tisnovsky



#-----------------------------------------------------------------------------
.section .data
ASCII_char_message:
        .asciz "char=%c code=%d hex=%02x\n" @ zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main                    @ tento symbol ma byt dostupny i linkeru

main:
        stmfd sp!, {lr}                 @ ulozeni zvolenych registru na zasobnik
        mov   r4, #32                   @ inicializace pocitadla

loop:
        ldr   r0, =ASCII_char_message   @ adresa zpravy, ktera se ma vytisknout
        mov   r1, r4                    @ druhym parametrem je kod znaku
        mov   r2, r4                    @ tretim parametrem je totez cele cislo
        mov   r3, r4                    @ ctvrtym parametrem je totez cele cislo

        bl    printf                    @ zavolani knihovni funkce printf()

        add   r4, r4, #1                @ zvyseni hodnoty pocitadla
        cmp   r4, #127                  @ porovnani s koncovou hodnotou smycky
        bne   loop                      @ dosahli jsme konce? pokud ne, skok na zacatek smycky

        mov   r0, #42                   @ navratova hodnota (exit status)
        ldmfd sp!, {pc}                 @ obnova registru, ukonceni aplikace
                                        @ (rizeni se vrati na adresu ulozenou v LR)

