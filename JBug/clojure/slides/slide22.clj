
Memoization
-----------

(defn fact
    [n]
    (apply *
         (range 1M (inc n))))
 
(dotimes [i 10] (time (fact 10000)))

(defn fact2
    [n]
    (memoize
        (fn [n]
            (apply *
                (range 1M (inc n))))))
 
(dotimes [i 10] (time (fact2 10000)))

