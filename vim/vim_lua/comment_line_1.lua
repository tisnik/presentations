-- Demonstracni priklad s ukazkou manipulace s okny a buffery.
-- Pavel Tisnovsky 2016
--
-- Nacteni prikladu do Vimu se provede prikazem:
-- :luafile comment_line_1.lua



-- Funkce urcena pro zakomentovani aktualniho radku
-- (bez detekce pouziteho programovaciho jazyka)
function commentLine()
    -- ziskame objekt predstavujici aktualni buffer
    local buffer = vim.buffer()
    -- ziskame objekt predstavujici aktualni okno a z nej
    -- vycteme cislo radku, na nemz se nachazi textovy kurzor
    local lineNumber = vim.window().line
    -- precteni puvodniho obsahu radku v bufferu
    local line = buffer[lineNumber]
    print("Changing the line #" .. lineNumber .. ": " .. line)
    line = "// " .. line
    -- modifikace radku v bufferu
    buffer[lineNumber] = line
end



-- Namapovani volani funkce na klavesovou zkratku ,c
vim.command("map ,c :lua commentLine()<cr>")

