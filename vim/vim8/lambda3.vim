" ---------------------------------------------
" Vim8 example script #6 - lambda expressions
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let  sequence = range(10)
echo "sequence1=" sequence
echo "\n"

let  sequence2 = filter(copy(sequence), {index, value -> value % 2 == 0})
let  sequence3 = filter(copy(sequence), {index, value -> value % 3 == 0})
echo "sequence1=" sequence
echo "sequence2=" sequence2
echo "sequence3=" sequence3

