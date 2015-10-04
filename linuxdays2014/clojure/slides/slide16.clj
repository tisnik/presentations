
Poněkud složitější projekt
--------------------------
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
