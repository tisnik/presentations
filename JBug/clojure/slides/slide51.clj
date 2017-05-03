
Threading macros
----------------
->

(-> "/etc/passwd" slurp clojure.string/split-lines count)

->>

(->> (range) (take 20) (filter #(zero? (mod % 3))))

