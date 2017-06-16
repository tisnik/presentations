
Regulární výrazy
----------------
" Test zda řetězec vyhovuje či naopak nevyhovuje regulárnímu výrazu
" Operátory =~ a !~
"
let str1 = "hello"
let str2 = "HELLO"
let regexp = "[a-z]*"
" 
echo "String and regexp:"
echo str1 =~ regexp
echo str2 !~ regexp
" 
echo "Ignorecase vs noignorecase:"
set ignorecase
" Use Vim settings
echo str2 =~ "Hello"
" Don't ignore case
echo str2 =~# "Hello"
" Let's ignore case
echo str2 =~? "Hello"
" 
set noignorecase
" Use Vim settings
echo str2 =~ "Hello"
" Don't ignore case
echo str2 =~# "Hello"
" Let's ignore case
echo str2 =~? "Hello"
