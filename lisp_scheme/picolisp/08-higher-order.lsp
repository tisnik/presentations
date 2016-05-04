;
; PicoLisp
;
; Demonstration example #8:
; Higher order functions.
;
; Author: Pavel Tisnovsky
;

; regular function
(de inc
    (x)
    (+ x 1)) 

; use inc in higher order function
(println (mapcar inc (1 2 3)))

; use + in higher order function
(println (apply + (1 2 3 4)))

(de add
    (x y)
    (+ x y))

(println (apply add (1 2 3 4)))

(println (apply * (range 1 6)))

; higher order function in other (regular) function
(de factorial
    (n)
    (apply * (range 1 n)))

(println (factorial 10))

; needed to exit from the interpreter
(bye)

; finito

