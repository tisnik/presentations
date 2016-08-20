# asmsyntax=as

# Ukazka pouziti maker v GNU Assembleru - direktiva .include
# - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix

# Nacteni definice makra pro ukonceni aplikace
.include "exit.s"

# Nacteni maker pro (opakovany) tisk zpravy i prislusne subrutiny
.include "writeMessage.s"



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

