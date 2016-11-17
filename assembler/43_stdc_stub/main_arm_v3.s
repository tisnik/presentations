# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - varianta urcena pro klasickou 32bitovou architekturu ARM
#
# Autor: Pavel Tisnovsky



#-----------------------------------------------------------------------------
.section .data



#-----------------------------------------------------------------------------
.section .text
        .global main                @ tento symbol ma byt dostupny i linkeru

main:
        stmfd sp!, {lr}             @ ulozeni registru LR na zasobnik
        mov   r0, #42               @ navratova hodnota (exit status)
        ldmfd sp!, {pc}             @ ukonceni aplikace (rizeni se vrati na adresu ulozenou v LR)

