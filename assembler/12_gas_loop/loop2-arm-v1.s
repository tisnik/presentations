# asmsyntax=as
 
# Testovaci program naprogramovany v assembleru GNU as
# - pocitana programova smycka s testem na zacatku
# - uprava pro mikroprocesory s architekturou ARM
#
# Autor: Pavel Tisnovsky
 
 
 
# Linux kernel system call table
sys_exit   = 1
sys_write  = 4
 
# Dalsi konstanty pouzite v programu - standardni streamy
std_input  = 0
std_output = 1

# pocet opakovani znaku
rep_count  = 40
 
 
 
#-----------------------------------------------------------------------------
.section .data
 
 
 
#-----------------------------------------------------------------------------
.section .bss
        .lcomm buffer, rep_count     @ rezervace bufferu pro vystup
 
 
 
#-----------------------------------------------------------------------------
.section .text
        .global _start               @ tento symbol ma byt dostupny i linkeru
 
_start:
        ldr   r1, =buffer            @ zapis se bude provadet do tohoto bufferu
        mov   r2, $rep_count+1       @ pocet opakovani znaku
        mov   r3, #'*'               @ zapisovany znak
loop:
        sub   r2, r2, #1             @ zmenseni pocitadla
        cmp   r2, #0                 @ otestovani, zda jsme jiz nedosahli nuly
        beq   konec                  @ pokud jsme se dostali k nule, konec smycky
        strb  r3, [r1]               @ zapis znaku do bufferu
        add   r1, r1, #1             @ uprava ukazatele do bufferu
        b     loop                   @ nepodmineny skok na zacatek smycky
konec:
 
        mov   r7, $sys_write         @ cislo syscallu pro funkci "write"
        mov   r0, $std_output        @ standardni vystup
        ldr   r1, =buffer            @ adresa retezce, ktery se ma vytisknout
        mov   r2, $rep_count         @ pocet znaku, ktere se maji vytisknout
        svc   0                      @ volani Linuxoveho kernelu
 
        mov   r7, $sys_exit          @ cislo sycallu pro funkci "exit"
        mov   r0, #0                 @ exit code = 0
        svc   0                      @ volani Linuxoveho kernelu

