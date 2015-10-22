" ---------------------------------------------
" Vim Script #14
" ---------------------------------------------
" String expressions and operators

let str1 = "hello"
let str2 = "HELLO"

echo "String concatenation:"
echo str . str

echo "Ignore vs. noignorecase"
set ignorecase
" Use :set ignorecase settings
echo str1 == str2
" Don't ignore case
echo str1 ==# str2
" Let's ignore case
echo str1 ==? str2

set noignorecase
" Use :set ignorecase settings
echo str1 == str2
" Don't ignore case
echo str1 ==# str2
" Let's ignore case
echo str1 ==? str2

echo "String comparion"
echo "ax" <  "bx"
echo "ax" <= "bx"
echo "ax" >= "bx"

echo "String comparion and ignore/noignorecase"
echo "Bart" <   "bart"
echo "Bart" <#  "bart"
echo "Bart" <?  "bart"
