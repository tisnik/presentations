; Ukazka pouziti maker ve FASMu
;
; Autor: Pavel Tisnovsky



format ELF executable 3

; Linux kernel system call table
sys_exit   = 1
sys_write  = 4

; Dalsi konstanty pouzite v programu - standardni streamy
std_input  = 0
std_output = 1



; Deklarace makra pro ukonceni aplikace
macro exit {
        mov   eax, sys_exit          ; cislo sycallu pro funkci "exit"
        mov   ebx, 0                 ; exit code = 0
        int   0x80                   ; volani Linuxoveho kernelu
}



; Deklarace makra pro vytisteni zpravy na standardni vystup
macro writeMessage message,messageLength {
        mov   ecx, message           ; adresa retezce, ktery se ma vytisknout
        mov   edx, messageLength     ; pocet znaku, ktere se maji vytisknout
        call  write_message
}



segment readable executable

entry main

main:
        writeMessage message1,message1len
        writeMessage message2,message2len
        writeMessage message3,message3len
        exit                         ; ukonceni aplikace



; Podprogram pro vytisteni zpravy na standardni vystup
; Ocekava se, ze v ecx bude adresa zpravy a v edx jeji delka
write_message:
        mov   eax, sys_write         ; cislo syscallu pro funkci "write"
        mov   ebx, std_output        ; standardni vystup
        int   0x80
        ret



segment readable writable

message1 db 'Hello world', 10
message1len = $ - message1         ; delka prvni zpravy

message2 db 'Vitejte na root.cz', 10
message2len = $ - message2         ; delka druhe zpravy

message3 db 'Assembler je fajn', 10
message3len = $ - message3         ; delka druhe zpravy
