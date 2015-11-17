--------------------------
-- Koprogramy (coroutines)
--------------------------

-- vytvoreni koprogramu, vypis jeho stavu a spusteni
-- (anonymni) funkce koprogramu je vytvorena primo
-- ve volani coroutine.create()

-- vytvoreni koprogramu s vyuzitim anonymni funkce
koprogram = coroutine.create(
    function()
        print("*** Koprogram byl spusten ***")
    end
)

-- vypis typu objektu
print("Typ objektu:", koprogram)

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu:", coroutine.status(koprogram))

-- spusteni koprogramu
coroutine.resume(koprogram)

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu:", coroutine.status(koprogram))

