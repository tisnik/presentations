(ns properties2edn.core)


(defn properties->map
  "Convert properties entries into a map. Keys are converted into proper keywords."
  [properties]
  (into {}
        (for [[k v] properties]
              [(keyword k) v])))


(defn load-properties-file
  "Load configuration from the provided properties file."
  [file-name]
  (with-open [reader (clojure.java.io/reader file-name)]
    (let [properties (java.util.Properties.)]
      (.load properties reader)
      (properties->map properties))))


(defn properties->edn
  "Convert properties file into EDN format."
  [properties-file-name edn-file-name]
  (let [payload (load-properties-file properties-file-name)
        fout    (clojure.java.io/writer edn-file-name)]
    (clojure.pprint/pprint payload fout)))


(defn -main
  [& args]
  (properties->edn "test.properties" "test.edn"))
