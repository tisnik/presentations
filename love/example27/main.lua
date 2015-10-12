--
-- Knihovna LÖVE
--
-- Dvacátý sedmý demonstrační příklad
--
-- Vytvoření pružných vazeb mezi několika tělesy.
--



-- rozměry okna, do něhož se bude provádět vykreslování
width = 600
height = 600
ground_height = 50

-- tíhové zrychlení
G = 9.81

-- počet pixelů odpovídající jednomu metru v simulovaném světě
pixels_per_meter = 64



--
-- Funkce volaná při inicializaci aplikace.
--
function love.load()
    -- načtení standardního fontu a nastavení grafického režimu
    local font = love.graphics.newFont(love.default_font, 40)

    -- inicializace grafického režimu
    love.graphics.setMode(width, height, false, false, 0)

    -- nastavení rozměrů simulovaného světa
    -- (mapování fyzikálních jednotek na pixely)
    love.physics.setMeter(pixels_per_meter)

    -- vytvoření simulovaného světa
    world = love.physics.newWorld(0, G * pixels_per_meter, true)

    -- tabulka s tělesy
    objects = {}

    -- těleso představující zemi
    objects.ground = {}
    -- počáteční umístění tělesa
    objects.ground.body = love.physics.newBody(world, width/2, height-ground_height/2-40)
    -- tvar a rozměry
    objects.ground.shape = love.physics.newRectangleShape(0, 0, width, ground_height, -0.15)
    -- propojení tvaru s tělesem
    objects.ground.fixture = love.physics.newFixture(objects.ground.body, objects.ground.shape, 5)
    objects.ground.fixture:setRestitution(0.7)

    objects.mesh = {}
    for i = 1, 5 do
        objects.mesh[i] = {}
        for j = 1, 5 do
            -- těleso představující míček
            local obj = {}
            -- počáteční umístění tělesa
            obj.body = love.physics.newBody(world, 300 + i * 30, 50 + j * 30, "dynamic")
            -- tvar a rozměry
            obj.shape = love.physics.newCircleShape(10)
            -- propojení tvaru s tělesem
            obj.fixture = love.physics.newFixture(obj.body, obj.shape, 5)
            obj.fixture:setRestitution(0.9)
            objects.mesh[i][j] = obj
        end
    end

    -- vytvoření pružné vazby mezi míčky
    for i = 1, 5 do
        for j = 1, 4 do
            local obj = {}
            local b1 = objects.mesh[i][j].body
            local b2 = objects.mesh[i][j+1].body
            local joint = love.physics.newDistanceJoint(b1, b2,
                        b1:getX(), b1:getY(),
                        b2:getX(), b2:getY())
            joint:setLength(22)
            joint:setFrequency(20)
        end
    end

    -- vytvoření kolmé pružné vazby mezi míčky
    for i = 1, 4 do
        for j = 1, 5 do
            local obj = {}
            local b1 = objects.mesh[i][j].body
            local b2 = objects.mesh[i+1][j].body
            local joint = love.physics.newDistanceJoint(b1, b2,
                        b1:getX(), b1:getY(),
                        b2:getX(), b2:getY())
            joint:setLength(22)
            joint:setFrequency(20)
        end
    end
end



--
-- Funkce volaná cca 30x za sekundu
--
function love.update(dt)
    -- přepočítat parametry celého "světa"
    world:update(dt)

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
    -- vykreslení země
    love.graphics.setColor(72, 160, 14)
    love.graphics.polygon("line", objects.ground.body:getWorldPoints(objects.ground.shape:getPoints()))

    -- vykreslení všech míčků
    love.graphics.setColor(250, 150, 150)
    for i = 1, 5 do
        for j = 1, 5 do
            local obj = objects.mesh[i][j]
            love.graphics.circle("line", obj.body:getX(), obj.body:getY(),
                                         obj.shape:getRadius())
        end
    end

    -- vykreslení pružné vazby
    love.graphics.setColor(150, 150, 250)
    for i = 1, 5 do
        for j = 1, 4 do
            local obj1 = objects.mesh[i][j]
            local obj2 = objects.mesh[i][j+1]
            love.graphics.line(obj1.body:getX(), obj1.body:getY(),
                               obj2.body:getX(), obj2.body:getY())
        end
    end
    for i = 1, 4 do
        for j = 1, 5 do
            local obj1 = objects.mesh[i][j]
            local obj2 = objects.mesh[i+1][j]
            love.graphics.line(obj1.body:getX(), obj1.body:getY(),
                               obj2.body:getX(), obj2.body:getY())
        end
    end

    -- výpis zprávy
    love.graphics.setColor(250, 250, 250)
    love.graphics.print("Escape: to exit.", 20, 615)
end



--
-- Callback funkce zavolaná při stisku klávesy.
--
function love.keypressed(k)
    if k == 'escape' then
    -- klávesou "Escape" se aplikace ukončí
        love.event.quit()
    elseif k == 'r' then
    -- restart celé simulace po stisku klávesy [R]
        love.load()
    end
end



--
-- finito
--

