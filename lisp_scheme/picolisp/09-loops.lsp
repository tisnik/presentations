;
; PicoLisp
;
; Demonstration example #9:
; Program loops (this example needs used interaction)
;
; Author: Pavel Tisnovsky
;

; simplest loop
(for n 10 (println n)) 

; user have to provide numbers on standard input
(while (num? (read)) (println 'cislo))

; user have to provide numbers on standard input
(until (=T (setq N (read)))
    (println 'vysledek (* N N)))

; needed to exit from the interpreter
(bye)

; finito

