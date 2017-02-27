
ID oken
-------
" Funkce bude obecně vracet různá čísla:
function! PrintWindowNumbers()
    let windowNumbers = []
    windo call add(windowNumbers, winnr()) 
    for windowNumber in windowNumbers
        echo windowNumber
    endfor
endfunction
"
" Funkce bude pro jedno okno vždy vracet stejné ID
function! PrintWindowIDs()
    let windowIDs = []
    windo call add(windowIDs, win_getid(winnr())) 
    for windowID in windowIDs
        echo windowID
    endfor
endfunction
