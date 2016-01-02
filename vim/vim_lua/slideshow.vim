" Slideshow tool v1.1
" Pavel Tisnovsky 2012, 2013, 2014



" Seznam s nazvy slajdu
let g:slides=readfile("list.txt")

" Prvky v poli se cisluji od nuly!
let g:index=0

function! GotoFirstSlide()
    let g:index = 0
endfunction

function! GotoLastSlide()
    let g:index = len(g:slides) - 1
endfunction

function! BeforeFirstSlide()
    return g:index < 0
endfunction

function! AfterLastSlide()
    return g:index >= len(g:slides)
endfunction

function! ShowNextSlide()
    let g:index += 1
    if AfterLastSlide()
        call GotoFirstSlide()
    endif
    call ShowActualSlide()
endfunction

function! ShowPrevSlide()
    let g:index -= 1
    if BeforeFirstSlide()
        call GotoLastSlide()
    endif
    call ShowActualSlide()
endfunction

function! ShowFirstSlide()
    call GotoFirstSlide()
    call ShowActualSlide()
endfunction

function! ShowLastSlide()
    call GotoLastSlide()
    call ShowActualSlide()
endfunction

function! ShowActualSlide()
    execute "edit" g:slides[g:index]
endfunction

function! StatusLine()
    return "Slide " . (1+g:index) . "/" . len(g:slides) . " : " . g:slides[g:index]
endfunction

" Hot keys
map <PageUp>   :call ShowPrevSlide()<cr>
map <PageDown> :call ShowNextSlide()<cr>
map <Home>     :call ShowFirstSlide()<cr>
map <End>      :call ShowLastSlide()<cr>

" Setup
set statusline=%!StatusLine()

" Potrebujeme zobrazit stavovy radek i ve chvili,
" kdy je zobrazeno pouze jedno okno
set laststatus=2

" Spustit prezentaci
:call ShowFirstSlide()

