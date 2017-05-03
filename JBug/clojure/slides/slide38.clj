
Atoms
-----

(def x (atom 42))

(deref x)

@x

(reset! x 10)

@x

(swap! x + 1)

@x

