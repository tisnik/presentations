(ns xml2edn.core)

(use '[clojure.xml])


(defn xml->edn
  "Convert XML file into EDN format."
  [xml-file-name edn-file-name]
  (let [payload (clojure.xml/parse "nested.xml")
        fout    (clojure.java.io/writer edn-file-name)]
    (clojure.pprint/pprint payload fout)))


(defn -main
  [& args]
  (xml->edn "nested.xml" "nested.edn"))
