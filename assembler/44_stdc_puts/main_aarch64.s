# asmsyntax=as

# Program pro otestovani volani funkci ze standardni knihovny jazyka C
# - volani funkce 'puts'
# - varianta urcena pro klasickou 32bitovou architekturu ARM
#
# Autor: Pavel Tisnovsky



#-----------------------------------------------------------------------------
.section .data
hello_world_message:
        .asciz "Hello world!\n"         // zprava, ktera se ma vytisknout na standardni vystup



#-----------------------------------------------------------------------------
.section .text
        .global main                    // tento symbol ma byt dostupny i linkeru

main:
        stp   x29, x30, [sp, -16]!      // ulozeni dvojice registru na zasobnik, zajisteni zarovnani
        ldr   x0, =hello_world_message  // adresa zpravy, ktera se ma vytisknout
        bl    puts                      // zavolani knihovni funkce puts()
        mov   w0, #42                   // navratova hodnota (exit status)
        ldp   x29, x30, [sp], 16        // obnoveni dvojice registru
        ret                             // navrat z funkces/subrutiny main

