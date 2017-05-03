
Future+promise dataflow
-----------------------

(defn fact[n] (apply * (range 1M n)))

(def x (promise))
(def y (promise))
(def z (promise))

(def task-1
    (future
        (deliver z (+ @x @y))))

(def task-2
    (future
        (deliver x (fact 10))))

(def task-3
    (future
        (deliver y (fact 100))))

; now all three calculations are running
; first one needs to wait for other two
@task-1
