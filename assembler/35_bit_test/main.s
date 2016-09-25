# asmsyntax=as

# Program pro otestovani instrukce BT
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



.macro testAndPrintBitValue word,bitIndex
        mov ebx, \word
        mov al, '0'                        # ASCII kod znaku, ktery se ma vepsat do sablony
        bt  ebx, \bitIndex                 # pokud je testovany bit jednickovy, nastavi se i Carry Flag
        adc al, 0                          # pricteni Carry Flagu ke znaku "0"
        mov [bitValueTemplate], al         # zapis do sablony
        writeMessage bitValueMessage, bitValueMessageLen  # vypis celeho retezce na standardni vystup
.endm

#-----------------------------------------------------------------------------
.section .data
bitValueMessage:
        .string "Bit value: "              # prvni cast zpravy
bitValueTemplate:                          # druha cast zpravy ma vlastni navesti
        .string "?\n"                      # otaznik bude prepsan
bitValueMessageLen = $ - bitValueMessage   # delka zpravy



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        printHexNumber 0x00000001
        testAndPrintBitValue 0x00000001, 0
        testAndPrintBitValue 0x00000001, 1
        testAndPrintBitValue 0x00000001, 31
        println

        printHexNumber 0x80000000
        testAndPrintBitValue 0x80000000, 0
        testAndPrintBitValue 0x80000000, 1
        testAndPrintBitValue 0x80000000, 31
        println

        printHexNumber 0xffffffff
        testAndPrintBitValue 0xffffffff, 0
        testAndPrintBitValue 0xffffffff, 1
        testAndPrintBitValue 0xffffffff, 31
        println

        exit                         # ukonceni aplikace

