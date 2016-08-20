# asmsyntax=as

# Makro pro tisk zpravy na standardni vystup.
#
# Autor: Pavel Tisnovsky

# Linux kernel system call table
sys_write  = 4
std_output = 1


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
        writeMessage \message, \messageLength
        dec   ebp                    # snizeni hodnoty pocitadla
        jnz   loop\@                 # opakovani smycky
.endm



# Podprogram pro vytisteni zpravy na standardni vystup
# Ocekava se, ze v ecx bude adresa zpravy a v edx jeji delka
write_message:
        mov   eax, sys_write         # cislo syscallu pro funkci "write"
        mov   ebx, std_output        # standardni vystup
        int   0x80
        ret

