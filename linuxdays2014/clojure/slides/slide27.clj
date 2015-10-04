
Clojure a SQL
-------------
(import 'java.sql.Connection)
(import 'java.sql.DriverManager)
(import 'java.sql.ResultSet)
;
(def connection-string "jdbc:mysql://localhost/test")
;
(def select-statement  "select id, name, surname from users")
;
(defn load-mysql-driver
  []
  (Class/forName "com.mysql.jdbc.Driver"))
;
(defn get-connection
  [user-name password]
  (DriverManager/getConnection "jdbc:mysql://localhost/test" user-name password))
;
(defn close-connection
  [connection]
  (.close connection))
;
(defn run
  []
  (let [connection (get-connection "tester" "quess-it :-)")
        statement  (.prepareStatement connection select-statement)
        result-set (.executeQuery statement)]
    (while (.next result-set)
      (println (str
                 (.getString result-set 1) ", "
                 (.getString result-set 2) ", "
                 (.getString result-set 3))))
    (close-connection connection)))
;
