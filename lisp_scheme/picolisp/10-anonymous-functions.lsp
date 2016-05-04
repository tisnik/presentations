;
; PicoLisp
;
; Demonstration example #10:
; Anonymous functions
;
; Author: Pavel Tisnovsky
;

; anonymous function used in higher order function
(println (mapcar (quote (x) (+ x 1) ) (1 2 3 4)))

; anonymous function used in higher order function
(println (mapcar (quote (x) (* x x)) (range 1 10)) )

; anonymous function used in higher order function
(println (mapcar (quote (n) (apply * (range 1 n) )) (range 1 10))           )

; needed to exit from the interpreter
(bye)

; finito

