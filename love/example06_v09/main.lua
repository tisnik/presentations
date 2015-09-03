--
-- Knihovna LÖVE
--
-- Šestý demonstrační příklad
--
-- Kreslení pomocí funkcí z knihovny love.graphics
--



-- rozměry okna
width = 450
height = 450

-- poloměr vykreslovaného obrazce
radius = 200



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    -- načtení standardního fontu a nastavení grafického režimu
    local font = love.graphics.newFont(love.default_font, 20)
    love.window.setMode(width, height, {})
    love.graphics.setFont(font)
end



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    local max = 120
    -- vykreslení obrazce složeného ze sady rovnostranných trojúhelníků
    for i=1, max, 3 do
        -- natočení trojúhelníku
        local colorAngle = math.rad(i*360/max)
        -- výpočet a nastavení barvy
        love.graphics.setColor(128+127*math.cos(colorAngle), 255, 128+128*math.sin(colorAngle))
        for j=0, 2 do
            local angle1 = math.rad(i + j * 120)
            local angle2 = angle1 + math.rad(120)
            local x1 = width/2 + radius*math.cos(angle1)
            local y1 = width/2 + radius*math.sin(angle1)
            local x2 = width/2 + radius*math.cos(angle2)
            local y2 = width/2 + radius*math.sin(angle2)
            love.graphics.line(x1, y1, x2, y2)
        end
    end
    love.graphics.setColor(255, 200, 255, 255)
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
