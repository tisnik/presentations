----------------------------------
-- Programové smyčky: repeat-until
----------------------------------

-- vypocet Fibonacciho posloupnosti az do mezni hodnoty
n = 1000
a, b = 1, 1
repeat
    print(a)
    a, b = b, a+b
until a > n

