# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - varianta urcena pro 64bitovou architekturu AArch64
#
# Autor: Pavel Tisnovsky



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .text
        .global main               // tento symbol ma byt dostupny i linkeru

main:

        mov  x0, #0                // navratova hodnota (exit status)
        // mov  pc, lr             // nelze pouzit!
        ret                        // ukonceni aplikace (rizeni se vrati na adresu ulozenou v LR)

