" ---------------------------------------------
" Vim8 example script #12 - usage of json_encode()
" function for vector (array) values.
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

let vector1 = [1, 2, 3]
echo json_encode(vector1)

let vector2 = ["Hello", "world", "!"]
echo json_encode(vector2)

let matrix1 = [[1,2,3], [4,5,6], [7,8,9]]

echo json_encode(matrix1)

let matrix2 = [[1,2,3],
\             [4,5,6],
\             [7,8,9]]

echo json_encode(matrix2)

