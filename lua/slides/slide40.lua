--------------
-- Uzávěry (2)
--------------

-- Funkce obsahujici lokalni promennou.
-- Tato funkce vraci anonymni funkci
-- jako svuj vysledek.
function generateClosure()
    -- lokalni promenna, ktera neni
    -- z okolniho programu dostupna
    local y = 1
    -- anonymni funkce vytiskne hodnotu
    -- lokalni promenne funkce "generateClosure"
    -- a potom se pokusi o zmenu jeji hodnoty:
    local result = function()
        print(y)
        y = y + 1
    end
    -- po vytvoreni zarodku uzaveru
    -- zmenime hodnotu lokalni promenne
    y = 42
    -- vratime vytvorenou funkci - uzaver
    return result
end

-- ziskame uzaver, tj. instanci anonymni funkce
closure = generateClosure()

-- vytiskne se posloupnost hodnot 42, 43, 44 a 45
closure()
closure()
closure()
closure()

