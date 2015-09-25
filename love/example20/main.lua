--
-- Knihovna LÖVE
--
-- Dvacátý demonstrační příklad
--
-- Jednoduchý "svět", v němž se nachází dva míčky a jeden kvádr.
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

    -- těleso představující první míček
    objects.ball1 = {}
    -- počáteční umístění tělesa
    objects.ball1.body = love.physics.newBody(world, 400, 100, "dynamic")
    -- tvar a rozměry
    objects.ball1.shape = love.physics.newCircleShape(40)
    -- propojení tvaru s tělesem
    objects.ball1.fixture = love.physics.newFixture(objects.ball1.body, objects.ball1.shape, 5)
    objects.ball1.fixture:setRestitution(0.9)

    -- těleso představující druhý míček
    objects.ball2 = {}
    -- počáteční umístění tělesa
    objects.ball2.body = love.physics.newBody(world, 225, 50, "dynamic")
    -- tvar a rozměry
    objects.ball2.shape = love.physics.newCircleShape(50)
    -- propojení tvaru s tělesem
    objects.ball2.fixture = love.physics.newFixture(objects.ball2.body, objects.ball2.shape, 5000)
    objects.ball2.fixture:setRestitution(0.1)

    -- těleso představující kvádr
    objects.block3 = {}
    -- počáteční umístění tělesa
    objects.block3.body = love.physics.newBody(world, 450, 50, "dynamic")
    -- tvar a rozměry
    objects.block3.shape = love.physics.newRectangleShape(100, 100)
    -- propojení tvaru s tělesem
    objects.block3.fixture = love.physics.newFixture(objects.block3.body, objects.block3.shape, 5)
    objects.block3.fixture:setRestitution(0.0)
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

    -- vykreslení prvního tělesa (míčku)
    love.graphics.setColor(250, 150, 150)
    love.graphics.circle("line", objects.ball1.body:getX(), objects.ball1.body:getY(),
                                 objects.ball1.shape:getRadius())

    -- vykreslení druhého tělesa (míčku)
    love.graphics.setColor(150, 150, 250)
    love.graphics.circle("line", objects.ball2.body:getX(), objects.ball2.body:getY(),
                                 objects.ball2.shape:getRadius())

    -- vykreslení třetího tělesa (kvádru)
    love.graphics.setColor(150, 250, 150)
    love.graphics.polygon("line", objects.block3.body:getWorldPoints(objects.block3.shape:getPoints()))

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

