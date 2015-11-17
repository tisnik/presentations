------------------------------------
-- Programové smyčky: for (počítaná)
------------------------------------

for prom=x1, x2 do
    blok příkazů umístěný v těle smyčky
end

for prom=x1, x2, krok do
    blok příkazů umístěný v těle smyčky
end

function star(step1, step2)
    for i=0, 35 do
        for j=0, 6 do
            left(2*360/7)
            forward(step1)
        end
        left(step2)
    end
end

