# asmsyntax=as

# - volani funkce 'puts'
# - varianta urcena pro klasickou 32bitovou architekturu ARM


#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "Hello world!\n"         @ zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main                    @ tento symbol ma byt dostupny i linkeru

main:
        stmfd sp!, {lr}                 @ ulozeni zvolenych registru na zasobnik
        ldr   r0, =hello_world_message  @ adresa zpravy, ktera se ma vytisknout
        bl    puts                      @ zavolani knihovni funkce puts()
        mov   r0, #42                   @ navratova hodnota (exit status)
        ldmfd sp!, {pc}                 @ obnova registru, ukonceni aplikace (rizeni se vrati na adresu ulozenou v LR)

