----------
-- Rekurze
----------

-- funkce pro rekurzivni vypocet faktorialu
function factorial(n)
    -- faktorial je definovan pouze pro prirozena cisla a nulu
    if n < 0 then
        return nil
    -- rekurze je ukoncena pri n=0
    elseif n == 0 then
        return 1
    else
        return n*factorial(n-1)
    end
end

-- vypis tabulky s faktorialy
print()
print("Factorial")
print("n", "n!")
for n = -5, 10 do
    print(n, factorial(n))
end

