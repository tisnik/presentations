
Producer-consumer
-----------------
(defn -main
    [& args]
    (println "Start")
    ; channel with given capacity
    (let [channel (chan (dropping-buffer 10))]
 
        (go
            (loop [result []]
                (<! (timeout 1))
                (let [item (<! channel)] ; if channel is closed, nil is returned
                    (if item             ; not nil is returned instead
                       (recur (conj result item)) ; add item to collection
                       (println result)))))       ; end of sequence
 
        (println "consumer started")
 
        (go
            (doseq [i (range 0 1000)]
                (>! channel i))
            (close! channel)))
 
        (println "producer started")
 
    (wait)
    (println "Finish")
    (System/exit 0))
