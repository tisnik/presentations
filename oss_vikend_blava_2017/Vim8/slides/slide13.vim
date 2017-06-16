
Programová smyčka while
-----------------------
let mylist = ["Answer", "to", "The", "Ultimate", "Question",
              "of", "Life,", "the", "Universe,", "and", "Everything:",
              42]
echo len(mylist)
"
let i = 0
while i < 12
    echo mylist[i]
    let i+=1
endwhile
