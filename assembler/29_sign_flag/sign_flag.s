# asmsyntax=as

# Program pro otestovani chovani priznaku SF (priznak znamenka)
# - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



# Nacteni definice makra pro ukonceni aplikace
.include "exit.s"

# Nacteni maker pro (opakovany) tisk zpravy i prislusne subrutiny
.include "writeMessage.s"

#-----------------------------------------------------------------------------

# Deklarace makra pro porovnani dvou hodnot a vytisteni stavu priznaku ZF
.macro compareAndShowSignFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        cmp   eax, ebx               # porovnani registru a nastaveni priznaku
        js    sign_set\@             # test na priznak SF
        writeMessage messageSignNotSet, messageSignNotSetLen
        jmp   end_compare\@
sign_set\@:
        writeMessage messageSignSet, messageSignSetLen
end_compare\@:
.endm

# Deklarace makra pro soucet dvou hodnot a vytisteni stavu priznaku ZF
.macro addAndShowSignFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        add   eax, ebx               # soucet registru a nastaveni priznaku
        js    sign_set\@             # test na priznak SF
        writeMessage messageSignNotSet, messageSignNotSetLen
        jmp   end_add\@
sign_set\@:
        writeMessage messageSignSet, messageSignSetLen
end_add\@:
.endm



#-----------------------------------------------------------------------------
.section .data
messageSignSet:
        .string "Sign flag set\n"
messageSignSetLen = $ - messageSignSet  # delka prvni zpravy

messageSignNotSet:
        .string "Sign flag not set\n"
messageSignNotSetLen = $ - messageSignNotSet  # delka druhe zpravy

messageCmp:
        .string "\nInstruction: CMP\n"
messageCmpLen = $ - messageCmp     # delka treti zpravy

messageAdd:
        .string "\nInstruction: ADD\n"
messageAddLen = $ - messageAdd     # delka ctvrte zpravy

messagePositiveValues:
        .string "\nPositive values\n"
messagePositiveValuesLen = $ - messagePositiveValues

messageNegativeValues:
        .string "\nNegative values\n"
messageNegativeValuesLen = $ - messageNegativeValues

message0x7fffffffand0x80000000:
        .string "\n0x7fffffff and 0x80000000\n"
message0x7fffffffand0x80000000Len = $ - message0x7fffffffand0x80000000



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        writeMessage messageCmp, messageCmpLen

        writeMessage messagePositiveValues, messagePositiveValuesLen
        compareAndShowSignFlag    0,   0
        compareAndShowSignFlag  100,   0
        compareAndShowSignFlag    0, 100
        compareAndShowSignFlag  100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        compareAndShowSignFlag -100,    0
        compareAndShowSignFlag    0, -100
        compareAndShowSignFlag -100, -100

        writeMessage messageAdd, messageAddLen

        writeMessage messagePositiveValues, messagePositiveValuesLen
        addAndShowSignFlag   0,   0
        addAndShowSignFlag 100,   0
        addAndShowSignFlag   0, 100
        addAndShowSignFlag 100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        addAndShowSignFlag -100,    0
        addAndShowSignFlag  100, -100
        addAndShowSignFlag -100,  100
        addAndShowSignFlag -100, -100

        writeMessage message0x7fffffffand0x80000000, message0x7fffffffand0x80000000Len
        addAndShowSignFlag 0x7fffffff, 0x7fffffff
        addAndShowSignFlag 0x7fffffff, 0x80000000
        addAndShowSignFlag 0x80000000, 0x80000000
        addAndShowSignFlag 0x80000000, 0x80000001

        exit                              # ukonceni aplikace

