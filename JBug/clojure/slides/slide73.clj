
Unit tests...
-------------
(ns factorial.core-test
  (:require [clojure.test :refer :all]
            [factorial.core :refer :all]))
 
(deftest factorial-test
    (testing "Factorial"
        (is ( = (factorial 0)   1) "beginning")
        (is ( = (factorial 1)   1) "beginning")
        (is ( = (factorial 2)   (* 1 2)) "still easy")
        (is ( = (factorial 5)   (* 1 2 3 4 5)) "5!")
        (is ( = (factorial 6)   720) "6!")))
 
(deftest negative-factorial-test
    (testing "Negative tests"
        (is ( = (factorial 0)   0) "negative test case #1")
        (is ( = (factorial 1)   0) "negative test case #2")
        (is ( = (factorial 2)   0) "negative test case #3")))
 
(deftest exception-test
    (testing "If factorial throws exception"
        (is (thrown? IllegalArgumentException (factorial -1)))
        (is (thrown? IllegalArgumentException (factorial -2)))
        (is (thrown? IllegalArgumentException (factorial -100)))))
 
(deftest negative-exception-test
    (testing "(negative test) If factorial throws exception"
        (is (thrown? IllegalArgumentException (factorial 1)))
        (is (thrown? IllegalArgumentException (factorial 2)))
        (is (thrown? IllegalArgumentException (factorial 3)))))
