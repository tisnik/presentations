(ns json2edn.core)

(require '[clojure.data.json :as json])
(require '[clojure.edn :as edn])


(defn json->edn
  "Convert JSON format into EDN format."
  [json-file-name edn-file-name]
  (let [payload (-> json-file-name slurp (json/read-str :key-fn keyword))
        fout    (clojure.java.io/writer edn-file-name)]
    (clojure.pprint/pprint payload)
    (clojure.pprint/pprint payload fout)))


(defn -main
  [& args]
  (json->edn "sqs_messages_response.json" "sqs_messages_response.edn"))
