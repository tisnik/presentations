# asmsyntax=as

# Makro pro pripravu a tisk hexadecimalni hodnoty na standardni vystup.
# - pro zapis je pouzita "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



# Makro pro vypis 32bitove hexadecimalni hodnoty na standardni vystup
# Jedinym parametrem makra je hodnota (konstanta)
.macro printHexNumber value
        mov  edx, \value                   # hodnotu pro tisk ulozit do registru EDX
        mov  ebx, offset hexValueTemplate  # adresu pro retezec ulozit do registru EBX
        call hex2string                    # zavolani prislusne subrutiny pro prevod na string
        writeMessage hexValueMessage, hexValueMessageLen # retezec je naplnen, tak ho muzeme vytisknout
.endm



#-----------------------------------------------------------------------------
.section .data
hexValueMessage:
        .string "Hex value: 0x"             # prvni cast zpravy
hexValueTemplate:                           # druha cast zpravy ma vlastni navesti
        .string "????????\n"                # otazniky budou prepsany
hexValueMessageLen = $ - hexValueMessage    # delka zpravy



#-----------------------------------------------------------------------------
.section .text

# Subrutina urcena pro prevod 32bitove hexadecimalni hodnoty na retezec
# Vstup: EDX - hodnota, ktera se ma prevest na retezec
#        EBX - adresa jiz drive alokovaneho retezce (resp. osmice bajtu)
hex2string:
                  mov cl,  8                # pocet opakovani smycky

print_one_digit:  rol edx, 4                # rotace doleva znamena, ze se do spodnich 4 bitu nasune dalsi cifra
                  mov al, dl                # nechceme porusit obsah vstupni hodnoty v EDX, proto pouzijeme AL
                  and al, 0x0f              # maskovani, potrebujeme pracovat jen s jednou cifrou
                  cmp al, 10                # je cifra vetsi nebo rovna 10?
                  jge alpha_digit           # ano je, prevest na znak 'A'..'F'

numeric_digit:    add al, '0'               # neni, prevest na znak '0'..'9' (postacuje pricist ASCII hodnotu '0')
                  jmp store_digit

alpha_digit:      add al, 'A'-10            # prevod hodnoty 10..15 na znaky 'A'..'F'

store_digit:      mov byte ptr [ebx], al    # ulozeni cifry do retezce
                  inc ebx                   # dalsi ulozeni v retezci o znak dale
                  dec cl                    # snizeni pocitadla smycky
                  jnz print_one_digit       # a opakovani smycky, dokud se nedosahlo nuly

                  ret                       # navrat ze subrutiny

