;
; PicoLisp
;
; Demonstration example #15:
; Comparisons
;
; Author: Pavel Tisnovsky
;

(println "=T")
(println (=T NIL))
(println (=T T))
(println (=T 42))
(println (=T "string"))
(prinl)

(println "nT")
(println (nT NIL))
(println (nT T))
(println (nT 42))
(println (nT "string"))
(prinl)

(println "=0")
(println (=0 NIL))
(println (=0 T))
(println (=0 42))
(println (=0 "string"))
(prinl)

(println "=1")
(println (=1 NIL))
(println (=1 T))
(println (=1 42))
(println (=1 "string"))
(prinl)

(println "n0")
(println (n0 NIL))
(println (n0 T))
(println (n0 42))
(println (n0 "string"))
(prinl)

; needed to exit from the interpreter
(bye)

; finito

