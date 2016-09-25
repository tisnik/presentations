# asmsyntax=as

# Program pro otestovani instrukce BSR
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
.include "printHexNumber.s"

# Nacteni makra pro vytisteni decimalni 32bitove hodnoty
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
        mov ebx, 0x00000001
        printHexNumber ebx
        bsr eax, ebx
        printDecimalNumber eax
        println

        mov ebx, 0x00000002
        printHexNumber ebx
        bsr eax, ebx
        printDecimalNumber eax
        println

        mov ebx, 0x0000f000          # sada ctyr jednicek za sebou
        printHexNumber ebx
        bsr eax, ebx
        printDecimalNumber eax
        println

        mov ebx, 0x00010000
        printHexNumber ebx
        bsr eax, ebx
        printDecimalNumber eax
        println

        mov ebx, 0x80000000
        printHexNumber ebx
        bsr eax, ebx
        printDecimalNumber eax
        println

        mov ebx, 0x80000001          # jednickovy je pouze nejnizsi a nejvyssi bit
        printHexNumber ebx
        bsr eax, ebx
        printDecimalNumber eax
        println

        mov ebx, 0x00000000
        printHexNumber ebx
        bsr eax, ebx                 # nahodna hodnota
        printDecimalNumber eax
        println

        exit                         # ukonceni aplikace

