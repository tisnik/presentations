
GUI: Clojure Seesaw
-------------------
(ns seesaw9.core (:gen-class))
 
(use 'seesaw.core)
(use 'seesaw.color)
 
(def formular
    (grid-panel :columns 2
                :rows 3
                :items [(button :text ":background :red"
                                :background :red
                                :listen [:action #(println "Button#1\n" %1)])
                        (button :text ":background :yellow"
                                :background :yellow
                                :listen [:action #(println "Button#2\n" %1)])
                        (button :text ":background :orange"
                                :background :orange
                                :listen [:action #(println "Button#3\n" %1)])
                        (button :text ":background #ff8080"
                                :background "#ff8080"
                                :listen [:action #(println "Button#4\n" %1)])
                        (button :text ":background #8080ff"
                                :background "#8080ff"
                                :listen [:action #(println "Button#5\n" %1)])
                        (button :text ":background #8f8"
                                :background "#8f8"
                                :listen [:action #(println "Button#6\n" %1)])
                        ]))
 
(defn -main
    [& args]
    (-> (frame :title "Color test"
               :on-close :exit
               :content formular)
        (pack!)
        (show!)))
