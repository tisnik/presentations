" ---------------------------------------------
" Vim8 example script #17 - usage of js_encode()
" function for special values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let originalDictionary = {
\    "true1"  : 1==1,
\    "true2"  : v:true,
\    "false1" : 1==2,
\    "false2" : v:false,
\    "null1"  : v:null,
\    "null2"  : v:none,
\    "emptyString"  : ""
\}

let jsonDictionary = js_encode(originalDictionary)
echo jsonDictionary

