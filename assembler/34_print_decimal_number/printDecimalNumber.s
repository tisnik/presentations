# asmsyntax=as

# Makro pro pripravu a tisk desitkove hodnoty na standardni vystup.
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



# Makro pro vypis 32bitove desitkove hodnoty na standardni vystup
# Jedinym parametrem makra je hodnota (konstanta)
.macro printDecimalNumber value
        mov  eax, \value                       # hodnotu pro tisk ulozit do registru EAX
        mov  ebx, offset decimalValueTemplate  # adresu pro retezec ulozit do registru EBX
        call decimal2string                    # zavolani prislusne subrutiny pro prevod na string
        writeMessage decimalValueMessage, decimalValueMessageLen # retezec je naplnen, tak ho muzeme vytisknout
.endm



#-----------------------------------------------------------------------------
.section .data
decimalValueMessage:
        .string "Decimal value: "              # prvni cast zpravy
decimalValueTemplate:                          # druha cast zpravy ma vlastni navesti
        .string "??????????\n"                 # otazniky budou prepsany (musi jich byt presne deset!)
decimalValueMessageLen = $ - decimalValueMessage    # delka zpravy



#-----------------------------------------------------------------------------
.section .text

# Subrutina urcena pro prevod 32bitove desitkove hodnoty na retezec
# Vstup: EDX - hodnota, ktera se ma prevest na retezec
#        EBX - adresa jiz drive alokovaneho retezce (resp. minimalne deseti bajtu)
decimal2string:
                  mov ecx, 10              # celkovy pocet zapisovanych cifer/znaku
                  mov edi, ecx             # instrukce DIV vyzaduje deleni registrem, pouzijme tedy EDI

next_digit:
                  xor edx, edx             # delenec je dvojice EDX:EAX, vynulujeme tedy horni registr EDX
                  div edi                  # deleni hodnoty ulozene v EDX:EAX deseti (delitelem je EDI)
                                           # vysledek se ulozi do EAX, zbytek do EDX
                                           # pri deleni deseti je jistota, ze zbytek je jen cislo 0..9

                  add dl, '0'              # prevod hodnoty 0..9 na znak '0'-'9'

                  mov byte ptr [ebx+ecx-1], dl # zapis retezce (od posledniho znaku)

                  dec ecx                  # presun na predchozi znak v retezci a soucasne snizeni hodnoty pocitadla
                  jnz next_digit           # uz jsme dosli k poslednimu cislu?

                  ret                      # navrat ze subrutiny

