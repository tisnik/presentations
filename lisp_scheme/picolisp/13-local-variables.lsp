;
; PicoLisp
;
; Demonstration example #13:
; Usage of local variables
;
; Author: Pavel Tisnovsky
;

(let x 10 (println (* x 2)))

(let (x 6 y 7) (println (* x y)))

(de average
    [values]
    (let [sum   (apply + values)
          count (length values)]
          (/ sum count)))

(de average2
    [values]
    (let [sum   (apply + values)
          count (length values)]
          (let [result (/ sum count)]
                result)))

(de average3
    [values]
    (let [sum    (apply + values)
          count  (length values)
          result (/ sum count)]
                result))

(println "Average1")
(println (average (1 2 3)))
(println (average (1 1 1)))
(println (average (1 1 10)))

(println "Average2")
(println (average2 (1 2 3)))
(println (average2 (1 1 1)))
(println (average2 (1 1 10)))

(println "Average3")
(println (average3 (1 2 3)))
(println (average3 (1 1 1)))
(println (average3 (1 1 10)))

; needed to exit from the interpreter
(bye)

; finito

