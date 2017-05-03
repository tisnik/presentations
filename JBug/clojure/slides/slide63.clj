
Project file
------------
(defproject ringapp1 "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.6.0"]
                 [ring/ring-core "1.3.2"]
                 [ring/ring-jetty-adapter "1.3.2"]
                 [hiccup "1.0.4"]
                 [org.clojure/tools.cli "0.3.1"]]
  :dev-dependencies [[lein-ring "0.8.10"]]
  :plugins [[lein-ring "0.8.10"]]
  :main ^:skip-aot ringapp1.core
  :target-path "target/%s"
  :ring     {:handler ringapp1.core/app}
  :profiles {:uberjar {:aot :all}})
