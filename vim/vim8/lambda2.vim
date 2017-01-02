" ---------------------------------------------
" Vim8 example script #5 - lambda expressions
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let  sequence = range(10)
echo "sequence1=" sequence
echo "\n"

let  sequence2 = map(copy(sequence), {index, value -> value * 2})
echo "sequence1=" sequence
echo "sequence2=" sequence2
echo "\n"

let  sequence3 = map(copy(sequence2), {index, value -> value * 2})
echo "sequence1=" sequence
echo "sequence2=" sequence2
echo "sequence3=" sequence3

