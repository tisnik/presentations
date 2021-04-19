(ns edn2json.core)

(require '[clojure.data.json :as json])
(require '[clojure.edn :as edn])


(defn edn->json
  "Convert EDN format into JSON format."
  [edn-file-name json-file-name]
  (let [payload (-> edn-file-name slurp edn/read-string)
        output (with-out-str (json/pprint payload))]
    (spit json-file-name output)))


(defn -main
  [& args]
  (edn->json "details.edn" "details.json"))
