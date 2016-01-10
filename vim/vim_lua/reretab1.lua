-- Demonstracni priklad s ukazkou pouziti prikazu luado
-- Pavel Tisnovsky 2016
--
-- Nacteni prikladu do Vimu se provede prikazem:
-- :luafile reretab1.lua



-- Funkce urcena pro nahrazeni ctyr mezer znakem <Tab>
function reretab(line, linenr)
    local tabstop = 4
    local spaces = string.rep(" ", tabstop)
    return string.gsub(line, spaces, "\t")
end



-- Namapovani volani funkce na klavesovou zkratku ,c
vim.command("map ,r :luado return reretab(line, linenr)<cr>")

