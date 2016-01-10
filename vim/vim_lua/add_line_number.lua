-- Demonstracni priklad s ukazkou pouziti prikazu luado
-- Pavel Tisnovsky 2016
--
-- Nacteni prikladu do Vimu se provede prikazem:
-- :luafile add_line_number.lua



-- Funkce urcena pro pridani cisla radku na kazdy (vybrany)
-- radek v aktualnim bufferu
function addLineNumber(line, linenr)
    return linenr .. " " .. line
end



-- Namapovani volani funkce na klavesovou zkratku ,c
vim.command("map ,n :luado return addLineNumber(line, linenr)<cr>")

