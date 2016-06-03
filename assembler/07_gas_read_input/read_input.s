# asmsyntax=as

# Aplikace pro precteni dat ze standardniho vstupu
# naprogramovana v assembleru GNU as - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix


# Linux kernel system call table
sys_exit  = 1
sys_read  = 3
sys_write = 4

# Dalsi konstanty pouzite v programu - standardni streamy
std_input  = 0
std_output = 1



#-----------------------------------------------------------------------------
.section .data

message1:
        .ascii "Enter your name: "         # string, ktery NENI ukoncen nulou
        message1len = $ - message1         # delka prvni zpravy

message2:
        .ascii "Hello "                    # string, ktery NENI ukoncen nulou
        message2len = $ - message2         # delka druhe zpravy



#-----------------------------------------------------------------------------
.section .bss
        .lcomm input,  50                  # rezervace 50 bajtu pro vstup



#-----------------------------------------------------------------------------
.section .text
        .global _start                     # tento symbol ma byt dostupny i linkeru

_start:
        # tisk prvni zpravy (vyzvy)
        mov   eax, sys_write               # cislo syscallu pro funkci "write"
        mov   ebx, std_output              # standardni vystup
        mov   ecx, offset message1         # adresa retezce, ktery se ma vytisknout
        mov   edx, message1len             # pocet znaku, ktere se maji vytisknout
        int   0x80                         # volani Linuxoveho kernelu

        # precteni vstupu od uzivatele
        mov   eax, sys_read                # cislo syscallu pro funkci "read"
        mov   ebx, std_input               # standardni vstup
        mov   ecx, offset input            # adresa bufferu
        mov   edx, 50                      # maximalni delka zpravy
        int   0x80                         # volani Linuxoveho kernelu

        # tisk druhe zpravy (zacatek odpovedi)
        mov   eax, sys_write               # cislo syscallu pro funkci "write"
        mov   ebx, std_output              # standardni vystup
        mov   ecx, offset message2         # adresa retezce, ktery se ma vytisknout
        mov   edx, message2len             # pocet znaku, ktere se maji vytisknout
        int   0x80                         # volani Linuxoveho kernelu

        # tisk vstupu od uzivatele
        mov   eax, sys_write               # cislo syscallu pro funkci "write"
        mov   ebx, std_output              # standardni vystup
        mov   ecx, offset input            # adresa bufferu
        mov   edx, 50                      # delka (max delka)
        int   0x80                         # volani Linuxoveho kernelu

        mov   eax, sys_exit                # cislo sycallu pro funkci "exit"
        mov   ebx, 0                       # exit code = 0
        int   0x80                         # volani Linuxoveho kernelu

