---------------------------
-- Proměnný počet parametrů
---------------------------

-- funkce s dvojici pojmenovanych parametru
-- s moznosti pristupu k dalsim parametrum
-- pristupnym pres vyraz ...
function g(x, y, ...)
    -- pokud je seznam volitelnych parametru
    -- naplnen alespon jednou hodnotou,
    -- vypise se jeho delka
    if ... ~= nil then
        -- prevod na asociativni pole
        local varargs = {...}
        -- vypis delky pole
        print("vararg length: ", #varargs .. " items")
    end
    -- vypis obou pojmenovanych parametru
    -- i promennych parametru
    print(x, y, ...)
end

-- ukazka volani funkce
g()
g(1)
g(1,2)
g(1,2,3)
g(1,2,3,4)
g(1,2,3,5)
g("a", "b", "c", "d", "e")

