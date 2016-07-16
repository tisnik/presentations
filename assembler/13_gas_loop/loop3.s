# asmsyntax=as
 
# Testovaci program naprogramovany v assembleru GNU as
# - smycka vyuzivajici instrukci CMP
# - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky
 
.intel_syntax noprefix
 
 
# Linux kernel system call table
sys_exit   = 1
sys_write  = 4
 
# Dalsi konstanty pouzite v programu - standardni streamy
std_input  = 0
std_output = 1

# pocet opakovani znaku
rep_count='z'-'a'+1
 
 
 
#-----------------------------------------------------------------------------
.section .data
 
 
 
#-----------------------------------------------------------------------------
.section .bss
        .lcomm buffer, rep_count     # rezervace bufferu pro vystup
 
 
 
#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru
 
_start:
        mov   ecx, offset buffer     # zapis se bude provadet do tohoto bufferu
        mov   al, 'a'                # kod prvniho zapisovaneho znaku
loop:
        mov   [ecx], al              # zapis znaku do bufferu
        inc   al                     # ASCII kod dalsiho znaku
        inc   ecx                    # uprava ukazatele do bufferu
        cmp   al, 'z'+1              # ma se smycka ukoncit?
        jnz   loop                   # pokud jsme neprekrocili kod 'z', opakovat smycku
 
        mov   eax, sys_write         # cislo syscallu pro funkci "write"
        mov   ebx, std_output        # standardni vystup
        mov   ecx, offset buffer     # adresa retezce, ktery se ma vytisknout
        mov   edx, rep_count         # pocet znaku, ktere se maji vytisknout
        int   0x80                   # volani Linuxoveho kernelu
 
        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu

