--------------------------------------
-- Funkce jako plnohodnotný datový typ
--------------------------------------

funkce=print               -- promennym lze priradit i funkci
print("funkce=", funkce)
funkce(42)

print=1                    -- pozor! prepis globalniho objektu (zde funkce)
                           -- legalni, nicmene zpusobi problemy dale

print("dofile=", print)    -- nyni jiz funkce print neni dostupna

