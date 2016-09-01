# asmsyntax=as

# Program pro otestovani chovani priznaku CF (priznak prenosu)
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
.macro compareAndShowCarryFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        cmp   eax, ebx               # porovnani registru a nastaveni priznaku
        jc    carry_set\@             # test na priznak ZF
        writeMessage messageCarryNotSet, messageCarryNotSetLen
        jmp   end_compare\@
carry_set\@:
        writeMessage messageCarrySet, messageCarrySetLen
end_compare\@:
.endm

# Deklarace makra pro soucet dvou hodnot a vytisteni stavu priznaku ZF
.macro addAndShowCarryFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        add   eax, ebx               # soucet registru a nastaveni priznaku
        jc    carry_set\@             # test na priznak ZF
        writeMessage messageCarryNotSet, messageCarryNotSetLen
        jmp   end_add\@
carry_set\@:
        writeMessage messageCarrySet, messageCarrySetLen
end_add\@:
.endm



#-----------------------------------------------------------------------------
.section .data
messageCarrySet:
        .string "Carry flag set\n"
messageCarrySetLen = $ - messageCarrySet  # delka prvni zpravy

messageCarryNotSet:
        .string "Carry flag not set\n"
messageCarryNotSetLen = $ - messageCarryNotSet  # delka druhe zpravy

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
        compareAndShowCarryFlag    0,   0
        compareAndShowCarryFlag  100,   0
        compareAndShowCarryFlag    0, 100
        compareAndShowCarryFlag  100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        compareAndShowCarryFlag -100,    0
        compareAndShowCarryFlag    0, -100
        compareAndShowCarryFlag -100, -100

        writeMessage messageAdd, messageAddLen

        writeMessage messagePositiveValues, messagePositiveValuesLen
        addAndShowCarryFlag   0,   0
        addAndShowCarryFlag 100,   0
        addAndShowCarryFlag   0, 100
        addAndShowCarryFlag 100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        addAndShowCarryFlag -100,    0
        addAndShowCarryFlag  100, -100
        addAndShowCarryFlag -100,  100
        addAndShowCarryFlag -100, -100

        writeMessage message0x7fffffffand0x80000000, message0x7fffffffand0x80000000Len
        addAndShowCarryFlag 0x7fffffff, 0
        addAndShowCarryFlag 0x7fffffff, 1
        addAndShowCarryFlag 0x7fffffff, 2
        addAndShowCarryFlag 0x7fffffff, 0x7fffffff
        addAndShowCarryFlag 0x7fffffff, 0x80000000
        addAndShowCarryFlag 0x80000000, 0x80000000
        addAndShowCarryFlag 0x80000000, 0x80000001

        exit                              # ukonceni aplikace

