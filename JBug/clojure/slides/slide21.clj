
Recursion vs tail recursion
---------------------------
Factorial - a typical example

    (defn fact
        [n]
        (if (<= n 1)
            1
            (* n (fact (- n 1)))))

    (fact 100M)

    (fact 10000M)

         StackOverflowError :)

Very deep recursion might cause stack overflow
    ''recur'' special form

    (defn fact
        ([n]
         (fact n 1))
        ([n acc]
         (if (<= n 1)
             acc
             (recur (dec n) (* acc n)))))

    It is not possible to use ''recur'' everywhere
        so called "tail position"
