
GUI: Clojure Seesaw
-------------------
(ns seesaw1.core (:gen-class))
 
(use 'seesaw.core)
 
(defn -main
    [& args]
    (let [main-frame (frame :title "Hello world!")
          btn        (button :text "Click Me")]
          (config! main-frame :content btn)
          (pack!   main-frame)
          (show!   main-frame)))
