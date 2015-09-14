; asmsyntax=nasm

; Jednoducha aplikace typu "Hello world!" naprogramovana
; v assembleru NASM.
;
; Autor: Pavel Tisnovsky



; Linux kernel system call table
sys_exit  equ 1
sys_write equ 4



;-----------------------------------------------------------------------------
section .data
        hello:        db 'Hello world!',10
        ; $ obsahuje aktualni adresu v dobe prekladu
        helloLength:  equ $-hello



;-----------------------------------------------------------------------------
section .bss



;-----------------------------------------------------------------------------
section .text
        global _start           ; tento symbol ma byt dostupny i linkeru

_start:
        mov   eax,sys_write     ; cislo syscallu pro funkci "write"
        mov   ebx,1             ; standardni vystup
        mov   ecx,hello         ; adresa retezce, ktery se ma vytisknout
        mov   edx,helloLength   ; helloLength je konstanta, nikoli adresa!
        int   80h               ; volani Linuxoveho kernelu

        mov   eax,sys_exit      ; cislo sycallu pro funkci "exit"
        mov   ebx,0             ; exit code = 0
        int   80h               ; volani Linuxoveho kernelu

