--
-- Knihovna LÖVE
--
-- Třetí demonstrační příklad
--
-- Nastavení barvy vykreslování a vykreslení vyplněných obdélníků.
-- Naprogramování reakce na stisk klávesy [Esc].
--



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- velikost okna
    local width = love.graphics.getWidth()
    local height = love.graphics.getHeight()

    -- vykreslení matice obdélníků
    for j = 0,15 do
        for i = 0,15 do
            -- nastavení barvy vykreslování
            love.graphics.setColor(j*16, i*8+j*8, i*16)
            local x = 50 + i*30
            local y = 50 + j*30
            -- vykreslení vyplněného obdélníku
            love.graphics.rectangle("fill", x, y, 29, 29)
        end
    end
end



--
-- Callback funkce zavolaná při stisku klávesy.
--
function love.keypressed(k)
    if k == 'escape' then
        love.event.quit()
    end
end

--
-- finito
--
