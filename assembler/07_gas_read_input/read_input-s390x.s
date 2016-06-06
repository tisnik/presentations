# asmsyntax=as

# Aplikace pro precteni dat ze standardniho vstupu
# naprogramovana v assembleru GNU as.
#
# Autor: Pavel Tisnovsky
#        Dan Horák


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
        message1len = . - message1         # delka prvni zpravy

        .align 2                           # musime zajistit zarovnani pro instrukci larl
message2:
        .ascii "Hello "                    # string, ktery NENI ukoncen nulou
        message2len = . - message2         # delka druhe zpravy



#-----------------------------------------------------------------------------
.section .bss
        .lcomm input,  50                  # rezervace 50 bajtu pro vstup



#-----------------------------------------------------------------------------
.section .text
        .global _start                     # tento symbol ma byt dostupny i linkeru

_start:
        # tisk prvni zpravy (vyzvy)
        la    1,sys_write                  # cislo syscallu pro funkci "write"
        la    2,std_output                 # standardni vystup
        larl  3,message1                   # adresa retezce, ktery se ma vytisknout
        la    4,message1len                # pocet znaku, ktere se maji vytisknout
        svc   0                            # volani Linuxoveho kernelu

        # precteni vstupu od uzivatele
        la    1,sys_read                   # cislo syscallu pro funkci "read"
        la    2,std_input                  # standardni vstup
        larl  3,input                      # adresa bufferu
        la    4,50                         # maximalni delka zpravy
        svc   0                            # volani Linuxoveho kernelu

        # tisk druhe zpravy (zacatek odpovedi)
        la    1,sys_write                  # cislo syscallu pro funkci "write"
        la    2,std_output                 # standardni vystup
        larl  3,message2                   # adresa retezce, ktery se ma vytisknout
        la    4,message2len                # pocet znaku, ktere se maji vytisknout
        svc   0                            # volani Linuxoveho kernelu

        # tisk vstupu od uzivatele
        la    1,sys_write                  # cislo syscallu pro funkci "write"
        la    2,std_output                 # standardni vystup
        larl  3,input                      # adresa bufferu
        la    4,50                         # delka (max delka)
        svc   0                            # volani Linuxoveho kernelu

        la    1,sys_exit                   # cislo sycallu pro funkci "exit"
        la    2,0                          # exit code = 0
        svc   0                            # volani Linuxoveho kernelu

