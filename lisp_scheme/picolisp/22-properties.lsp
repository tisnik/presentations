;
; PicoLisp
;
; Demonstration example #22
; symbol properties
;
; Author: Pavel Tisnovsky
;

(setq x 42)
(println x)

(put 'x 'description 'answer)
(println x)
(println (get 'x 'description))

(put 'x 'performed-by 'deep-thought)
(println x)
(println (get 'x 'performed-by))

; needed to exit from the interpreter
(bye)

; finito

