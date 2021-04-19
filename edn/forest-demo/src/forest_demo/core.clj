(ns forest-demo.core)

(require '[clojure.xml :as xml])
(require '[tupelo.forest :as tf])


(defn pprint-to-file
  [filename payload]
  (clojure.pprint/pprint payload (clojure.java.io/writer filename)))


(defn -main
  [& args]
  (let [payload        (xml/parse "nested.xml")
        hiccup-format  (tf/enlive->hiccup payload)
        bush-format    (tf/enlive->bush payload)
        tree-format    (tf/enlive->tree payload)]
    (pprint-to-file "nested-enlive.edn" payload)
    (pprint-to-file "nested-hiccup.edn" hiccup-format)
    (pprint-to-file "nested-bush.edn" bush-format)
    (pprint-to-file "nested-tree.edn" tree-format)))
