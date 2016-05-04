;
; PicoLisp
;
; Demonstration example #4:
; list can be used as a stack
;
; Author: Pavel Tisnovsky
;

; push items into the stack
(push 'my-stack 1)
(push 'my-stack 2)
(push 'my-stack 3)

(println my-stack)

; pop one item
(println (pop 'my-stack))
(println my-stack)

; pop one item
(println (pop 'my-stack))
(println my-stack)

; pop one item
(println (pop 'my-stack))
(println my-stack)

; pop one item
(println (pop 'my-stack))
(println my-stack)

; needed to exit from the interpreter
(bye)

; finito

