
" ---------------------------------------------
" Vim Script #4
" ---------------------------------------------
" Usage of lists
" Usage of while loop
"
let mylist = ["Answer", "to", "The", "Ultimate", "Question",
              "of", "Life,", "the", "Universe,", "and", "Everything:",
              42]
"
let i = 0
while i < 12
    echo mylist[i]
    let i+=1
endwhile
