
Testing
-------
(ns factorial.core
  (:gen-class))
 
(defn factorial
    [n]
    (if (neg? n)
        (throw (IllegalArgumentException. "negative numbers are not supported!"))
        (apply * (range 1 (inc n)))))
 
(defn -main
    "I don't do a whole lot ... yet."
    [& args]
    (doseq [i (range 0 10)]
        (println i "! = " (factorial i))))
