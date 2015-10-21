" ---------------------------------------------
" Vim Script #7
" ---------------------------------------------
" Vim constant and variables

echo v:

let vars = v:
for item in keys(vars)
    echo item
    echo vars[item]
    echo "----------------"
endfor

" finito
