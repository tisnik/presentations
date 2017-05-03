
Expectations
------------
(defproject expectations-demo "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.6.0"]
                 [expectations "2.0.9"]]
  :main ^:skip-aot expectations-demo.core
  :target-path "target/%s"
  :plugins [[lein-expectations "0.0.8"]]
  :profiles {:uberjar {:aot :all}})
 
(expect 42 (* 6 7))
(expect "Hello world" (str "Hello" " " "world"))
(expect 2/3 (/ 2 3))
(expect ArithmeticException (/ 1 0))
