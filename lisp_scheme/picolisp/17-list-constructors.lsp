;
; PicoLisp
;
; Demonstration example #17:
; List constructors
;
; Author: Pavel Tisnovsky
;

(println (cons))
(println (cons 1))
(println (cons 1 2))
(println (cons 1 (2)))
(println (cons 0 (1 2 3 4)))
(println (cons (1 2 3 4) (1 2 3 4)))

(println (list))
(println (list NIL))
(println (list 1 2))
(println (list 1 2 3 4))
(println (list 1 (2 3 4)))

; needed to exit from the interpreter
(bye)

; finito

