-----------------------
-- Objekty v jazyce Lua
-----------------------

Complex = {}

-- Metatabulka pro objekty predstavujici komplexni cisla
complex_meta = {
    -- Pro "objektovy" zpusob volani metod
    __index = Complex
}

-- Konstruktor pro komplexni cisla
function Complex:new(real, imag)
    -- asociativni pole pro ulozeni atributu
    local value = { real = real, imag = imag }
    return setmetatable(value, complex_meta)
end

-- Metoda print
function Complex:print()
    print(self.real, self.imag)
end

-- Objekty predstavujici komplexni cisla
z1 = Complex:new(1, 2)
z2 = Complex:new(3, 4)
z3 = Complex:new(5, 6)

-- Ruzne zpusoby zavolani metody print()

-- primo pres "tridu" - nepouziva se metatabulka
Complex.print(z1)

-- pres metatabulku, explicitni naplneni parametru self
z2.print(z2)

-- pres metatabulku, vyuziti syntaktickeho cukru
-- pro automaticke naplneni parametru self
z3:print()

