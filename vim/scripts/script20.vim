" ---------------------------------------------
" Vim Script #20
" ---------------------------------------------
" Yank register, working with matrices etc.

let matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
let yank_reg = ""
for row in matrix
    for item in row
        let yank_reg = yank_reg . "\t" . (item*2)
    endfor
    let yank_reg = yank_reg . "\n"
endfor
let @" = yank_reg
normal p

