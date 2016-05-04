;
; PicoLisp
;
; Demonstration example #2:
; dotted pairs and its usage in PicoLisp
;
; Author: Pavel Tisnovsky
;

(println (1 . 2))

(println (1 . ((2 . 3) . 4)))

(println '((1 . 2) . (3 . 4)))

; this is the proper list
(println (1 . (2 . (3 . NIL))))

; this is the proper list
(println (1 . (2 . (3 . ()))))

; needed to exit from the interpreter
(bye)

; finito

