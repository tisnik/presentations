--------------
-- Metatabulky
--------------

-- Asociativni pole predstavujici zaklad objektu
objekt = {}

-- Asociativni pole, ktere bude pouzito jako metatabulka
metatable = {}

-- Ziskani metatabulky (vrati se nil, ktere se posleze vytiskne)
print(getmetatable(objekt))

-- Prirazeni metatabulky k objektu
setmetatable(objekt, metatable)

-- Ziskani metatabulky (vrati se prazdne pole, nikoli nil)
table = getmetatable(objekt)

print(table)

-- Tisk obsahu metatabulky
for key, value in pairs(table) do
    print(key, value)
end

