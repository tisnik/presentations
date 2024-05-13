; Jednoducha aplikace typu "Hello world!" naprogramovana
; v assembleru FASM pro Linux na x86.
;
; Autor: Pavel Tisnovsky



format ELF executable 3

sys_exit = 1
sys_write = 4
stdout = 1



segment readable executable

entry main

main:
        lea  ecx, [msg]            ; adresa retezce, ktery se ma tisknout
        mov  edx, length           ; delka retezce vcetne konce radku
        mov  ebx, stdout           ; handle specialniho souboru stdout
        mov  eax, sys_write        ; cislo syscallu pro funkci sys_write 
        int  80h                   ; volani linuxoveho kernelu

        mov  eax, sys_exit         ; cislo syscallu pro funkci sys_exit
        xor  ebx, ebx              ; navratovy kod
        int  80h                   ; volani linuxoveho kernelu



segment readable writable

msg  db 'Hello world!', 10
length = $ - msg
