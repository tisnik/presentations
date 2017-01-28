" ---------------------------------------------
" Vim8 example script #13 - usage of js_encode()
" function for vector (array) values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let vector1 = [1, 2, 3]
echo js_encode(vector1)

let vector2 = ["Hello", "world", "!"]
echo js_encode(vector2)

let matrix1 = [[1,2,3], [4,5,6], [7,8,9]]

echo js_encode(matrix1)

let matrix2 = [[1,2,3],
\             [4,5,6],
\             [7,8,9]]

echo js_encode(matrix2)

