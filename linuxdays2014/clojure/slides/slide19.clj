
XML
---
(require '[clojure.xml :as xml])
;
(defn read-and-parse-xml
    [filename]
    (xml-seq (xml/parse filename)))
;
(defn find-node
    [xmlstructure tag]
    (for [x xmlstructure :when (= tag (:tag x))] x))
;
(read-and-parse-xml "monitors.xml")
;
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
;
(def xml (read-and-parse-xml "monitors.xml"))
;
(println :content (first xml))
