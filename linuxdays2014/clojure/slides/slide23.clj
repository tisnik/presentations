
Clojure Ring
------------
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
