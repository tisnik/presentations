;
; PicoLisp
;
; Demonstration example #6:
; FIFO implemented in circular list
;
; Author: Pavel Tisnovsky
;

; create fifo and add item into it
(fifo 'X 1)
(println X)

(fifo 'X 2 3)
(println X)

(println (fifo 'X))
(println X)

(println (fifo 'X))
(println X)

(println (fifo 'X))
(println X)

(println (fifo 'X))
(println X)

; needed to exit from the interpreter
(bye)

; finito

