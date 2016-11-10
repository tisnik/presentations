# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'printf' s vetsim poctem parametru
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "char=%c code=%d\n" # zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:
        sub  rsp, 8                # zajistit zarovnani RSP na adresu delitelnou 16

                                   # prvnim parametrem je adresa zpravy
        mov  rdi, offset hello_world_message
        mov  rsi, '*'              # druhym parametrem je kod znaku
        mov  rdx, 42               # tretim parametrem je cele cislo
        xor  al, al                # pocet parametru predanych ve vektorovych registrech
        call printf                # volani funkce 'printf' ze standardni knihovny

        add  rsp, 8                # obnoveni puvodni hodnoty RSP

        xor  eax, eax              # navratova hodnota (exit status)

        ret                        # ukonceni aplikace

