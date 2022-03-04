# asmsyntax=as

# Presun bloku dat po osmi bajtech.
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
sys_exit=93
sys_write=64

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h

# pocet bajtu pro blokove presuny
rep_count  = 448


# Deklarace makra pro ukonceni aplikace
.macro exit
        mov  x8, #sys_exit      // cislo sycallu pro funkci "exit"
        mov  x0, #0             // exit code = 0
        svc  0                  // volani Linuxoveho kernelu
.endm



# Deklarace makra pro vytisteni zpravy na standardni vystup
.macro writeMessage message,messageLength
        mov  x8, #sys_write       // cislo sycallu pro funkci "write"
        mov  x0, #1               // standardni vystup
        ldr  x1, =\message        // adresa retezce, ktery se ma vytisknout
        mov  x2, #\messageLength  // pocet znaku, ktere se maji vytisknout
        svc  0                    // volani Linuxoveho kernelu
.endm


# Deklarace makra pro presun bloku po osmi bajtech
.macro moveBlockByWords from, to, length
        ldr   x1, =\from        // adresa bloku pro cteni
        ldr   x2, =\to          // adresa bloku pro zapis
        mov   x4, #\length      // pocet bajtu
loop\@:
        ldr   x3, [x1], 8       // cteni osmi bajtu
        str   x3, [x2], 8       // zapis osmi bajtu
        sub   x4, x4, #8        // zmenseni pocitadla
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
        .global _start          // tento symbol ma byt dostupny i linkeru

_start:
        writeMessage buffer, rep_count

        mov   x10, #50000       // pocet opakovani blokoveho presunu
        lsl   x10, x10, #8      // jeste zvetsime pocet opakovani
loop:
        moveBlockByWords hello_lbl, buffer, rep_count
        sub   x10, x10, #1      // snizeni hodnoty pocitadla
        cbnz  x10, loop         // pokud se nedosahlo nuly, opakovat

        writeMessage buffer, rep_count

        exit
