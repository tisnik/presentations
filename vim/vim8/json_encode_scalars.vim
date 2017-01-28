" ---------------------------------------------
" Vim8 example script #8 - usage of json_encode()
" function for scalar values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let integerNumber = 42
echo json_encode(integerNumber)

let realNumber = 3.0/2
echo json_encode(realNumber)

let booleanValueTrue = 1==1
echo json_encode(booleanValueTrue)

let booleanValueFalse = 1==2
echo json_encode(booleanValueFalse)

let greetings = "VimPerfect"
echo json_encode(greetings)

