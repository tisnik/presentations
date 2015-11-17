---------------------------------
-- Bloky a viditelnost proměnných
---------------------------------

x=10                              -- vytvoreni globalni promenne x
print("globalni x=", x)

do                                -- zacatek bloku
    local x=20                    -- vytvoreni lokalni promenne x
    print("1. lokalni x=", x)
    do                            -- zacatek zanoreneho bloku
        local x=30                -- vytvoreni lokalni promenne x
        print("2. lokalni x=", x)
    end                           -- konec zanoreneho bloku
    print("1. lokalni x=", x)
end                               -- konec bloku

print("globalni x=", x)

