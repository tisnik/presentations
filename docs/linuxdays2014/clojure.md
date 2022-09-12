# Clojure prakticky

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz`
* Datum: 2014-10-05
* Prezentace:
    - [https://tisnik.github.io/presentations/linuxdays2014/clojure.html](https://tisnik.github.io/presentations/linuxdays2014/clojure.html)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/linuxdays2014/clojure/clojure.txt](https://github.com/tisnik/presentations/blob/master/linuxdays2014/clojure/clojure.txt)



## Základní informace o Clojure (1)

* Clojure = Java + Closure
    - Rich Hickey
    - Založeno na Lispu/Scheme
    - Teorie λ-kalkulu

## Základní informace o Clojure (2)

* Multiparadigmatický programovací jazyk
    - Přednost má funkcionální přístup
    - Ovšem není striktně vyžadován
* Podporuje tvorbu masivně paralelních
  vícevláknových aplikaci
    - Agenti
    - Transakce - STM
    - Neměnné datové typy
    -> eliminace vzniku deadlocků
    -> žádný GIL
* REPL
* Code=Data

## Runtime jazyka Clojure + knihovny

* Podpora běhu na více virtuálních strojích
    - JVM
        - překlad od the Fly
    - .NET
    - JavaScript
        - Resp. libovolná VM JavaScriptu
* Nejedná se o náhradu Javy, C# ani JavaScriptu
    - Kooperace s těmito jazyky
    - A především jejich knihovnami
    -> Clojure se nesnaží znovuobjevit kolo
    -> velmi snadný přechod na Clojure pro Java vývojáře

## Základní vlastnosti Clojure

* Čtyři referenční typy namísto proměnných
    - synchronní/asynchronní operace
    - atomické operace
    - transakce
    - validace
    - sledování (watch)

## Clojure a líné vyhodnocování

* Clojure vyznává stejnou filozofii jako /me
    - Práce (výpočet) se provede až ve chvíli
      kdy je to skutečně zapotřebí (nebo. nikdy)
    - Lazy sequences
      (range 0 100000)
    - Výsledky mnoha výpočtů nemusí být dostupné ihned
    -> proč nevyužít další vlákna běžící v pozadí?

## Clojure jako jazyk odvozený od LISPu/Scheme

```clojure
; výpis na standardní výstup (side effect)
(println "Hello" "world")
; volání funkce +
(+ 1 2 3 4)
; vnořené funkce
(* (+ 1 2 3) (+ 3 4))
; prázdný seznam je rozdílný od nil
'()
()
; vektory jsou vyhodnoceny samy na sebe (na rozdíl od seznamů)
[1 2 3 4]
```

## Kolekce

* Neměnné/immutable
    - Seznam
        * `first`, `rest`, `count`
    - Vektor
        * velmi důležitá a užitečná datová struktura
        * založen na RRB-Stromech
          (Relaxed Radix Balanced Trees)
        * zabere méně paměti než seznamy
        * rychlý přístup k prvkům O(log₃₂N)
    - Mapa
        * základ formátu .edn
        * Extensible Data Notation
    - Množina

## Funkce pro práci s kolekcemi

```
(count)
(empty)
(cons)
(conj)
(pop)  ; rozdílné chování pro seznamy/vektory
(peek) ; rozdílné chování pro seznamy/vektory
(nth)
(first)
(rest)
```

## Časová složitost vybraných operací

```
# Funkce Seznam Vektor
1 count  O(1)   O(1)
2 nth    O(N)   O(log₃₂N)
3 pop    O(1)   O(log₃₂N)
4 peek   O(1)   O(log₃₂N)
5 first  O(1)   O(1)
6 last   O(N)   O(N)
```

## Clojure v praxi

* REPL
* IDE
* Web server, generovani HTML, SQL, ...

## REPL

* Read Eval Print Loop
* Naprostý základ při tvorbě a především ladění aplikací
* Přímé spuštění REPL
    - `java -cp .:clojure-1.5.1.jar clojure.main`
* Existují i lepší možnosti!
    - `lein repl`

## REPL ve Screenu

* Spuštění
    - `screen -S clojure bash -c 'java -cp .:clojure-1.5.1.jar clojure.main'`
* Výhody
    - lze ovládat i z jiného programu
    - základ - poslání textu do screenu tak, jakoby byl zapsán na klávesnici
* Příklady
    - `screen -S clojure -p 0 -X stuff "(+ 1 2)\\n"`
    - `screen -S clojure -p 0 -X stuff "(range 1 10)\\n"`
    - `screen -S clojure -p 0 -X stuff "(defn add [x y] (+ x y))\n"`
    - `screen -S clojure -p 0 -X stuff "(add 1 2)\n"`
* Použito v pluginu Slime for Vim

## IDE

* Slime for Vim
* Cider (Emacs)
* Counterclockwise (Eclipse)

## Leiningen

* "Maven pro Clojure"
* Tvorba projektů
* Jediný skript, který nainstaluje vše potřebné
* Unit testing
* Řešení závislostí
* Spuštění různých typů aplikací
    - Webové atd.
* Vylepšený REPL
* Podpora pluginů

## Ukázka souboru project.clj

```clojure
(defproject Test2 "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [hiccup "1.0.4"]]
  :main test.core)
