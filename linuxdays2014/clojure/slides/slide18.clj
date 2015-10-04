
JSON
----
(defn render-json-data
    "Render JSON data to be send back to the client (browser)."
    [output-data]
    (json/write-str output-data))
;
(defn read-job-info-as-json
    "Fetch the timestamp and duration of the last build from Jenkins server."
    [job-name]
    (let [full-json-url (str json-url "job/" (.replace job-name " " "%20") "/lastBuild/api/json?pretty=true")
          inputstr (slurp full-json-url)]
        (if inputstr
            (let [parsed   (json/read-str inputstr)]
                [(get parsed "timestamp") (get parsed "duration")]))))
