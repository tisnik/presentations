" ---------------------------------------------
" Vim8 example script #15 - usage of json_encode()
" function for special float values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let positiveInfinity = 1.0/0
let negativeInfinity = -1.0/0
let NaN1 = 0.0/0
let NaN2 = 1 + NaN1
let NaN3 = positiveInfinity - positiveInfinity
let NaN4 = positiveInfinity / positiveInfinity

let originalList = [0, 0.0, 1, 1.0, positiveInfinity, negativeInfinity, NaN1, NaN2, NaN3, NaN4]
let jsonList = json_encode(originalList)
echo jsonList

