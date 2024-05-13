; Jednoducha aplikace typu "Hello world!" naprogramovana
; v assembleru FASM pro Linux na x86-64.
;
; Autor: Pavel Tisnovsky



format ELF64 executable 3

sys_exit = 60
sys_write = 1
stdout = 1



segment readable executable

entry main

main:
        lea  rsi, [msg]            ; adresa retezce, ktery se ma tisknout
        mov  rdx, 13               ; delka retezce vcetne konce radku
        mov  rdi, stdout           ; handle specialniho souboru stdout
        mov  rax, sys_write        ; cislo syscallu pro funkci sys_write 
        syscall                    ; volani linuxoveho kernelu

        mov  rax, sys_exit         ; cislo syscallu pro funkci sys_exit
        xor  rdi, rdi              ; navratovy kod
        syscall                    ; volani linuxoveho kernelu



segment readable writable

msg  db 'Hello world!', 10
