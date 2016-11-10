# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'printf' pro vypis hodnoty typu double
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "float = %f\n"      # zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .bss

.lcomm number, 8                     # na toto misto se bude ukladat konstanta typu double




#-----------------------------------------------------------------------------
.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:
        sub  rsp, 8                # zajistit zarovnani RSP na adresu delitelnou 16

                                   # prvnim parametrem je adresa zpravy
        mov  rdi, offset hello_world_message

        fldpi                      # druhym parametrem je double konstanta Pi
        fstp  qword ptr number
        movsd xmm0, qword ptr number

        mov  eax, 1                # pocet parametru predanych ve vektorovych registrech
        call printf                # volani funkce 'printf' ze standardni knihovny

        add  rsp, 8                # obnoveni puvodni hodnoty RSP

        xor  eax, eax              # navratova hodnota (exit status)

        ret                        # ukonceni aplikace

