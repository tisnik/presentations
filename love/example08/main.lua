--
-- Knihovna LÖVE
--
-- Osmý demonstrační příklad
--
-- Práce se sprity.
--


-- rozměry okna
width = 450
height = 450



local sprite1 = nil
local sprite2 = nil



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    -- načtení standardního fontu a nastavení grafického režimu
    local font = love.graphics.newFont(love.default_font, 40)
    -- načtení spritů
    sprite1 = love.graphics.newImage("sprite1.png")
    sprite2 = love.graphics.newImage("sprite2.png")
    love.graphics.setMode(width, height, false, false, 0)
    love.graphics.setFont(font)
end



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- velikost okna
    local windowWidth = love.graphics.getWidth()
    local windowHeight = love.graphics.getHeight()

    -- vykreslení mřížky
    for y=0, windowHeight - sprite2:getHeight(), sprite2:getHeight()+5 do
        for x=0, windowWidth - sprite2:getWidth(), sprite2:getWidth()+5 do
            love.graphics.draw(sprite2, x, y)
        end
    end

    -- vykreslení prvního spritu přes ostatní sprity
    love.graphics.draw(sprite1, 30, 30)
    love.graphics.print("Press escape to exit.", 30, 433)
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
