# asmsyntax=as

# Testovaci program naprogramovany v assembleru GNU as
# - pocitana programova smycka realizovana instrukci CBNZ
# - uprava pro mikroprocesory s architekturou AArch64
#
# Autor: Pavel Tisnovsky



# Linux kernel system call table
sys_exit   = 93
sys_write  = 64

# List of syscalls for AArch64:
# https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h

# Dalsi konstanty pouzite v programu - standardni streamy
std_input  = 0
std_output = 1

# pocet opakovani znaku
rep_count  = 40



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .bss
        .lcomm buffer, rep_count     // rezervace bufferu pro vystup



#-----------------------------------------------------------------------------
.section .text
        .global _start               // tento symbol ma byt dostupny i linkeru

_start:
        ldr   x1, =buffer            // zapis se bude provadet do tohoto bufferu
        mov   x2, #rep_count         // pocet opakovani znaku
        mov   w3, #'*'               // zapisovany znak
loop:
        strb  w3, [x1], 1            // zapis znaku do bufferu s post-inkrementaci adresy
        sub   x2, x2, #1             // zmenseni pocitadla a soucasne nastaveni priznaku
        cbnz  x2, loop               // pokud jsme se nedostali k nule, skok na zacatek smycky

        mov   x8, #sys_write         // cislo syscallu pro funkci "write"
        mov   x0, #std_output        // standardni vystup
        ldr   x1, =buffer            // adresa retezce, ktery se ma vytisknout
        mov   x2, #rep_count         // pocet znaku, ktere se maji vytisknout
        svc   0                      // volani Linuxoveho kernelu

        mov   x8, #sys_exit          // cislo sycallu pro funkci "exit"
        mov   x0, #0                 // exit code = 0
        svc   0                      // volani Linuxoveho kernelu