```

## Poněkud složitější projekt

```clojure
(defproject smearch "0.1.0-SNAPSHOT"
  :description "The ultimate application"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [org.clojure/java.jdbc "0.3.3"]
                 [ring/ring-core "1.2.2"]
                 [ring/ring-jetty-adapter "1.2.2"]
                 [hiccup "1.0.4"]
                 [org.clojure/tools.cli "0.3.1"]]
  :resource-paths ["resources/teiid-8.6.0.Final-jdbc.jar"]
  :dev-dependencies [[lein-ring "0.8.10"]]
  :plugins [[lein-ring "0.8.10"]]
  :ring {:handler smearch.core/app}
  :main smearch.core)
```

## Leiningen a REPL

* Základní tvar
    - `lein repl`
* Leiningen REPL + Screen
    - `screen -S clojure`
    - `lein repl`

## JSON

```clojure
(defn render-json-data
    "Render JSON data to be send back to the client (browser)."
    [output-data]
    (json/write-str output-data))

(defn read-job-info-as-json
    "Fetch the timestamp and duration of the last build from Jenkins server."
    [job-name]
    (let [full-json-url (str json-url "job/" (.replace job-name " " "%20") "/lastBuild/api/json?pretty=true")
          inputstr (slurp full-json-url)]
        (if inputstr
            (let [parsed   (json/read-str inputstr)]
                [(get parsed "timestamp") (get parsed "duration")]))))
