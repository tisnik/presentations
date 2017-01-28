" ---------------------------------------------
" Vim8 example script #10 - usage of json_decode()
" function for scalar values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let integerNumber = 42
let jsonValue = json_encode(integerNumber)
echo json_decode(jsonValue)

let realNumber = 3.0/2
let jsonValue = json_encode(realNumber)
echo json_decode(jsonValue)

let booleanValueTrue = 1==1
let jsonValue = json_encode(booleanValueTrue)
echo json_decode(jsonValue)

let booleanValueFalse = 1==2
let jsonValue = json_encode(booleanValueFalse)
echo json_decode(jsonValue)

let greetings = "VimPerferct"
let jsonValue = json_encode(greetings)
echo json_decode(jsonValue)

