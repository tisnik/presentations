
" ---------------------------------------------
" Vim Script #13
" ---------------------------------------------
" Boolean operators
" 
let bool1 = 1
let bool2 = 0
" 
echo "Not, and, or:"
echo !bool1
echo !bool2
echo bool1 && bool2
echo bool1 || bool2
" 
echo "Ternary operator:"
echo bool1 ? "true" : "false"
echo bool2 ? "true" : "false"
" 
echo "String->number->boolean conversion"
echo !0
echo !"0"
echo !1
echo !"1"
