------------------------------
-- Předávání parametrů funkcím
------------------------------

-- funkce se dvema parametry,
-- ktera nevraci zadnou hodnotu
function repeatMessage(message, count)
    for i = 1, count do
        print(i, message)
    end
end

-- volani funkce
repeatMessage("Hello world!", 10)

