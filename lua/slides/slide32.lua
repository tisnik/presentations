---------------------------
-- Návratové hodnoty funkcí
---------------------------

-- funkce vracejici dve hodnoty: vysledek celociselneho
-- deleni a zbytek po celociselnem deleni
function divMod(x,y)
    return math.floor(x / y), x % y
end

print("n", "10/n", "zbytek")
for n = 1, 10 do
    x, y = divMod(10, n)
    print(n, x, y)
end

