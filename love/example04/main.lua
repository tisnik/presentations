--
-- Knihovna LÖVE
--
-- Čtvrtý demonstrační příklad
--
-- Naprogramování dalších reakcí na události.
--

local border = 50
local rectangleOffset = 30
local rectangleSize = 29

local selX = nil
local selY = nil

--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
   love.graphics.setColor(0,0,0)
   love.graphics.setBackgroundColor(255,255,255)
end



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
            local x = border + i*rectangleOffset
            local y = border + j*rectangleOffset
            -- vykreslení vyplněného obdélníku
            love.graphics.rectangle("fill", x, y, rectangleSize, rectangleSize)
        end
    end
    if selX and selY then
        -- nastavení barvy vykreslování
        love.graphics.setColor(255-selY*16, selX*8+selY*8, 255-selX*16)
        -- vykreslení vyplněného obdélníku
        love.graphics.rectangle("fill", selX, selY, rectangleSize, rectangleSize)
    end
end



--
-- Callback funkce zavolaná při stisku tlačítka myši.
--
function love.mousepressed(x, y, button)
    if button == 'l' then
        if x > border and x < border + rectangleOffset*16 and
           y > border and y < border+rectangleOffset*16 then
            selX = x - ((x-border) % rectangleOffset)
            selY = y - ((y-border) % rectangleOffset)
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
