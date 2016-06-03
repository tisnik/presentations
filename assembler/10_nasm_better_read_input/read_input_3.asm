; asmsyntax=nasm

; Aplikace pro precteni dat ze standardniho vstupu.
;
; Autor: Pavel Tisnovsky



; Linux kernel system call table
sys_exit  equ 1
sys_read  equ 3
sys_write equ 4

; Dalsi konstanty pouzite v programu - standardni streamy
std_input  equ 0
std_output equ 1
err_output equ 2



;-----------------------------------------------------------------------------
section .data
        message1:   db 'Enter your name: '
        message1len equ $-message1        ; delka prvni zpravy

        message2:   db 'Hello '
        message2len equ $-message2        ; delka druhe zpravy



;-----------------------------------------------------------------------------
section .bss
        entered:   resd 1                  ; delka vstupu
        input:     resb 50                 ; rezervace 50 bajtu pro vstup



;-----------------------------------------------------------------------------
section .text
        global _start                     ; tento symbol ma byt dostupny i linkeru

_start:
        ; tisk prvni zpravy (vyzvy uzivateli)
        mov   eax, sys_write              ; cislo syscallu pro funkci "write"
        mov   ebx, err_output             ; chybovy vystup
        mov   ecx, message1               ; adresa retezce, ktery se ma vytisknout
        mov   edx, message1len            ; pocet znaku, ktere se maji vytisknout
        int   80h                         ; volani Linuxoveho kernelu

        ; precteni vstupu od uzivatele
        mov   eax, sys_read               ; cislo syscallu pro funkci "read"
        mov   ebx, std_input              ; standardni vstup
        mov   ecx, input                  ; adresa bufferu
        mov   edx, 50                     ; maximalni delka zpravy
        int   80h                         ; volani Linuxoveho kernelu
        mov   [entered], eax ;

        ; tisk druhe zpravy (zacatek odpovedi)
        mov   eax, sys_write              ; cislo syscallu pro funkci "write"
        mov   ebx, err_output             ; chybovy vystup
        mov   ecx, message2               ; adresa retezce, ktery se ma vytisknout
        mov   edx, message2len            ; pocet znaku, ktere se maji vytisknout
        int   80h                         ; volani Linuxoveho kernelu

        ; tisk vstupu od uzivatele
        mov   eax, sys_write              ; cislo syscallu pro funkci "write"
        mov   ebx, std_output             ; standardni vystup
        mov   ecx, input                  ; adresa bufferu
        mov   edx, [entered]                    ; delka (max delka)
        int   80h                         ; volani Linuxoveho kernelu

        mov   eax, sys_exit               ; cislo sycallu pro funkci "exit"
        mov   ebx, 0                      ; exit code = 0
        int   80h                         ; volani Linuxoveho kernelu

