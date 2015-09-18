--
-- Knihovna LÖVE
--
-- Čtrnáctý demontrační příklad
--
-- Použití jednoduchého částicového systému na nějž působí gravitace.
--


-- rozměry okna, do něhož se bude provádět vykreslování
width = 450
height = 450

-- asociativní pole představující částicový systém
local particleSystem = nil

-- maximální počet částic v částicovém systému
particleCount = 1000



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    -- načtení standardního fontu a nastavení grafického režimu
    local font = love.graphics.newFont(love.default_font, 40)

    -- inicializace grafického režimu
    love.graphics.setMode(width, height, false, false, 0)

    -- nastavení fontu
    love.graphics.setFont(font)

    -- načtení obrázku představujícího jednu částici
    local particleImage = love.graphics.newImage("sprite1.png")

    -- vytvoření částicového systému s jeho inicializací
    particleSystem = love.graphics.newParticleSystem(particleImage, particleCount)

    -- kolik nových částic se průměrně vygeneruje za sekundu
    particleSystem:setEmissionRate(10)

    -- životnost emitoru částic i jednotlivých částic vytvářených v emitoru
    particleSystem:setLifetime(-1)
    particleSystem:setParticleLife(5)

    -- pozice emitoru na obrazovce (mimo obrazovku)
    particleSystem:setPosition(width/2, -50)

    -- počáteční rychlost částic
    particleSystem:setSpeed(70, 100)
    particleSystem:setDirection(0)
    particleSystem:setSpread(360)

    -- další parametry systému: gravitace působící na částice
    particleSystem:setGravity(100, 200)
    -- velikost částic a relativní změna velikosti v čase
    particleSystem:setSizes(1, 0.3)
    particleSystem:stop()
end



--
-- Funkce volaná cca 30x za sekundu
--
function love.update(dt)
    -- přepočítat parametry částicového systému
    particleSystem:update(dt)

    local delay = 1/30
    if dt < delay then
        love.timer.sleep(delay - dt)
    end
end



--
-- Tato funkce je volána automaticky při překreslení obsahu
-- okna či obrazovky.
--
function love.draw()
    -- režim vykreslování
    love.graphics.setBlendMode("alpha")

    -- vykreslení částicového systému na obrazovku
    love.graphics.draw(particleSystem, 0, 0)

    -- zprávy vypsané na obrazovky
    love.graphics.print("Press Enter to start particle emitter.", 30, 415)
    love.graphics.print("Press Escape to exit.", 30, 433)
end



--
-- Callback funkce zavolaná při stisku klávesy.
--
function love.keypressed(k)
    -- klávesou "Return" či "Enter" se částicový systém zapne
    if k == 'return' then
        particleSystem:start()
    end
    -- klávesou "Escape" se aplikace ukončí
    if k == 'escape' then
        love.event.quit()
    end
end



--
-- finito
--

