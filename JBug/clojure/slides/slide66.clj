
Sessions
--------
(ns servertest3.core)
;
(require '[ring.adapter.jetty      :as jetty])
(require '[ring.middleware.params  :as http-params])
(require '[ring.middleware.session :as http-session])
(require '[ring.util.response      :as http-response])
;
(require '[hiccup.page :as page])
;
(defn render-page
    [counter]
    (page/xhtml
        [:head
            [:title "Hello world!"]
            [:meta {:name "Author"    :content "Pavel Tisnovsky"}]
            [:meta {:name "Generator" :content "Clojure"}]
            [:meta {:http-equiv "Content-type" :content "text/html; charset=utf-8"}]
        ]
        [:body
            [:h1 "Hello world!"]
            [:div "Counter: " counter]]))
;
(defn generate-response
    [page-content session]
    (-> (http-response/response page-content)
        (http-response/content-type "text/html")
        (assoc :session session)))
;
(defn index-page-handler
    [session]
    (let [counter (get session :counter 0)
          session (assoc session :counter (inc counter))]
          (generate-response (render-page counter) session)))
;
(defn handle-request
    [request]
    (let [params   (request :params)
          session  (request :session)]
          (index-page-handler session)))
;
(defn handler
    [request]
    (handle-request request))
;
(def app
    (-> handler
        http-session/wrap-session ; we need to work with HTTP sessions
        http-params/wrap-params)) ; and to process request parameters, of course
;
(defn start-server
    [port]
    (println "Starting the server at the port: " port)
    (jetty/run-jetty app {:port port}))
;
(defn -main
    [& args]
    (start-server 8080))
;
