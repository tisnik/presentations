# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'puts'
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "Hello world!\n"    # zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:
        sub  rsp, 8                # zajistit zarovnani RSP na adresu delitelnou 16

                                   # jedinym parametrem je adresa zpravy
        mov  rdi, offset hello_world_message
        call puts                  # volani funkce 'puts' ze standardni knihovny

        add  rsp, 8                # obnoveni puvodni hodnoty RSP

        xor  eax, eax              # navratova hodnota (exit status)
        ret                        # ukonceni aplikace

