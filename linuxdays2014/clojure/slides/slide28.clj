
Clojure a SQL
-------------
(ns test
  (:require [clojure.java.jdbc :as jdbc]))
;
(def db-spec {:classname   "com.mysql.jdbc.Driver" ; must be on classpath
              :subprotocol "jdbc:mysql://localhost/test"
              :subname     "1234"
              :user        "tester"
              :password    "quess-it :-)"})
;
(def select-statement
   (str "select id, name, surname from users"))
;
(defn run
  []
  (doseq [rs (jdbc/query db-spec [select-statement])]
    (println (str
      (rs :id) ", "
      (rs :name) ", "
      (rs :surname)))))
  
