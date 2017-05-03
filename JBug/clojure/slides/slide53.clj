
Java interop
------------

(new String)
(new String "Hello world")

(. Integer valueOf "42")
(. Float MAX_VALUE)

(def my-string "Hello world")
(. my-string length)

(def rect (new java.awt.Rectangle))

rect

(set! (. rect width) 320)
(set! (. rect height) 200)
rect

