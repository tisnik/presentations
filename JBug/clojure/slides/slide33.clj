
Lazy sequences
--------------

(map inc [1 2 3 4])

(map inc (range 1 9))

(map * [1 2 3 4] [5 6 7 8])

(def lazy (range))

(def lazy2 (map inc lazy))

(nth lazy2 10)

(take 10 lazy2)

(defn end-of? [x] (<= x 42))

(take-while end-of? (range 1 100 3))

(filter (fn [x] (< x 10)) (range 0 1000))

