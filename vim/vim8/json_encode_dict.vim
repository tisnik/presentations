" ---------------------------------------------
" Vim8 example script #14 - usage of json_encode()
" function for dictionaries.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let dict1 = {"first": 1, "second" : 2, "third" : 3}
echo json_encode(dict1)

let dict2 = {1 : "first", 2 : "second", 3 : "third"}
echo json_encode(dict2)

let dict3 = {"first" : [1,2,3], "second" : [4,5,6]}
echo json_encode(dict3)

let vectorOfDicts = [ {"first" : 1, "second" : 2}, {"another" : "dictionary"}]
echo json_encode(vectorOfDicts)

