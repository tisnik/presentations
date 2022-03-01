# asmsyntax=as

# Presun bloku dat.
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
sys_exit=93
sys_write=64

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h

# pocet bajtu
rep_count  = 13


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


# Deklarace makra pro presun bloku
.macro moveBlock from,to,length
        ldr   x1, =\from        // adresa bloku pro cteni
        ldr   x2, =\to          // adresa bloku pro zapis
        mov   x4, #\length      // pocet bajtu
loop\@:
        ldrb  w3, [x1], 1       // cteni bajtu
        strb  w3, [x2], 1       // zapis bajtu
        sub   x4, x4, #1        // zmenseni pocitadla a soucasne nastaveni priznaku
        cbnz  x4, loop\@        // pokud jsme se nedostali k nule, skok na zacatek smycky
.endm



#-----------------------------------------------------------------------------
.section .data

hello_lbl:
        .string "Hello World!\n"

buffer:
        .string "************\n"

#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start          // tento symbol ma byt dostupny i linkeru

_start:
        writeMessage buffer, rep_count

        moveBlock hello_lbl, buffer, rep_count
        moveBlock hello_lbl, buffer, rep_count

        writeMessage buffer, rep_count

        exit

