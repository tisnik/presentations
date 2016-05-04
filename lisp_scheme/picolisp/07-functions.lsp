;
; PicoLisp
;
; Demonstration example #7:
; Functions declared by "de"
;
; Author: Pavel Tisnovsky
;

; one-liner function
(de add (x y) (+ x y))

; function written on more lines
(de mul
    (x y)
    (* x y))

; Clojure-like definition
(de div
    [x y]
    (/ x y))

; test functions
(println (add 1 2))
(println (mul 6 7))
(println (div 10 3))

; needed to exit from the interpreter
(bye)

; finito

