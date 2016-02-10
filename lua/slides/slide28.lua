---------
-- Funkce
---------

-- funkce obsahujici lokalni promennou
function printHello()
    local helloStr = "Hello"
    print(helloStr)
end

printHello()

worldStr="World"

-- funkce vyuzivajici globalni promennou
function printWorld()
    -- ke globalni promenne je pripojena
    -- retezcova konstanta (literal)
    print(worldStr .. "!")
end

-- volani obou funkci
printHello()
printWorld()

-- zmena globalni promenne
-- se projevi i ve volane funkci
worldStr = 42
printWorld()

