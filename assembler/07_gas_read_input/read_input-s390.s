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
        basr  13,0                         # nastaveni literal poolu
.L0:    ahi   13,.LT0-.L0

        # tisk prvni zpravy (vyzvy)
        la    1,sys_write                  # cislo syscallu pro funkci "write"
        la    2,std_output                 # standardni vystup
        l     3,.LC1-.LT0(13)              # adresa retezce, ktery se ma vytisknout
        la    4,message1len                # pocet znaku, ktere se maji vytisknout
        svc   0                            # volani Linuxoveho kernelu

        # precteni vstupu od uzivatele
        la    1,sys_read                   # cislo syscallu pro funkci "read"
        la    2,std_input                  # standardni vstup
        l     3,.LC3-.LT0(13)              # adresa bufferu
        la    4,50                         # maximalni delka zpravy
        svc   0                            # volani Linuxoveho kernelu

        # tisk druhe zpravy (zacatek odpovedi)
        la    1,sys_write                  # cislo syscallu pro funkci "write"
        la    2,std_output                 # standardni vystup
        l     3,.LC2-.LT0(13)              # adresa retezce, ktery se ma vytisknout
        la    4,message2len                # pocet znaku, ktere se maji vytisknout
        svc   0                            # volani Linuxoveho kernelu

        # tisk vstupu od uzivatele
        la    1,sys_write                  # cislo syscallu pro funkci "write"
        la    2,std_output                 # standardni vystup
        l     3,.LC3-.LT0(13)              # adresa bufferu
        la    4,50                         # delka (max delka)
        svc   0                            # volani Linuxoveho kernelu

        la    1,sys_exit                   # cislo sycallu pro funkci "exit"
        la    2,0                          # exit code = 0
        svc   0                            # volani Linuxoveho kernelu

# literal pool
.LT0:
.LC1:   .long   message1
.LC2:   .long   message2
.LC3:   .long   input
