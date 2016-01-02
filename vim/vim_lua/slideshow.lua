-- Slideshow tool v1.1
-- Pavel Tisnovsky 2016



-- Pole s nazvy slajdu
local slides = nil

-- Prvky v poli se cisluji od jednicky!
local index = 1

function loadSlideList(filename)
    local slides = {}
    for line in io.lines(filename) do
        table.insert(slides, line)
    end
    return slides
end

function gotoFirstSlide()
    index = 1
end

function gotoLastSlide()
    index = #slides
end

function beforeFirstSlide()
    return index < 1
end

function afterLastSlide()
    return index > #slides
end

function showNextSlide()
    index = index + 1
    if afterLastSlide() then
        gotoFirstSlide()
    end
    showActualSlide()
end

function showPrevSlide()
    index = index - 1
    if beforeFirstSlide() then
        gotoLastSlide()
    end
    showActualSlide()
end

function showFirstSlide()
    gotoFirstSlide()
    showActualSlide()
end

function showLastSlide()
    gotoLastSlide()
    showActualSlide()
end

function showActualSlide()
    vim.command("edit " .. slides[index])
end

function statusLine()
    return "Slide " .. index .. "/" .. #slides .. " : " .. slides[index]
end

slides = loadSlideList("list.txt")

-- Hot keys
vim.command("map <PageUp>   :lua showPrevSlide()<cr>")
vim.command("map <PageDown> :lua showNextSlide()<cr>")
vim.command("map <Home>     :lua showFirstSlide()<cr>")
vim.command("map <End>      :lua showLastSlide()<cr>")

-- Setup
vim.command([[
function! StatusLine()
    return luaeval('statusLine()')
endfunction]])
vim.command("set statusline=%!StatusLine()")

-- Potrebujeme zobrazit stavovy radek i ve chvili,
-- kdy je zobrazeno pouze jedno okno
vim.command("set laststatus=2")

-- Spustit prezentaci
showFirstSlide()

