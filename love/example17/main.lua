--
-- Knihovna LÖVE
--
-- Šestnáctý demonstrační příklad
--
-- Použití jednoduchého částicového systému.
--


-- rozměry okna, do něhož se bude provádět vykreslování
width = 600
height = 600

-- asociativní pole představující částicový systém
local particleSystem1 = nil
local particleSystem2 = nil


-- maximální počet částic v částicovém systému
particleCount = 1000


local colors = {
    {255, 255,   0, 100 ,255,   0,   0, 100},
    {255,   0,   0, 100 ,255, 255,   0, 100},
    {  0, 255,   0, 100 ,  0,   0,   0, 100},
    {255, 255, 255, 100 ,255,   0, 255, 100},
    {255, 255, 255, 100 ,255, 255,   0, 100},
    {255, 255, 255, 100 ,255,   0,   0, 100}
}

local sizes = {
    {3, 0.5},
    {5, 0},
    {1, 1},
    {0, 1},
    {10, 0},
    {0, 10},
}

local speeds = {
    {100, 400},
    {200, 800},
    {200, 0},
    {0, 200},
}

local emissionRates = {
    50, 100, 200, 300, 500, 5, 10}

local spreads = {
    0.3, 0.1, 1, 2, 3.14, 6.28
}

function getColors(index)
    return colors[index][1],
           colors[index][2],
           colors[index][3],
           colors[index][4],
           colors[index][5],
           colors[index][6],
           colors[index][7],
           colors[index][8]
end

function getSizes(index)
    return sizes[index][1],
           sizes[index][2]
end

function getEmissionRate(index)
    return emissionRates[index]
end

function getSpeeds(index)
    return speeds[index][1],
           speeds[index][2]
end

function getSpread(index)
    return spreads[index]
end

function createParticleSystem(x, y, particleImage)
    -- vytvoření částicového systému s jeho inicializací
    local particleSystemObject = love.graphics.newParticleSystem(particleImage, particleCount)

    -- kolik nových částic se průměrně vygeneruje za sekundu
    particleSystemObject:setEmissionRate(getEmissionRate(1))

    -- životnost emitoru částic i jednotlivých částic vytvářených v emitoru
    particleSystemObject:setLifetime(-1)
    particleSystemObject:setParticleLife(3)

    -- počáteční rychlost částic
    particleSystemObject:setSpeed(getSpeeds(1))

    -- pozice emitoru částic, směr generování částic a rozptyl
    particleSystemObject:setPosition(x, y)
    particleSystemObject:setDirection(-3.14/2)
    particleSystemObject:setSpread(getSpread(1))
    particleSystemObject:setSpin(1, 3)

    -- další parametry systému: gravitace působící na částice, změna barvy apod.
    particleSystemObject:setGravity(100, 200)
    particleSystemObject:setColors(getColors(1))

    -- velikost částic a relativní změna velikosti v čase
    particleSystemObject:setSizes(getSizes(1))
    particleSystemObject:stop()

    local particleSystem = {}
    particleSystem.particleSystemObject = particleSystemObject
    particleSystem.colorIndex = 1
    particleSystem.sizeIndex = 1
    particleSystem.emissionRateIndex = 1
    particleSystem.speedIndex = 1
    particleSystem.spreadIndex = 1
    return particleSystem
end



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
    local particleImage = love.graphics.newImage("particle.png")

    particleSystem1 = createParticleSystem(200, 500, particleImage)
    particleSystem2 = createParticleSystem(400, 500, particleImage)
end



