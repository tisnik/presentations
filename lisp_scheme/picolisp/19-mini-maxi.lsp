;
; PicoLisp
;
; Demonstration example #19:
; Maxi, mini, sum and cnt
;
; Author: Pavel Tisnovsky
;

(println (mini hash (range 1 1000)))

(println (maxi hash (range 1 1000)))

(de sqr [n] (* n n))
(println (sum sqr (range 1 10)))

(de dividable [x y] (=0 (% x y)))
(println (cnt (quote [n] (dividable 100 n)) (range 1 100)))

; needed to exit from the interpreter
(bye)

; finito

