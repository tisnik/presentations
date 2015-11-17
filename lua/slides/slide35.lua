------------------------
-- Ukázkový příklad: ...
------------------------

-- funkce vracejici trojici:
-- 1. pocet prvku
-- 2. soucet prvku (suma)
-- 3. aritmeticky prumer jejich hodnot
function statistic(...)
   -- pokud nejsou zadany zadne parametry,
   -- neni nutne vypocet provadet
   if ... == nil then
       return 0, 0, 0
   end
   -- prevod seznamu parametru
   -- na asociativni pole
   items = {...}
   -- pocet prvku
   n = #items
   sum = 0
   -- vypocet sumy
   for i=1, n do
      sum = sum + items[i]
   end
   return n, sum, sum/n
end

print("n", "sum", "average")
print(statistic())
print(statistic(1, 2, 3, 4))
print(statistic(1, 1, 0, 0))
print(statistic(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

