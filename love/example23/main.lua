--
-- Knihovna LÖVE
--
-- Dvacátý třetí demonstrační příklad
--
-- Vyřešení problémů s rychle se pohybujícími tělesy
--



-- rozměry okna, do něhož se bude provádět vykreslování
width = 600
height = 600

-- parametry podlahy a stěny
ground_height = 50
wall_width = 2

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
    objects.ground.shape = love.physics.newRectangleShape(width, ground_height)
    -- propojení tvaru s tělesem
    objects.ground.fixture = love.physics.newFixture(objects.ground.body, objects.ground.shape, 5)
    objects.ground.fixture:setRestitution(0.7)

    -- těleso představující stěnu
    objects.wall = {}
    -- počáteční umístění tělesa
    objects.wall.body = love.physics.newBody(world, 200, height/2, "dynamic")
    -- tvar a rozměry
    objects.wall.shape = love.physics.newRectangleShape(wall_width, 200)
    -- propojení tvaru s tělesem
    objects.wall.fixture = love.physics.newFixture(objects.wall.body, objects.wall.shape, 5)
    objects.wall.fixture:setRestitution(0.7)

    -- těleso představující první míček
    objects.ball1 = {}
    -- počáteční umístění tělesa
    objects.ball1.body = love.physics.newBody(world, 550, height/2, "dynamic")
    objects.ball1.body:setLinearVelocity(-10000000,0)
    -- nutno nastavit na "true" - použije se pomalejší ale přesnější algoritmus výpočtu
    objects.ball1.body:setBullet(true)
    -- tvar a rozměry
    objects.ball1.shape = love.physics.newCircleShape(5)
    -- propojení tvaru s tělesem
    objects.ball1.fixture = love.physics.newFixture(objects.ball1.body, objects.ball1.shape, 5)
    objects.ball1.fixture:setRestitution(0.2)
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

    -- vykreslení stěny
    love.graphics.setColor(250, 100, 100)
    love.graphics.polygon("line", objects.wall.body:getWorldPoints(objects.wall.shape:getPoints()))

    -- vykreslení míčku
    love.graphics.setColor(250, 250, 150)
    love.graphics.circle("line", objects.ball1.body:getX(), objects.ball1.body:getY(),
                                 objects.ball1.shape:getRadius())

    -- vykreslení obalových těles
    love.graphics.setColor(128, 128, 128)
    local x1,y1,x2,y2 = objects.ball1.fixture:getBoundingBox()
    love.graphics.rectangle("line", x1, y1, x2-x1, y2-y1)

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

