-----------------------------
-- Volitelné parametry funkcí
-----------------------------

function fce(x, y, z)
    print(x, y, z)
end

-- volani funkce fce s ruznym poctem parametru
fce(1, 2, 3)
fce(1, 2, 3, 4) -- posledni hodnota se nevyuzije
fce()
fce(42)
fce(42, 6502)
fce(nil, 6502)

-- lze pouzit i retezce popr. hodnoty dalsich typu typu
fce("Hello", "world", "!")
fce("Hello" .. " world", "!" )
fce("Hello" .. " world" .. "!" )

