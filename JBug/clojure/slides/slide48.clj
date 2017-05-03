
Validators
----------

(def x (ref 42))

(set-validator! x (fn [val] (even? val)))

(dosync (ref-set x 10))

(dosync (alter x + 10))

(dosync (alter x + 1))

; check is not performed DURING transaction
(dosync (alter x + 1) (alter x + 1))
