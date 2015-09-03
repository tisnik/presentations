--
-- Knihovna LÖVE
--
-- Sedmý demonstrační příklad
--
-- Kreslení pomocí funkcí z knihovny love.graphics, nastavení režimu
-- směšování barev
--


-- rozměry okna
width = 450
height = 450

-- poloměr vykreslovaného obrazce
radius = 200

-- režim směšování barev
blending = "alpha"
-- konstanta pro směšování
blend_factor = 80



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    -- načtení standardního fontu a nastavení grafického režimu
    local font = love.graphics.newFont(love.default_font, 20)
    love.graphics.setMode(width, height, false, false, 0)
    love.graphics.setFont(font)
end



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- nastavení režimu směšování barev
    love.graphics.setBlendMode(blending)
    love.graphics.setColor(255, 255, 255, blend_factor)
    -- vykreslení obrazce
    for i=1, 90 do
        for j=0, 3 do
            local angle1 = math.rad(i + j * 90)
            local angle2 = angle1 + 90
            local x1 = width/2 + radius*math.cos(angle1*2)
            local y1 = width/2 + radius*math.sin(angle1*3)
            local x2 = width/2 + radius*math.cos(angle2*3)
            local y2 = width/2 + radius*math.sin(angle2*2)
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
    elseif k == 'b' then
        setBlending()
    end
end

-- povolení či zákaz směšování barev po stisku klávesy "b"
function setBlending()
    if blending == "alpha" then
        blending = "additive"
    else
        blending = "alpha"
    end
end


--
-- finito
--
