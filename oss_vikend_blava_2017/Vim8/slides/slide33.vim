
Řetězce - přístup ke znakům či podřetězcům
------------------------------------------
let str = "http://www.root.cz"
while str != ""
    echo str
    let str = str[1 : strlen(str) - 1]
endwhile
