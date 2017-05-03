
Async programming
-----------------
(ns async1.core (:gen-class))
 
(require '[clojure.core.async :refer (go chan >! <!)])
 
(defn wait
    "Pozastaveni hlavniho vlakna - simulace interaktivni prace."
    []
    (Thread/sleep 1000))
 
(defn -main
    [& args]
    (println "Start")
    ; vytvorime kanal
    (let [channel (chan)]
        ; send message to channel (go block will wait for data)
        (go (>! channel "Hello world #1!"))
        (wait)
 
        ; read message from channel
        (go (println (<! channel)))
        (wait)
         
        ; try to read from empty channel (it will wail to new data)
        (go (println (<! channel)))
        (wait)
 
        ; send another message to channel
        (go (>! channel "Hello world #2!"))
        (wait))
 
    (println "Finish"))
