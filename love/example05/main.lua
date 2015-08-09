--
-- Knihovna LÖVE
--
-- Pátý demonstrační příklad
--
-- Načtení obrázku ze souboru, zobrazení obrázku.
--



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    image = love.graphics.newImage("gnome-globe.png")
end



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- velikost okna
    local windowWidth = love.graphics.getWidth()
    local windowHeight = love.graphics.getHeight()

    -- velikost bitmapy
    local imageWidth = image:getWidth()
    local imageHeight = image:getHeight()

    -- výpočet umístění bitmapy
    local x = windowWidth/2 - imageWidth/2
    local y = windowHeight/2 - imageHeight/2

    -- zobrazení bitmapy
    love.graphics.draw(image, x, y)
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
