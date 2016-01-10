-- Demonstracni priklad s ukazkou pouziti prikazu luado
-- Pavel Tisnovsky 2016
--
-- Nacteni prikladu do Vimu se provede prikazem:
-- :luafile reretab2.lua



-- Funkce urcena pro nahrazeni mezer znakem <Tab>
function reretab(line, linenr)
    -- volba tabstob ci ts obsahuje pocet mezer
    local tabstop = vim.eval("&ts")
    local spaces = string.rep(" ", tabstop)
    -- nahrazeni mezer za znaky <Tab>
    return string.gsub(line, spaces, "\t")
end



-- Namapovani volani funkce na klavesovou zkratku ,c
vim.command("map ,r :luado return reretab(line, linenr)<cr>")

