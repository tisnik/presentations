;
; PicoLisp
;
; Demonstration example #3:
; lists as basic data structure
;
; Author: Pavel Tisnovsky
;

(println '(1 2 3 4))

; create list and assign it to symbol
; (=variable)
(setq a '(1 2 3))

; get first item
(println (car a))

; get the rest of a list
(println (cdr a))

; combination of car+cdr
(println (cadr a))

; combination of cdr+cdr
(println (cddr a))

; needed to exit from the interpreter
(bye)

; finito

