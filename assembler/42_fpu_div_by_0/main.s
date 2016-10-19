# asmsyntax=as

# Program pro otestovani deleni nulou
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



#-----------------------------------------------------------------------------
.section .data
fpuDivideByZeroMessage:
        .string "1/0:   "                        # zprava
fpuDivideByZeroMessageLength = $ - fpuDivideByZeroMessage   # delka zpravy

fpuDivideByNegativeZeroMessage:
        .string "-1/0:  "                        # zprava
fpuDivideByNegativeZeroMessageLength = $ - fpuDivideByNegativeZeroMessage   # delka zpravy

fpuDivideZeroByZeroMessage:
        .string "0/0:   "                        # zprava
fpuDivideZeroByZeroMessageLength = $ - fpuDivideZeroByZeroMessage   # delka zpravy



#-----------------------------------------------------------------------------
.section .bss

.lcomm number, 4                     # na toto misto se bude ukladat konstanta typu float



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        writeMessage fpuDivideByZeroMessage, fpuDivideByZeroMessageLength

        fld1                         # nacteni FP konstanty 1.0
        fldz                         # nacteni FP konstanty 0.0
        fdivp                        # deleni nulou
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        writeMessage fpuDivideByNegativeZeroMessage, fpuDivideByNegativeZeroMessageLength

        fld1                         # nacteni FP konstanty 1.0
        fldz                         # nacteni FP konstanty 0.0
        fchs                         # zmena znamenka nuly
        fdivp                        # deleni zapornou nulou
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        writeMessage fpuDivideZeroByZeroMessage, fpuDivideZeroByZeroMessageLength

        fldz                         # nacteni FP konstanty 0.0
        fldz                         # nacteni FP konstanty 0.0
        fdivp                        # vypocet 0.0/0.0
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        println                      # odradkovani

        exit                         # ukonceni aplikace

