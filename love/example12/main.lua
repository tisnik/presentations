--
-- Knihovna LÖVE
--
-- Dvanáctý demonstrační příklad
--
-- Práce se sprity: zobrazení, otočení změnou souřadnicového systému.
--


-- rozměry okna
width = 450
height = 450



-- objekty představující sprity zobrazené v okně
local sprite1 = {x=100, y=100, r=0, dr=-0.17}
local sprite2 = {x=185, y=80,  r=0, dr=0.1}
local sprite3 = {x=300, y=100, r=0, dr=0.05}



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
-- Vykreslení spritu s jeho otočením.
--
function drawSprite(sprite)
    -- uložení transformační matice
    love.graphics.push()
    -- zajištění posunu a rotace
    love.graphics.translate(sprite.x, sprite.y)
    love.graphics.translate(sprite.image:getWidth()/2, sprite.image:getHeight()/2)
    love.graphics.rotate(sprite.r)
    love.graphics.translate(-sprite.image:getWidth()/2, -sprite.image:getHeight()/2)
    -- vykreslení spritu
    love.graphics.draw(sprite.image, 0, 0)
    -- obnovení původní transformační matice
    love.graphics.pop()
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
-- Změna rotace spritů v okně
--
function updateSpriteAngle(sprite)
    sprite.r = sprite.r + sprite.dr
end



--
-- Funkce volaná cca 30x za sekundu
--
function love.update(dt)
    updateSpriteAngle(sprite1)
    updateSpriteAngle(sprite2)
    updateSpriteAngle(sprite3)
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
