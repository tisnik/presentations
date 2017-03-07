
" ---------------------------------------------
" Vim Script #6
" ---------------------------------------------
" Variables
" 1    g:variable_name    global
" 2    s:variable_name    local for script file
" 3    w:variable_name    local for window (not buffer!)
" 4    t:variable_name    local for tab
" 5    b:variable_name    local for buffer (not window!)
" 6    l:variable_name    'true' local variable (inside function)
" 7    a:variable_name    named function argument
" 8    v:variable_name    Vim constant and variables
" 
echo v:version
" 
" g: t: etc. are dictionaries:
echo "All g: variables:"
echo g:
echo "All t: variables:"
echo t:
echo "All w: variables:"
echo w:
echo "All b: variables:"
echo b:
