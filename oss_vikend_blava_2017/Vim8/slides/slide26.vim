
Ignorecase/noignorecase
-----------------------
echo "Ignore vs. noignorecase"
set ignorecase
" Use :set ignorecase settings
echo str1 == str2
" Don't ignore case
echo str1 ==# str2
" Let's ignore case
echo str1 ==? str2
