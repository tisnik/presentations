# asmsyntax=as

# Program pro otestovani chovani priznaku ZF (priznak nulovosti)
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
.macro compareAndShowZeroFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        cmp   eax, ebx               # porovnani registru a nastaveni priznaku
        jz    zero_set\@             # test na priznak ZF
        writeMessage messageZeroNotSet, messageZeroNotSetLen
        jmp   end_compare\@
zero_set\@:
        writeMessage messageZeroSet, messageZeroSetLen
end_compare\@:
.endm

# Deklarace makra pro soucet dvou hodnot a vytisteni stavu priznaku ZF
.macro addAndShowZeroFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        add   eax, ebx               # soucet registru a nastaveni priznaku
        jz    zero_set\@             # test na priznak ZF
        writeMessage messageZeroNotSet, messageZeroNotSetLen
        jmp   end_add\@
zero_set\@:
        writeMessage messageZeroSet, messageZeroSetLen
end_add\@:
.endm



#-----------------------------------------------------------------------------
.section .data
messageZeroSet:
        .string "Zero flag set\n"
messageZeroSetLen = $ - messageZeroSet  # delka prvni zpravy

messageZeroNotSet:
        .string "Zero flag not set\n"
messageZeroNotSetLen = $ - messageZeroNotSet  # delka druhe zpravy

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
        compareAndShowZeroFlag    0,   0
        compareAndShowZeroFlag  100,   0
        compareAndShowZeroFlag    0, 100
        compareAndShowZeroFlag  100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        compareAndShowZeroFlag -100,    0
        compareAndShowZeroFlag    0, -100
        compareAndShowZeroFlag -100, -100

        writeMessage messageAdd, messageAddLen

        writeMessage messagePositiveValues, messagePositiveValuesLen
        addAndShowZeroFlag   0,   0
        addAndShowZeroFlag 100,   0
        addAndShowZeroFlag   0, 100
        addAndShowZeroFlag 100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        addAndShowZeroFlag -100,    0
        addAndShowZeroFlag  100, -100
        addAndShowZeroFlag -100,  100
        addAndShowZeroFlag -100, -100

        writeMessage message0x7fffffffand0x80000000, message0x7fffffffand0x80000000Len
        addAndShowZeroFlag 0x7fffffff, 0x7fffffff
        addAndShowZeroFlag 0x7fffffff, 0x80000000
        addAndShowZeroFlag 0x80000000, 0x80000000
        addAndShowZeroFlag 0x80000000, 0x80000001

        exit                              # ukonceni aplikace

