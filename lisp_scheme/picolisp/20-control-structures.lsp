;
; PicoLisp
;
; Demonstration example #20:
; Control structures
;
; Author: Pavel Tisnovsky
;

(de gcd
    [x y]
    (if (= x y) x
                (if (> x y)
                    (gcd (- x y) y)
                    (gcd x (- y x)))))

(setq a 20)
(setq b 10)
(if (=0 (- a a 10))
    (prog
         (println "zero result")
         0))

(setq a 20)
(setq b 10)
(when (=0 (- a a 10))
      (println "zero result")
      0)

(unless (=0 (- 1 1))
      (println "zero result")
      0)

(de sgn [n]
    (cond
        ((< n 0)        'negative)
        ((> n 0)        'positive)
        ((=0 n)         'zero)))

(de gcd2
    [x y]
    (if2 (= x y) (> x y)
         NIL
         x
         (gcd (- x y) y)
         (gcd x (- y x))))

; needed to exit from the interpreter
(bye)

; finito

