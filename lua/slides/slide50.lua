--------------------------
-- Koprogramy (coroutines)
--------------------------

-- funkce, pro kterou bude koprogram vytvoren
function funkceKoprogramu()
    print("*** Koprogram byl spusten ***")
end

-- vytvoreni koprogramu
koprogram = coroutine.create(funkceKoprogramu)

-- vypis typu objektu
print("Typ objektu:", koprogram)

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu:", coroutine.status(koprogram))

-- spusteni koprogramu
coroutine.resume(koprogram)

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu:", coroutine.status(koprogram))

