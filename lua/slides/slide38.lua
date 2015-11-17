--------------------------------------
-- Funkce jako plnohodnotný datový typ
--------------------------------------

-- pomocna funkce, ktera vytiskne tabulku hodnot
-- pro uhly lezici mezi 0 az 90 stupni
-- na zaklade predane funkce
function printTable(func)
    -- tisk adresy funkce v adresnim prostoru VM
    print(func)
    -- tisk uhlu mezi 0 az 90 stupni
    -- a hodnot uzivatelske funkce pro tyto uhly
    -- (je nastaven krok po peti stupnich)
    for i=0, 90, 5 do
        -- prevod stupnu na radiany
        local alfa = math.pi * i / 180.0
        -- volani funkce predane jako parametr
        local y = func(alfa)
        print(string.format("%d\t%6.4f", i, y))
    end
end

-- uzivatelsky definovana funkce ulozena
-- do promenne "fce"
fce = function(x)
    return math.sin(x)
end

-- tisk tabulky
print("fce = function(x) return math.sin(x) end")
printTable(fce)

-- muzeme primo pouzit i knihovni funkci
-- se stejnym vyznamem
print("fce = math.sin")
printTable(math.sin)

