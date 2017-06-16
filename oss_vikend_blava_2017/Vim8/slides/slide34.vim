
Postupné zpracování řetězce
---------------------------
let str = "http://www.root.cz"
while str != ""
    echo str
    if str =~ "^root.*"
        break
    endif
    let str = str[1 : strlen(str) - 1]
endwhile
