;
; PicoLisp
;
; Demonstration example #18:
; Filter function
;
; Author: Pavel Tisnovsky
;

(de pos?
    [n]
    (> n 0))

(println (filter pos? (-5 -4 -3 -2 -1 0 1 2 3 4 5)))

(println (filter (quote (n) (=0 (% n 2))) (range 1 10)))

; needed to exit from the interpreter
(bye)

; finito

