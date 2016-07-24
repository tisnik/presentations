local infile = io.open("test6.data")
local lineno = 1

if not infile then
    print("Chyba pri otevirani souboru")
else
    for line in infile:lines() do
        print(lineno, line)
        tex.print(lineno .. "&" .. line)
        tex.print("\\\\")
        lineno = lineno + 1
    end
    infile:close()
end

