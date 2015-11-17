------------------------------------------
-- Přerušení koprogramu a obnova jeho běhu
------------------------------------------

-- vytvoreni koprogramu s vyuzitim anonymni funkce
koprogram = coroutine.create(
    function()
        for i=1, 10 do
            print("*** telo koprogramu pred zavolanim yield: "..i.." ***")
            coroutine.yield()
            print("*** telo koprogramu po zavolani yield: "..i.." ***")
        end
    end
)

-- vypis typu objektu
print("Typ objektu:", koprogram)

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu pred vstupem do smycky while:", coroutine.status(koprogram))
print()

counter = 0
-- spusteni a znovuspusteni koprogramu
while coroutine.resume(koprogram) do
    counter = counter + 1
    print("Funkce coroutine.resume() volano "..counter.."x")
    print("Stav koprogramu ve smycce while:", coroutine.status(koprogram))
    print()
end

-- zjisteni a vypis stavu koprogramu
print("Stav koprogramu po ukonceni smycky while:", coroutine.status(koprogram))

