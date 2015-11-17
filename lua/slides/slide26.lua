--------------------------
-- Pole a asociativní pole
--------------------------

pole1={"hodnota1", "hodnota2", "hodnota3"}
pole2={klic1="hodnota1", klic2="hodnota2"}
pole3={klic1="hodnota1", klic2="hodnota2",}

pole3["klic3"] = "hodnota3"
pole3.klic4 = "hodnota4"

for index,hodnota in ipairs(pole1) do
    print(index, hodnota)
end

for klic,hodnota in pairs(pole3) do
    print(klic, hodnota)
end