--
-- Funkce volaná cca 30x za sekundu
--
function love.update(dt)
    -- přepočítat parametry částicového systému
    particleSystem1.particleSystemObject:update(dt)
    particleSystem2.particleSystemObject:update(dt)

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
    love.graphics.draw(particleSystem1.particleSystemObject, 0, 0)
    love.graphics.draw(particleSystem2.particleSystemObject, 0, 0)

    -- zprávy vypsané na obrazovky
    love.graphics.print("Enter: start particle emitters.", 10, 20)

    love.graphics.print("F1: start/stop 1st emitter.", 10, 40)
    love.graphics.print("F2: start/stop 2nd emitter.", 10, 60)
    love.graphics.print("F3: color for 1st emmiter.", 10, 80)
    love.graphics.print("F4: color for 2nd emmiter.", 10, 100)

    love.graphics.print("F5: particle sizes for 1st emmiter.", 10, 140)
    love.graphics.print("F6: particle sizes for 2nd emmiter.", 10, 160)
    love.graphics.print("F7: emision rate for 1st emmiter.", 10, 180)
    love.graphics.print("F8: emision rate for 2nd emmiter.", 10, 200)

    love.graphics.print("F9: particle speeds for 1st emmiter.", 10, 240)
    love.graphics.print("F10: particle speeds for 2nd emmiter.", 10, 260)
    love.graphics.print("F11: spread for 1st emmiter.", 10, 280)
    love.graphics.print("F12: spread for 2nd emmiter.", 10, 300)

    love.graphics.print("Escape: to exit.", 10, 583)
end



function startOrStopParticleSystem(particleSystem)
    if particleSystem.particleSystemObject:isActive() then
        particleSystem.particleSystemObject:stop()
    else
        particleSystem.particleSystemObject:start()
    end
end

function changeParticleSystemColors(particleSystem)
    particleSystem.colorIndex = particleSystem.colorIndex + 1
    if particleSystem.colorIndex > #colors then
         particleSystem.colorIndex = 1
    end
    particleSystem.particleSystemObject:setColors(getColors(particleSystem.colorIndex))
end

function changeParticleSystemSizes(particleSystem)
    particleSystem.sizeIndex = particleSystem.sizeIndex + 1
    if particleSystem.sizeIndex > #sizes then
         particleSystem.sizeIndex = 1
    end
    particleSystem.particleSystemObject:setSizes(getSizes(particleSystem.sizeIndex))
end

function changeParticleSystemEmissionRate(particleSystem)
    particleSystem.emissionRateIndex = particleSystem.emissionRateIndex + 1
    if particleSystem.emissionRateIndex > #emissionRates then
         particleSystem.emissionRateIndex = 1
    end
    particleSystem.particleSystemObject:setEmissionRate(getEmissionRate(particleSystem.emissionRateIndex))
end

function changeParticleSystemSpeeds(particleSystem)
    particleSystem.speedIndex = particleSystem.speedIndex + 1
    if particleSystem.speedIndex > #speeds then
         particleSystem.speedIndex = 1
    end
    particleSystem.particleSystemObject:setSpeed(getSpeeds(particleSystem.speedIndex))
end

function changeParticleSystemSpread(particleSystem)
    particleSystem.spreadIndex = particleSystem.spreadIndex + 1
    if particleSystem.spreadIndex > #spreads then
         particleSystem.spreadIndex = 1
    end
    particleSystem.particleSystemObject:setSpread(getSpread(particleSystem.spreadIndex))
end



--
-- Callback funkce zavolaná při stisku klávesy.
--
function love.keypressed(k)
    -- klávesou "Return" či "Enter" se částicový systém zapne
    if k == 'return' then
        particleSystem1.particleSystemObject:start()
        particleSystem2.particleSystemObject:start()
    elseif k == 'f1' then
        startOrStopParticleSystem(particleSystem1)
    elseif k == 'f2' then
        startOrStopParticleSystem(particleSystem2)
    elseif k == 'f3' then
        changeParticleSystemColors(particleSystem1)
    elseif k == 'f4' then
        changeParticleSystemColors(particleSystem2)
    elseif k == 'f5' then
        changeParticleSystemSizes(particleSystem1)
    elseif k == 'f6' then
        changeParticleSystemSizes(particleSystem2)
    elseif k == 'f7' then
        changeParticleSystemEmissionRate(particleSystem1)
    elseif k == 'f8' then
        changeParticleSystemEmissionRate(particleSystem2)
    elseif k == 'f9' then
        changeParticleSystemSpeeds(particleSystem1)
    elseif k == 'f10' then
        changeParticleSystemSpeeds(particleSystem2)
    elseif k == 'f11' then
        changeParticleSystemSpread(particleSystem1)
    elseif k == 'f12' then
        changeParticleSystemSpread(particleSystem2)
    elseif k == 'escape' then
    -- klávesou "Escape" se aplikace ukončí
        love.event.quit()
    end
end



--
-- finito
--

