" ---------------------------------------------
" Vim Script #18
" ---------------------------------------------
" While, strlen etc.

let str = "http://www.root.cz"
while str != ""
    echo str
    let str = str[1 : strlen(str) - 1]
endwhile

