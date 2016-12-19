# asmsyntax=as
 
# Testovaci program naprogramovany v assembleru GNU as
# - pocitana programova smycka s testem na zacatku
# - uprava pro mikroprocesory s architekturou AArch64
#
# Autor: Pavel Tisnovsky
 
 
 
# Linux kernel system call table
sys_exit   = 93
sys_write  = 64
 
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
        mov   x2, #rep_count+1       // pocet opakovani znaku
        mov   w3, #'*'               // zapisovany znak
loop:
        sub   x2, x2, #1             // zmenseni pocitadla
        cmp   x2, #0                 // otestovani, zda jsme jiz nedosahli nuly
        beq   konec                  // pokud jsme se dostali k nule, konec smycky
        strb  w3, [x1]               // zapis znaku do bufferu
        add   x1, x1, #1             // uprava ukazatele do bufferu
        b     loop                   // nepodmineny skok na zacatek smycky
konec:
 
        mov   x8, #sys_write         // cislo syscallu pro funkci "write"
        mov   x0, #std_output        // standardni vystup
        ldr   x1, =buffer            // adresa retezce, ktery se ma vytisknout
        mov   x2, #rep_count         // pocet znaku, ktere se maji vytisknout
        svc   0                      // volani Linuxoveho kernelu
 
        mov   x8, #sys_exit          // cislo sycallu pro funkci "exit"
        mov   x0, #0                 // exit code = 0
        svc   0                      // volani Linuxoveho kernelu

