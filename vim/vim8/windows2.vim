" ---------------------------------------------
" Vim8 example script #2 - this script creates
" multiple windows and then prints its numbers
" and unique IDs
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

function! SplitCurrentWindow()
    split

    " create and close ten windows
    for i in range(10)
        split  " split new window
        close  " and close it immediatelly
    endfor

    vsplit
    split
    vsplit
endfunction

function! PrintWindowNumbers()
    let windowNumbers = []
    windo call add(windowNumbers, winnr()) 
    for windowNumber in windowNumbers
        echo windowNumber
    endfor
endfunction

function! PrintWindowIDs()
    let windowIDs = []
    windo call add(windowIDs, win_getid(winnr())) 
    for windowID in windowIDs
        echo windowID
    endfor
endfunction

call SplitCurrentWindow()
call PrintWindowNumbers()
call PrintWindowIDs()

