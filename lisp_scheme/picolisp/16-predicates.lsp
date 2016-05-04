;
; PicoLisp
;
; Demonstration example #16:
; Predicates
;
; Author: Pavel Tisnovsky
;

(println "atom")
(println (atom NIL))
(println (atom T))
(println (atom 42))
(println (atom '(1 2 3)))
(println (atom ""))
(println (atom "unknown"))
(println (atom gcd))
(println (atom average))
(println (atom println))
(println (atom print))
(println (atom car))
(println (atom cdr))
(prinl)

(println "num?")
(println (num? NIL))
(println (num? T))
(println (num? 42))
(println (num? '(1 2 3)))
(println (num? ""))
(println (num? "unknown"))
(println (num? gcd))
(println (num? average))
(println (num? println))
(println (num? print))
(println (num? car))
(println (num? cdr))
(prinl)

(println "fun?")
(println (fun? NIL))
(println (fun? T))
(println (fun? 42))
(println (fun? '(1 2 3)))
(println (fun? ""))
(println (fun? "unknown"))
(println (fun? gcd))
(println (fun? average))
(println (fun? println))
(println (fun? print))
(println (fun? car))
(println (fun? cdr))
(prinl)

(println "flg?")
(println (flg? NIL))
(println (flg? T))
(println (flg? 42))
(println (flg? '(1 2 3)))
(println (flg? ""))
(println (flg? "unknown"))
(println (flg? gcd))
(println (flg? average))
(println (flg? println))
(println (flg? print))
(println (flg? car))
(println (flg? cdr))
(prinl)

(println "bool")
(println (bool NIL))
(println (bool T))
(println (bool 42))
(println (bool '(1 2 3)))
(println (bool ""))
(println (bool "unknown"))
(println (bool gcd))
(println (bool average))
(println (bool println))
(println (bool print))
(println (bool car))
(println (bool cdr))
(prinl)

; needed to exit from the interpreter
(bye)

; finito

