;
; PicoLisp
;
; Demonstration example #14:
; Boolean operations
;
; Author: Pavel Tisnovsky
;

(println "and")
(println (and NIL NIL))
(println (and T NIL))
(println (and NIL T))
(println (and T T))
(prinl)

(println "or")
(println (or NIL NIL))
(println (or T NIL))
(println (or NIL T))
(println (or T T))
(prinl)

(println "not")
(println (not NIL NIL))
(println (not T NIL))
(println (not NIL T))
(println (not T T))
(prinl)

(println "nand")
(println (nand NIL NIL))
(println (nand T NIL))
(println (nand NIL T))
(println (nand T T))
(prinl)

(println "nor")
(println (nor NIL NIL))
(println (nor T NIL))
(println (nor NIL T))
(println (nor T T))
(prinl)

(println "xor")
(println (xor NIL NIL))
(println (xor T NIL))
(println (xor NIL T))
(println (xor T T))
(prinl)

; needed to exit from the interpreter
(bye)

; finito

