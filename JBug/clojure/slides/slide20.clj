
Multiarity functions
--------------------

(defn multiply
   ([x]
    (* x x))
   ([x y]
    (* x y))
   ([x y z]
    (* x y z)))

(multiply 2)
(multiply 6 7)
(multiply 2 3 7)