```

## XML

```clojure
(require '[clojure.xml :as xml])

(defn read-and-parse-xml
    [filename]
    (xml-seq (xml/parse filename)))

(defn find-node
    [xmlstructure tag]
    (for [x xmlstructure :when (= tag (:tag x))] x))

(read-and-parse-xml "monitors.xml")

({:tag :monitors, :attrs {:version "1"}, :content [{:tag :configuration, :attrs
nil, :content [{:tag :clone, :attrs nil, :content ["no"]} {:tag :output, :attrs
{:name "HDMI-1"}, :content nil} {:tag :output, :attrs {:name "HDMI-2"},
:content nil} {:tag :output, :attrs {:name "VGA"}, :content [{:tag :vendor,
:attrs nil, :content ["SAM"]} {:tag :product, :attrs nil, :content ["0x010c"]}
{:tag :serial, :attrs nil, :content ["0x4d4a3137"]} {:tag :width, :attrs nil,
:content ["1280"]} {:tag :height, :attrs nil, :content ["1024"]} {:tag :rate,
:attrs nil, :content ["60"]} {:tag :x, :attrs nil, :content ["1680"]} {:tag :y,
:attrs nil, :content ["0"]} {:tag :rotation, :attrs nil, :content ["normal"]}
{:tag :reflect_x, :attrs nil, :content ["no"]} {:tag :reflect_y, :attrs nil,
:content ["no"]}]} {:tag :output, :attrs

(def xml (read-and-parse-xml "monitors.xml"))

(println :content (first xml))
```

## Hiccup

```clojure
(require '[hiccup.core :as hiccup])
(require '[hiccup.page :as page])
(require '[hiccup.form :as form])

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
```

## Hiccup

```clojure
(ns test.core)

(require '[hiccup.page :as page])

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

(defn -main
    "Entry point"
    [& args]
    (spit "test.html" (render-html-page)))
```

## Hiccup

```clojure
(ns test.core)

(require '[hiccup.page :as page])

(defn factorial
    ([n]
        (factorial n 1N))  ; dulezite -> donutime pouziti BigInteger
                           ; (uz zadne IntegerOverflow :)
    ([n acc]
        (if  (= n 0)  acc
            (recur (dec n) (* acc n)))))

(defn render-factorials
    [max-n]
    (for [n (range 0 (inc max-n))]
        [:tr [:td n] [:td (factorial n)]]))

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

(defn -main
    "Entry point"
    [& args]
    (spit "test.html" (render-html-page)))
```

## Clojure Ring

```clojure
(defproject servertest "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [ring/ring-core "1.2.2"]
                 [ring/ring-jetty-adapter "1.2.2"]
                 [hiccup "1.0.4"]
                 [org.clojure/tools.cli "0.3.1"]]
  :dev-dependencies [[lein-ring "0.8.10"]]
  :plugins [[lein-ring "0.8.10"]]
  :ring {:handler servertest.core/app}
  :main servertest.core)
```

## Clojure Ring

```clojure
(ns servertest.core)

(require '[ring.adapter.jetty      :as jetty])
(require '[ring.middleware.params  :as http-params])
(require '[ring.util.response      :as http-response])

(require '[hiccup.page :as page])

(defn render-page
    []
    (page/xhtml
        [:head
            [:title "Hello world!"]
            [:meta {:name "Author"    :content "Pavel Tisnovsky"}]
            [:meta {:name "Generator" :content "Clojure"}]
            [:meta {:http-equiv "Content-type" :content "text/html; charset=utf-8"}]
        ]
        [:body
            [:h1 "Hello world!"]]))

(defn generate-response
    [page-content]
    (-> (http-response/response page-content)
        (http-response/content-type "text/html")))

(defn handle-request
    [request]
    (generate-response (render-page)))

(defn handler
    [request]
    (handle-request request))

(def app
    (-> handler
        http-params/wrap-params))

(defn start-server
    [port]
    (println "Starting the server at the port: " port)
    (jetty/run-jetty app {:port port}))

(defn -main
    [& args]
    (start-server 8080))
```

## Zpracování požadavku (requestu)

```clojure
(ns servertest2.core)

(require '[ring.adapter.jetty      :as jetty])
(require '[ring.middleware.params  :as http-params])
(require '[ring.util.response      :as http-response])

(require '[hiccup.page :as page])

(defn render-page
    []
    (page/xhtml
        [:head
            [:title "Hello world!"]
            [:meta {:name "Author"    :content "Pavel Tisnovsky"}]
            [:meta {:name "Generator" :content "Clojure"}]
            [:meta {:http-equiv "Content-type" :content "text/html; charset=utf-8"}]
        ]
        [:body
            [:h1 "Hello world!"]]))

(defn generate-response
    [page-content]
    (-> (http-response/response page-content)
        (http-response/content-type "text/html")))

(defn print-request-info
    [request]
    (println "time:        " (.toString (new java.util.Date)))
    (println "addr:        " (request :remote-addr))
    (println "params:      " (request :params))
    (println "user-agent:  " ((request :headers) "user-agent"))
    (println ""))

(defn handle-request
    [request]
    (println "request URI: " (request :uri))
    (print-request-info request)
    (generate-response (render-page)))

(defn handler
    [request]
    (handle-request request))

(def app
    (-> handler
        http-params/wrap-params))

(defn start-server
    [port]
    (println "Starting the server at the port: " port)
    (jetty/run-jetty app {:port port}))

(defn -main
    [& args]
    (start-server 8080))
```

## Sezení (sessions)

```clojure
(ns servertest3.core)

(require '[ring.adapter.jetty      :as jetty])
(require '[ring.middleware.params  :as http-params])
(require '[ring.middleware.session :as http-session])
(require '[ring.util.response      :as http-response])

(require '[hiccup.page :as page])

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

(defn generate-response
    [page-content session]
    (-> (http-response/response page-content)
        (http-response/content-type "text/html")
        (assoc :session session)))

(defn index-page-handler
    [session]
    (let [counter (get session :counter 0)
          session (assoc session :counter (inc counter))]
          (generate-response (render-page counter) session)))

(defn handle-request
    [request]
    (let [params   (request :params)
          session  (request :session)]
          (index-page-handler session)))

(defn handler
    [request]
    (handle-request request))

(def app
    (-> handler
        http-session/wrap-session ; we need to work with HTTP sessions
        http-params/wrap-params)) ; and to process request parameters, of course

(defn start-server
    [port]
    (println "Starting the server at the port: " port)
    (jetty/run-jetty app {:port port}))

(defn -main
    [& args]
    (start-server 8080))
```


## Clojure a SQL

```clojure
(import 'java.sql.Connection)
(import 'java.sql.DriverManager)
(import 'java.sql.ResultSet)

(def connection-string "jdbc:mysql://localhost/test")

(def select-statement  "select id, name, surname from users")

(defn load-mysql-driver
  []
  (Class/forName "com.mysql.jdbc.Driver"))

(defn get-connection
  [user-name password]
  (DriverManager/getConnection "jdbc:mysql://localhost/test" user-name password))

(defn close-connection
  [connection]
  (.close connection))

(defn run
  []
  (let [connection (get-connection "tester" "quess-it :-)")
        statement  (.prepareStatement connection select-statement)
        result-set (.executeQuery statement)]
    (while (.next result-set)
      (println (str
                 (.getString result-set 1) ", "
                 (.getString result-set 2) ", "
                 (.getString result-set 3))))
    (close-connection connection)))
```


## Clojure a SQL

```clojure
(ns test
  (:require [clojure.java.jdbc :as jdbc]))

(def db-spec {:classname   "com.mysql.jdbc.Driver" ; must be on classpath
              :subprotocol "jdbc:mysql://localhost/test"
              :subname     "1234"
              :user        "tester"
              :password    "quess-it :-)"})

(def select-statement
   (str "select id, name, surname from users"))

(defn run
  []
  (doseq [rs (jdbc/query db-spec [select-statement])]
    (println (str
      (rs :id) ", "
      (rs :name) ", "
      (rs :surname)))))
```
 
