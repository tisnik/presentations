; Jednoducha aplikace typu "Hello world!" naprogramovana
; v assembleru FASM pro DOS, vysledkem je soubor "flat soubor".
;
;
; pouziti DOS funkce Print String
; https://www.stanislavs.org/helppc/int_21-9.html



format binary as "COM"

        mov     ah, 9        ; kod funkce Print String
        mov     dx, message  ; adresa zpravy ukoncene dolarem
        int     21h          ; volani funkce DOSu

        xor     ax, ax       ; navratovy kod
        retn                 ; navrat do DOSu

; zprava v kodovem segmentu
message db 'Hello world!$'