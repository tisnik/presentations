----------
-- Rekurze
----------

-- rekurzivni vypocet binomickeho koeficientu
function binomical(n, k)
    if k == 0 then
        return 1
    else
        return binomical(n - 1, k - 1) * n / k;
    end
end

-- vypis nekterych hodnot "n nad k"
print()
print("Binomical coefficients")
print("n", "k", "n nad k")
for k = 0, 10 do
    for n = k, 10 do
        print(n, k, binomical(n, k))
    end
end

