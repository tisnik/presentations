-- Demonstracni priklad s ukazkou manipulace s bufferem:
-- vlozeni informaci na zacatek i na konec bufferu.
-- Pavel Tisnovsky 2016
--
-- Nacteni prikladu do Vimu se provede prikazem:
-- :luafile insert_template



-- ziskame objekt predstavujici aktualni buffer
local b = vim.buffer()


-- pridani informaci na zacatek bufferu
b:insert("-------------------------------", 0)
b:insert("Edited by: " .. os.getenv("USER"), 0)
b:insert("-------------------------------", 0)

-- pridani informaci na konec bufferu
b:insert("Created at: " .. os.date("%Y-%m-%d (%A)"))

