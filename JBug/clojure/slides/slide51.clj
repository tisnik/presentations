
Threading macros
----------------
->

(count (clojure.string/split-lines (slurp "/etc/passwd")))

; is equal to

(-> "/etc/passwd" slurp clojure.string/split-lines count)

->>

(->> (range) (take 20) (filter #(zero? (mod % 3))))

