;
; PicoLisp
;
; Demonstration example #5:
; list can be used as a queue
;
; Author: Pavel Tisnovsky
;

; push items into the queue
(queue 'my-queue 1)
(queue 'my-queue 2)
(queue 'my-queue 3)

(println my-queue)

; pop one item
(println (pop 'my-queue))
(println my-queue)

; pop one item
(println (pop 'my-queue))
(println my-queue)

; pop one item
(println (pop 'my-queue))
(println my-queue)

; pop one item
(println (pop 'my-queue))
(println my-queue)

; needed to exit from the interpreter
(bye)

; finito

