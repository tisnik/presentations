ideal
model   tiny                    ;pametovy model CS=DS=SS<64kB
p286                            ;povoleny instrukce procesoru 286+

;-----------------------------------------------------------------------------
dataseg                         ;zacatek data-segmentu

message   db      "Hello world!$"

;-----------------------------------------------------------------------------
codeseg                         ;zacatek code-segmentu
org     0100h                   ;zacatek kodu pro programy typu COM

start:

;------ Tisk retezce na obrazovku
        mov     dx, offset message
        mov     ah, 9
        int     21h

;------ Vyprazdnit buffer klavesnice a cekat na klavesu
        xor     ax, ax
        int     16h

;------ Ukonceni procesu
        retn

end start
