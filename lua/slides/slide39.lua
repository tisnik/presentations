----------
-- Uzávěry
----------

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
    return function()
        print(y)
        y = y + 1
    end
end

-- ziskame uzaver, tj. instanci anonymni funkce
closure1 = generateClosure()

-- jake hodnoty se vytisknou?
closure1()
closure1()
closure1()
closure1()

