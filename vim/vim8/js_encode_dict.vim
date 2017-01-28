" ---------------------------------------------
" Vim8 example script #15 - usage of js_encode()
" function for dictionaries.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let dict1 = {"first": 1, "second" : 2, "third" : 3}
echo js_encode(dict1)

let dict2 = {1 : "first", 2 : "second", 3 : "third"}
echo js_encode(dict2)

let dict3 = {"first" : [1,2,3], "second" : [4,5,6]}
echo js_encode(dict3)

let vectorOfDicts = [ {"first" : 1, "second" : 2}, {"another" : "dictionary"}]
echo js_encode(vectorOfDicts)

