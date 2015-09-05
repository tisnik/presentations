--
-- Knihovna LÖVE
--
-- Devátý demonstrační příklad
--
-- Práce se sprity: zobrazení, posun.
-- (skákající míčky)
--


-- rozměry okna
width = 450
height = 450



-- objekty představující sprity zobrazené v okně
local sprite1 = {x=100, y=100, dx=4, dy=0}
local sprite2 = {x=200, y=10,  dx=3, dy=0}
local sprite3 = {x=300, y=100, dx=2, dy=0}



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    -- načtení standardního fontu a nastavení grafického režimu
    local font = love.graphics.newFont(love.default_font, 40)
    -- načtení spritů
    sprite1.image = love.graphics.newImage("sprite2.png")
    sprite2.image = love.graphics.newImage("sprite1.png")
    sprite3.image = love.graphics.newImage("sprite2.png")
    love.graphics.setMode(width, height, false, false, 0)
    -- nastavení fontu
    love.graphics.setFont(font)
end



--
-- Vykreslení spritu s jeho posunem.
--
function drawSprite(sprite)
    -- vykreslení spritu s posunem
    love.graphics.draw(sprite.image, sprite.x, sprite.y)
end



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- vykreslení prvního spritu přes ostatní sprity
    drawSprite(sprite1)
    -- vykreslení druhého spritu přes ostatní sprity
    drawSprite(sprite2)
    -- vykreslení třetího spritu přes ostatní sprity
    drawSprite(sprite3)

    love.graphics.print("Press escape to exit.", 30, 433)
end



--
-- Změna pozice spritů v okně
--
function updateSpritePosition(sprite)
    -- velikost okna
    local windowWidth = love.graphics.getWidth()
    local windowHeight = love.graphics.getHeight()

    sprite.x = sprite.x + sprite.dx
    sprite.y = sprite.y + sprite.dy

    if sprite.x < 1 or sprite.x > windowWidth - sprite.image:getWidth() - 2 then
        sprite.dx = -sprite.dx
    end
    if sprite.y < 1 or sprite.y > windowHeight - sprite.image:getHeight() - 2 then
        sprite.dy = -sprite.dy
    end
    sprite.dy = sprite.dy + 0.1
end



--
-- Funkce volaná cca 30x za sekundu
--
function love.update(dt)
    updateSpritePosition(sprite1)
    updateSpritePosition(sprite2)
    updateSpritePosition(sprite3)
    local delay = 1/30
    if dt < delay then
        love.timer.sleep(delay - dt)
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
