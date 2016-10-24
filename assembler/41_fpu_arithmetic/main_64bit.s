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
fpuValueOneMessage:
        .string "1.0:      "                        # zprava
fpuValueOneMessageLength = $ - fpuValueOneMessage   # delka zpravy

fpuAddResultMessage:
        .string "1.0+1.0:  "                        # zprava
fpuAddResultMessageLength = $ - fpuAddResultMessage # delka zpravy

fpuMulResultMessage:
        .string "2.0*3.0:  "                        # zprava
fpuMulResultMessageLength = $ - fpuMulResultMessage # delka zpravy



#-----------------------------------------------------------------------------
.section .bss

.lcomm number, 4                     # na toto misto se bude ukladat konstanta typu float



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        writeMessage fpuValueOneMessage, fpuValueOneMessageLength

        fld1                         # nacteni FP konstanty 1.0
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        writeMessage fpuAddResultMessage, fpuAddResultMessageLength

        fld1                         # nacteni FP konstanty 1.0
        fld1                         # nacteni FP konstanty 1.0
        faddp                        # soucet obou hodnot (1.0+1.0)
        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        writeMessage fpuMulResultMessage, fpuMulResultMessageLength

        fld1                         # nacteni FP konstanty 1.0
        fld1                         # nacteni FP konstanty 1.0
        faddp                        # soucet obou hodnot (1.0+1.0)

        fld1                         # nacteni FP konstanty 1.0
        fld1                         # nacteni FP konstanty 1.0
        fld1                         # nacteni FP konstanty 1.0
        faddp
        faddp                        # soucet vsech tri hodnot (1.0+(1.0+1.0))

        fmulp                        # nyni jsou na zasobniku ulozeny hodnoty 2 a 3 ktere vynasobime

        fstp dword ptr number        # ulozeni do pameti (4 bajty)
        mov  eax, dword ptr number   # nacteni hodnoty, tentokrat to celociselneho registru
        printHexNumber eax           # vytiskneme celociselnou hodnotu v hexa tvaru



        println                      # odradkovani

        exit                         # ukonceni aplikace

