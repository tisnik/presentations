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
.include "printHexNumber2.s"



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        printHexNumber 0             # otestujme zakladni hodnoty
        printHexNumber 1
        printHexNumber 2

        println

        printHexNumber 9             # dulezity je i prechod '9'->'A'
        printHexNumber 10

        println

        printHexNumber 15            # dalsi dulezity prechod pro otestovani 'F'->'10'
        printHexNumber 16

        println

        printHexNumber 127           # dalsi zajimave hodnoty pro otestovani
        printHexNumber 128
        printHexNumber 255
        printHexNumber 256

        println

        printHexNumber -1            # aritmetika se znamenkem - dvojkovym doplnkem
        printHexNumber -2
        printHexNumber -256

        exit                         # ukonceni aplikace

