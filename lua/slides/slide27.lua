--------------------------
-- Pole a asociativní pole
--------------------------

pole={klic1="hodnota1", "hodnota2", klic2="hodnota3", "hodnota4"}

print(pole["klic1"])
print(pole["klic2"])
print(pole["klic3"]) -- neexistujici prvek, vypise se "nil"
print(pole.klic1)
print(pole.klic2)
print(pole.klic3)    -- neexistujici prvek, vypise se "nil"

