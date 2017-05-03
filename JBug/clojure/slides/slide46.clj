
Watchers
--------

(defn on-change
    [key identity old-val new-val]
    (println (str "Old value: " old-val))
    (println (str "New value: " new-val)))

(def x (ref 42))

(add-watch x "watch-1" on-change)

(dosync (alter x + 1))

(dosync (alter x + 1) (alter x - 1 ))

