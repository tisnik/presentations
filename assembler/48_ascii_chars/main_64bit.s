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
        .asciz "char=%c code=%d hex=%02x\n" # zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:
        sub  rsp, 8                # zajistit zarovnani RSP na adresu delitelnou 16

        mov  r12, 32               # pocitadlo je v prvnim registru, jehoz obsah je zachovan
                                   # i po zavolani funkce printf()
loop:
                                   # prvnim parametrem je adresa zpravy
        mov  rdi, offset hello_world_message
        mov  rsi, r12              # druhym parametrem je kod znaku
        mov  rdx, r12              # tretim parametrem je cele cislo
        mov  rcx, r12              # tretim parametrem je taktez cele cislo
        xor  al, al                # pocet parametru predanych ve vektorovych registrech
        call printf                # volani funkce 'printf' ze standardni knihovny

        inc  r12                   # zvyseni hodnoty pocitadla
        cmp  r12, 127              # konec smycky?
        jne  loop                  # ne, dalsi iterace

        add  rsp, 8                # obnoveni puvodni hodnoty RSP

        xor  eax, eax              # navratova hodnota (exit status)

        ret                        # ukonceni aplikace

