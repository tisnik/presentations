(ns logo (:require [pixie.math :refer :all]
                   [pixie.io :refer :all]))

(def s 480)

(->>
    (str "<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='" s "' height='" s "'>"
    (loop [i 0 R 255 G 255 B 0 o ""]
        (let [r (- 128 i)
              a (/ i 12.)
              b (+ i 80)
              x (+ (/ s 2) (* b (cos a)))
              y (+ (/ s 2) (* b (sin a)))
              c (str R "," G "," B)
              p (str "<circle cx='" x "' cy='" y "' r='" r "' ")
              q (str "fill='rgb(" R "," G "," B ")' style='fill-opacity:.06'/>\n")]
              (if (< i 128)
                  (recur (inc i) (- R 2) G (+ B 2) (str o p q p "fill='none' stroke='black'/>\n"))
                  o)))
         "</svg>")
    (spit "logo.svg"))


