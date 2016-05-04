;
; PicoLisp
;
; Demonstration example #23
; try-catch-finally in PicoLisp
;
; Author: Pavel Tisnovsky
;

(de factorial
    [n]
    (if (< n 0)
        (throw 'negative)
        (apply * (range 1 n))))

(catch 'negative
    (finally (println "end...")
    (for n 10 (println (factorial (- 5 n))))))

; needed to exit from the interpreter
(bye)

; finito

