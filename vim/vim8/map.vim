" ---------------------------------------------
" Vim8 example script #3 - usage of map()
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

function! DoubleValue(index, value)
    return a:value * 2
endfunction

let  sequence = range(10)
echo sequence

let  Funcref = function("DoubleValue")

call map(sequence, Funcref)
echo sequence

call map(sequence, Funcref)
echo sequence

