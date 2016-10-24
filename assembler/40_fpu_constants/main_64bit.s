# asmsyntax=as

# Program pro otestovani zakladnich FPU operaci
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
.include "printHexNumber_64bit.s"



#-----------------------------------------------------------------------------
.section .data
fpuValueZeroMessage:
        .string "0.0: "                             # zprava
fpuValueZeroMessageLength = $ - fpuValueZeroMessage # delka zpravy

fpuValueOneMessage:
        .string "1.0: "                             # zprava
fpuValueOneMessageLength = $ - fpuValueOneMessage   # delka zpravy

fpuValuePiMessage:
        .string "Pi:  "                             # zprava
fpuValuePiMessageLength = $ - fpuValuePiMessage     # delka zpravy



#-----------------------------------------------------------------------------
.section .bss

.lcomm number, 4                     # na toto misto se bude ukladat konstanta typu float



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        writeMessage fpuValueZeroMessage, fpuValueZeroMessageLength

        fldz                         # nacteni FP konstanty 0.0
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        writeMessage fpuValueOneMessage, fpuValueOneMessageLength

        fld1                         # nacteni FP konstanty 1.0
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        writeMessage fpuValuePiMessage, fpuValuePiMessageLength

        fldpi                        # nacteni FP konstanty Pi
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        println                      # odradkovani

        exit                         # ukonceni aplikace

