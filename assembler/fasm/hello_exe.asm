; Jednoducha aplikace typu "Hello world!" naprogramovana
; v assembleru FASM pro DOS, vysledkem je soubor .EXE.
;
;
; pouziti DOS funkci Print String a Terminate Process
; https://www.stanislavs.org/helppc/int_21-9.html
; https://www.stanislavs.org/helppc/int_21-4c.html



format MZ

        push    cs
        pop     ds           ; DS = CS

        mov     ah, 9        ; kod funkce Print String
        mov     dx, message  ; adresa zpravy ukoncene dolarem
        int     21h          ; volani funkce DOSu

        mov     ax,4C00h     ; kod funkce Terminate Process With Return Code
        int     21h          ; volani funkce DOSu

; zprava v kodovem segmentu
message db 'Hello world!$'
