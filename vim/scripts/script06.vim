" ---------------------------------------------
" Vim Script #5
" ---------------------------------------------
" Usage of lists
" Usage of for-each loop

" Alternative: vim -S script5.vim

let mylist = ["Answer", "to", "The", "Ultimate", "Question", "of", "Life,", "the", "Universe,", "and", "Everything:", 42]

for item in mylist
    echo item
endfor

" finito
