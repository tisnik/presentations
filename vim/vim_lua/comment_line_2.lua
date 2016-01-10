-- Demonstracni priklad s ukazkou manipulace s okny a buffery
-- i se ctenim aktualniho nastaveni
-- Pavel Tisnovsky 2016
--
-- Nacteni prikladu do Vimu se provede prikazem:
-- :luafile comment_line_2.lua



-- Funkce vracejici znaky urcene pro zakomentovani radku.
-- O ktere znaky se jedna, se zjisti na zaklade konfiguracni volby
-- "syntax"
function getCommentChars()
    local languages = {
        lua        = "--",
        c          = "//",
        java       = "//",
        javascript = "//",
        vim        = "\"",
        clojure    = ";",
        sh         = "#",
        python     = "#"}
    -- ziskani informace o aktualne nastavene syntaxi
    local selectedSyntax = vim.eval("&syntax")
    -- vraceni znaku z tabulky (popr. vraceni nil ve chvili,
    -- kdy je syntaxe neznama)
    return languages[selectedSyntax]
end



-- Funkce pro zakomentovani aktualniho radku
function commentLine()
    -- ziskame objekt predstavujici aktualni buffer
    local buffer = vim.buffer()
    -- ziskame objekt predstavujici aktualni okno a z nej
    -- vycteme cislo radku, na nemz se nachazi textovy kurzor
    local lineNumber = vim.window().line
    -- precteni puvodniho obsahu radku v bufferu
    local line = buffer[lineNumber]
    local commentChars = getCommentChars()

    -- pokud je znama syntaxe, provede se zakomentovani
    if commentChars then
        print("Changing the line #" .. lineNumber .. ": " .. line)
        line = commentChars .. " " .. line
        -- modifikace radku v bufferu
        buffer[lineNumber] = line
    end
end



-- Namapovani volani funkce na klavesovou zkratku ,c
vim.command("map ,c :lua commentLine()<cr>")

