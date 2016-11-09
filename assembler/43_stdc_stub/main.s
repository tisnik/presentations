# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:

        xor  eax, eax              # navratova hodnota (exit status)
        ret                        # ukonceni aplikace

