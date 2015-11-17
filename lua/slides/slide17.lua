---------------------------
-- Programové smyčky: while
---------------------------

while podmínka do
    programový blok vykonaný při splnění první podmínky
end

-- vypocet Fibonacciho posloupnosti az do mezni hodnoty
n = 1000
a, b = 1, 1
while a <= n do
    print(a)
    a, b = b, a+b
end

