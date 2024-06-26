# asmsyntax=as

# Presun bloku dat po jednotlivych bajtech.
#
# Autor: Pavel Tišnovský



# Linux kernel system call table
sys_exit=93
sys_write=64

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h

# počet bajtu pro blokove presuny
rep_count  = 448


# Deklarace makra pro ukonceni aplikace
.macro exit
        mov  x8, #sys_exit      // číslo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volání Linuxového kernelu
.endm



# Deklarace makra pro vytisteni zpravy na standardni vystup
.macro writeMessage message,messageLength
        mov  x8, #sys_write       // číslo sycallu pro funkci "write"
        mov  x0, #1               // standardni vystup
        ldr  x1, =\message        // adresa řetězce, ktery se ma vytisknout
        mov  x2, #\messageLength  // počet znaku, ktere se maji vytisknout
        svc  0                    // volání Linuxového kernelu
.endm


# Deklarace makra pro presun bloku po bajtech
.macro moveBlockByBytes from, to, length
        ldr   x1, =\from        // adresa bloku pro cteni
        ldr   x2, =\to          // adresa bloku pro zapis
        mov   x4, #\length      // počet bajtu
loop\@:
        ldrb  w3, [x1], 1       // cteni bajtu
        strb  w3, [x2], 1       // zapis bajtu
        sub   x4, x4, #1        // zmenseni pocitadla
        cbnz  x4, loop\@        // pokud jsme se nedostali k nule, skok na zacatek smycky
.endm


.balign 8

#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum<pad>"


#-----------------------------------------------------------------------------
.section .bss

        .lcomm buffer, rep_count     // rezervace bufferu pro vystup



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol má být dostupný i linkeru

_start:
        writeMessage buffer, rep_count

        mov   x10, #50000       // počet opakovani blokoveho presunu
        lsl   x10, x10, #8      // jeste zvetsime počet opakovani
loop:
        moveBlockByBytes hello_lbl, buffer, rep_count
        sub   x10, x10, #1      // snizeni hodnoty pocitadla
        cbnz  x10, loop         // pokud se nedosahlo nuly, opakovat

        writeMessage buffer, rep_count

        exit
