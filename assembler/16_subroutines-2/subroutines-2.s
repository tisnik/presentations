# asmsyntax=as

# Program pro otestovani chovani instrukci CALL a RET spolecne
# s ukladanim parametru na zasobnik
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



#-----------------------------------------------------------------------------
.section .data
message1:                          # adresa prvni zpravy
        .string "Hello World\n"
message1len = $ - message1 - 1     # delka prvni zpravy

message2:                          # adresa druhe zpravy
        .string "Assembler je fajn\n"
message2len = $ - message2 - 1     # delka druhe zpravy



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        call  writeFirstMessage      # zavolani podprogramu pro vytisteni prvni zpravy
        call  writeSecondMessage     # zavolani podprogramu pro vytisteni druhe zpravy
        call  exit                   # zavolani podprogramu pro ukonceni procesu



# Podprogram pro vytisteni prvni zpravy
writeFirstMessage:
        push  offset message1        # adresa retezce, ktery se ma vytisknout
        push  message1len            # pocet znaku, ktere se maji vytisknout
        call  writeMessage           # zavolani podprogramu pro vytisteni zpravy
        ret                          # navrat z podprogramu



# Podprogram pro vytisteni druhe zpravy
writeSecondMessage:
        push  offset message2        # adresa retezce, ktery se ma vytisknout
        push  message2len            # pocet znaku, ktere se maji vytisknout
        call  writeMessage           # zavolani podprogramu pro vytisteni zpravy
        ret                          # navrat z podprogramu



# Podprogram pro vytisteni zpravy na standardni vystup
# Ocekava se, ze v ecx bude adresa zpravy a v edx jeji delka
writeMessage:
        pop   ebp                    # ulozime na chvili navratovou adresu do EBP
        pop   edx                    # ziskame v poradi druhy ulozeny parametr
        pop   ecx                    # ziskame v poradi prvni ulozeny parametr
        mov   eax, sys_write         # cislo syscallu pro funkci "write"
        mov   ebx, std_output        # standardni vystup
        int   0x80                   # volani Linuxoveho kernelu
        push  ebp                    # obnovime navratovou adresu
        ret                          # navrat z podprogramu



# Podprogram pro ukonceni procesu zavolanim syscallu
exit:
        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu

# finito

