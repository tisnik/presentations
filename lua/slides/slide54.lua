-------------------------------------------
-- Inicializace koprogramu pomocí parametrů
-------------------------------------------

-- predani parametru koprogramu pri jeho prvnim spusteni

-- vytvoreni koprogramu s vyuzitim anonymni funkce
koprogram = coroutine.create(
    function(opakovani)
        print("Predany pocet opakovani: ", opakovani)
        if opakovani <= 1 then
            return
        end
        for i=1, opakovani do
            print("*** telo koprogramu pred zavolanim yield: "..i.." ***")
            coroutine.yield()
            print("*** telo koprogramu po zavolani yield: "..i.." ***")
        end
    end
)

-- vypis typu objektu
print("Typ objektu:", koprogram)

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu pred jeho spustenim:", coroutine.status(koprogram))
print()

coroutine.resume(koprogram, 5)

print("Stav koprogramu pred vstupem do smycky:", coroutine.status(koprogram))
print()

counter = 0
-- spusteni a znovuspusteni koprogramu
while coroutine.resume(koprogram) do
    counter = counter + 1
    print("Funkce coroutine.resume() volana "..counter.."x")
    print("Stav koprogramu ve smycce while:", coroutine.status(koprogram))
    print()
end

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu po ukonceni smycky while:", coroutine.status(koprogram))

