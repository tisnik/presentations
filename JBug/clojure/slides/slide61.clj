
Hiccup
------
(require '[hiccup.core :as hiccup])
(require '[hiccup.page :as page])
(require '[hiccup.form :as form])
;
(defn render-html-header
    []
    [:head
        [:title "Ultimate tool"]
        [:meta {:name "Author"    :content "Pavel Tisnovsky"}]
        [:meta {:name "Generator" :content "Clojure"}]
        [:meta {:http-equiv "Content-type" :content "text/html; charset=utf-8"}]
        (page/include-css "bootstrap.min.css")
        (page/include-js  "bootstrap.min.js")
    ]
)
;
(defn render-page
    [user-name]
    (page/xhtml
        (render-html-header)
        [:body
            [:div {:class "container"}
            (form/form-to [:get "/" ]
                (form/text-field {:autofocus "autofocus" :size "40"} "user-name" (str user-name))
                (form/submit-button "Search"))
            ] ; </div class="container">
        ] ; </body>
))
