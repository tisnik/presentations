---------
-- Funkce
---------

-- definice vlastnich funkci bez vyuziti
-- "syntaktickeho cukru"

-- funkce obsahujici lokalni promennou
-- (hodnota typu funkce je prirazena
--  promenne pojmenovane "printHello")
printHello = function()
    local helloStr = "Hello"
    print(helloStr)
end

worldStr="World"

-- funkce vyuzivajici globalni promennou
-- (hodnota typu funkce je prirazena
--  promenne pojmenovane "printWorld")
printWorld = function()
    -- ke globalni promenne je pripojena
    -- retezcova konstanta (literal)
    print(worldStr .. "!")
end

-- volani obou funkci
printHello()
printWorld()

-- zmena globalni promenne
-- se projevi i ve volane funkci
worldStr=42
printWorld()

