" ---------------------------------------------
" Vim8 example script #9 - usage of js_encode()
" function for scalar values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let integerNumber = 42
echo js_encode(integerNumber)

let realNumber = 3.0/2
echo js_encode(realNumber)

let booleanValueTrue = 1==1
echo js_encode(booleanValueTrue)

let booleanValueFalse = 1==2
echo js_encode(booleanValueFalse)

let greetings = "VimPerferct"
echo js_encode(greetings)

