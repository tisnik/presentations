------------------------------
-- Programové smyčky: for-each
------------------------------

for namelist in explist do
    blok příkazů umístěný v těle smyčky
end

months={"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"}

for poradi,month in pairs(months) do
    print(poradi, month)
end

-- pozor na rozdíl mezi pairs() a ipairs()!

