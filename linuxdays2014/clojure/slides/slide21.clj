
Hiccup
------
(ns test.core)
;
(require '[hiccup.page :as page])
;
(defn render-html-page
    []
    (page/xhtml
        [:head
            [:title "Hello world page"]
            [:meta {:name "Author"    :content "Pavel Tisnovsky"}]
            [:meta {:name "Generator" :content "Clojure/hiccup"}]
            [:meta {:http-equiv "Content-type" :content "text/html; charset=utf-8"}]
            (page/include-css "style.css")
            (page/include-js  "scripts.js")
        ]
        [:body
            [:h1 "Hello world"]
        ]
    )
)
;
(defn -main
    "Entry point"
    [& args]
    (spit "test.html" (render-html-page)))
