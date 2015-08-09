--
-- Knihovna LÖVE
--
-- První demonstrační příklad
--
-- Ukázka základní vykreslovací funkce: love.graphics.line()
--



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- velikost okna
    local width = love.graphics.getWidth()
    local height = love.graphics.getHeight()

    -- zobrazeni několika úseček
    for offset = 20, height/2-5, 20 do
        -- jediné volání této funkce může vést k vykreslení
        -- většího množství úseček
        love.graphics.line(offset, offset,
                           width-offset, offset,
                           width-offset, height-offset,
                           offset, height-offset,
                           offset, offset)
    end
end

--
-- finito
--
