# asmsyntax=as

# Program pro otestovani makra urceneho pro vytisteni hexadecimalni hodnoty.
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



# Nacteni definice makra pro ukonceni aplikace
.include "exit.s"

# Nacteni maker pro (opakovany) tisk zpravy i prislusne subrutiny
.include "writeMessage.s"

# Nacteni makra pro vytisteni hexadecimalni 32bitove hodnoty
# spolecne s makrem je nactena i prislusna subrutina
.include "printDecimalNumber.s"



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        printDecimalNumber 0         # otestujme zakladni hodnoty
        printDecimalNumber 1
        printDecimalNumber 2

        println

        printDecimalNumber 9         # dulezity je i prechod
        printDecimalNumber 10

        println

        printDecimalNumber 99        # dalsi dulezity prechod pro otestovani
        printDecimalNumber 100

        println

        printDecimalNumber 999       # a dalsi...
        printDecimalNumber 1000

        println

        printDecimalNumber -1        # aritmetika se znamenkem - dvojkovym doplnkem
        printDecimalNumber -2
        printDecimalNumber -9
        printDecimalNumber -10

        exit                         # ukonceni aplikace

