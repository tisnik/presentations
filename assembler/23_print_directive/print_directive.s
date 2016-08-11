# asmsyntax=as

# Ukazka pouziti maker v GNU Assembleru - pouziti direktivy .print pro vypis pocitadla
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

# Deklarace makra pro ukonceni aplikace
.macro exit
        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu
.endm



# Deklarace makra pro vytisteni zpravy na standardni vystup
.macro writeMessage message,messageLength
        mov   ecx, offset \message   # adresa retezce, ktery se ma vytisknout
        mov   edx, \messageLength    # pocet znaku, ktere se maji vytisknout
        call  write_message          # vytisknout zpravu "Zero flag not set"
.endm



# Deklarace makra pro vytisteni zpravy na standardni vystup
.macro writeMessageRepeatedly message,messageLength,count
        mov   ebp, \count            # nastaveni pocitadla
        .print "Declaring label loop\@"
loop\@:                              # lokalni navesti (unikatni)
        mov   ecx, offset \message   # adresa retezce, ktery se ma vytisknout
        mov   edx, \messageLength    # pocet znaku, ktere se maji vytisknout
        call  write_message          # vytisknout zpravu "Zero flag not set"
        dec   ebp                    # snizeni hodnoty pocitadla
        jnz   loop\@                 # opakovani smycky
.endm



#-----------------------------------------------------------------------------
.section .data
message1:
        .string "Hello world\n"
message1len = $ - message1         # delka prvni zpravy

message2:
        .string "Vitejte na mojefedora.cz\n"
message2len = $ - message2         # delka druhe zpravy

message3:
        .string "Assembler je fajn\n"
message3len = $ - message3         # delka druhe zpravy



#-----------------------------------------------------------------------------
.section .bss



#-----------------------------------------------------------------------------
.section .text
        .global _start               # tento symbol ma byt dostupny i linkeru

_start:
        writeMessageRepeatedly message1,message1len,10
        writeMessageRepeatedly message2,message2len,2
        writeMessageRepeatedly message3,message3len,7
        exit                         # ukonceni aplikace



# Podprogram pro vytisteni zpravy na standardni vystup
# Ocekava se, ze v ecx bude adresa zpravy a v edx jeji delka
write_message:
        mov   eax, sys_write         # cislo syscallu pro funkci "write"
        mov   ebx, std_output        # standardni vystup
        int   0x80
        ret

