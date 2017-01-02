" ---------------------------------------------
" Vim8 example script #4 - lambda expressions
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let  sequence = range(10)
echo sequence

call map(sequence, {index, value -> value * 2})
echo sequence

call map(sequence, {index, value -> value * 2})
echo sequence

