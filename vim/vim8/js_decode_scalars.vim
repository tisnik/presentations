" ---------------------------------------------
" Vim8 example script #11 - usage of js_decode()
" function for scalar values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let integerNumber = 42
let jsonValue = json_encode(integerNumber)
echo js_decode(jsonValue)

let realNumber = 3.0/2
let jsonValue = json_encode(realNumber)
echo js_decode(jsonValue)

let booleanValueTrue = 1==1
let jsonValue = json_encode(booleanValueTrue)
echo js_decode(jsonValue)

let booleanValueFalse = 1==2
let jsonValue = json_encode(booleanValueFalse)
echo js_decode(jsonValue)

let greetings = "VimPerferct"
let jsonValue = json_encode(greetings)
echo js_decode(jsonValue)

