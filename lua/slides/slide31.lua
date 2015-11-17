---------------------------
-- Návratové hodnoty funkcí
---------------------------

-- nerekurzivni vypocet faktorialu
-- (funkce s jednim parametrem vracejici taktez jednu hodnotu)
function factorial(n)
    local result = 1
    -- faktorial je definovan pouze pro prirozena cisla a nulu
    if n < 0 then
        return nil
    end
    for i = 1, n do
        result = result * i
    end
    return result
end

print("n", "n!")
for n = -5, 10 do
    print(n, factorial(n))
end

