
Hiccup
------
(ns test.core)
;
(require '[hiccup.page :as page])
;
(defn factorial
    ([n]
        (factorial n 1N))  ; dulezite -> donutime pouziti BigInteger
                           ; (uz zadne IntegerOverflow :)
    ([n acc]
        (if  (= n 0)  acc
            (recur (dec n) (* acc n)))))
;
(defn render-factorials
    [max-n]
    (for [n (range 0 (inc max-n))]
        [:tr [:td n] [:td (factorial n)]]))
;
(defn render-html-page
    []
    (page/xhtml
        [:head
            [:title "Factorial generator"]
            [:meta {:name "Author"    :content "Pavel Tisnovsky"}]
            [:meta {:name "Generator" :content "Clojure/hiccup"}]
            [:meta {:http-equiv "Content-type" :content "text/html; charset=utf-8"}]
            (page/include-css "style.css")
            (page/include-js  "scripts.js")
        ]
        [:body
            [:h1 "Factorial"]
            [:table
                [:tr [:th "n"] [:th "n!"]]
                (render-factorials 100)
            ]]))
;
(defn -main
    "Entry point"
    [& args]
    (spit "test.html" (render-html-page)))
