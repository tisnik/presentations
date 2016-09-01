# asmsyntax=as

# Program pro otestovani chovani priznaku OF (priznak preteceni)
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
.macro compareAndShowOverflowFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        cmp   eax, ebx               # porovnani registru a nastaveni priznaku
        jo    overflow_set\@             # test na priznak OF
        writeMessage messageOverflowNotSet, messageOverflowNotSetLen
        jmp   end_compare\@
overflow_set\@:
        writeMessage messageOverflowSet, messageOverflowSetLen
end_compare\@:
.endm

# Deklarace makra pro soucet dvou hodnot a vytisteni stavu priznaku ZF
.macro addAndShowOverflowFlag const1, const2
        mov   eax, \const1
        mov   ebx, \const2
        add   eax, ebx               # soucet registru a nastaveni priznaku
        jo    overflow_set\@             # test na priznak OF
        writeMessage messageOverflowNotSet, messageOverflowNotSetLen
        jmp   end_add\@
overflow_set\@:
        writeMessage messageOverflowSet, messageOverflowSetLen
end_add\@:
.endm



#-----------------------------------------------------------------------------
.section .data
messageOverflowSet:
        .string "Overflow flag set\n"
messageOverflowSetLen = $ - messageOverflowSet  # delka prvni zpravy

messageOverflowNotSet:
        .string "Overflow flag not set\n"
messageOverflowNotSetLen = $ - messageOverflowNotSet  # delka druhe zpravy

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
        compareAndShowOverflowFlag    0,   0
        compareAndShowOverflowFlag  100,   0
        compareAndShowOverflowFlag    0, 100
        compareAndShowOverflowFlag  100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        compareAndShowOverflowFlag -100,    0
        compareAndShowOverflowFlag    0, -100
        compareAndShowOverflowFlag -100, -100

        writeMessage messageAdd, messageAddLen

        writeMessage messagePositiveValues, messagePositiveValuesLen
        addAndShowOverflowFlag   0,   0
        addAndShowOverflowFlag 100,   0
        addAndShowOverflowFlag   0, 100
        addAndShowOverflowFlag 100, 100

        writeMessage messageNegativeValues, messageNegativeValuesLen
        addAndShowOverflowFlag -100,    0
        addAndShowOverflowFlag  100, -100
        addAndShowOverflowFlag -100,  100
        addAndShowOverflowFlag -100, -100

        writeMessage message0x7fffffffand0x80000000, message0x7fffffffand0x80000000Len
        addAndShowOverflowFlag 0x7fffffff, 0
        addAndShowOverflowFlag 0x7fffffff, 1
        addAndShowOverflowFlag 0x7fffffff, 2
        addAndShowOverflowFlag 0x7fffffff, 0x7fffffff
        addAndShowOverflowFlag 0x7fffffff, 0x80000000
        addAndShowOverflowFlag 0x80000000, 0x80000000
        addAndShowOverflowFlag 0x80000000, 0x80000001

        exit                              # ukonceni aplikace

