--
-- Knihovna LÖVE
--
-- Osmnáctý demonstrační příklad
--
-- Jednoduchý "svět", v němž se nachází dva kvádry.
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
    objects.ground.body = love.physics.newBody(world, width/2, height-ground_height/2)
    -- tvar a rozměry
    objects.ground.shape = love.physics.newRectangleShape(width, ground_height)
    -- propojení tvaru s tělesem
    objects.ground.fixture = love.physics.newFixture(objects.ground.body, objects.ground.shape, 5)

    -- těleso představující první kvádr
    objects.block1 = {}
    -- počáteční umístění tělesa
    objects.block1.body = love.physics.newBody(world, 200, 200, "dynamic")
    -- tvar a rozměry
    objects.block1.shape = love.physics.newRectangleShape(40, 150)
    -- propojení tvaru s tělesem
    objects.block1.fixture = love.physics.newFixture(objects.block1.body, objects.block1.shape, 5)

    -- těleso představující druhý kvádr
    objects.block2 = {}
    -- počáteční umístění tělesa
    objects.block2.body = love.physics.newBody(world, 225, 50, "dynamic")
    -- tvar a rozměry
    objects.block2.shape = love.physics.newRectangleShape(100, 50)
    -- propojení tvaru s tělesem
    objects.block2.fixture = love.physics.newFixture(objects.block2.body, objects.block2.shape, 5)
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

    -- vykreslení prvního tělesa
    love.graphics.setColor(250, 150, 150)
    love.graphics.polygon("line", objects.block1.body:getWorldPoints(objects.block1.shape:getPoints()))

    -- vykreslení druhého tělesa
    love.graphics.setColor(150, 150, 250)
    love.graphics.polygon("line", objects.block2.body:getWorldPoints(objects.block2.shape:getPoints()))

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
    end
end



--
-- finito
--

