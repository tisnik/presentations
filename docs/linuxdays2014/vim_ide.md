# Vim ve funkci integrovaného vývojového prostředí

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz>`
* Datum: 2014-10-05

## Vim

* 1988 Vi iMitation   Bram Moolenaar (Amiga)
* Později přenos na Unixové systémy
    - Vi iMitation -> Vi iMproved
* Z Vi převzaty:
    - modální režim práce
    - klávesové zkratky
    - většina voleb
    - příkazy (příkazový režim)
* Podpora pluginů, tabů, oken
* Zvýraznění syntaxe, kontrola pravopisu
* Makra, skriptování

Vim při vývoji
--------------
* Obecné vlastnosti
    - Konfigurační volby
    - Zobrazení textů
    - Zalamování textů
    - Folding
    - Okna, buffery, taby
* Vim a jazyky C/C++
* Vim a Java
* Vim a Clojure
* Vim a XML
* Vim a HTML
* Režim diff
* Editace binárních souborů

Základní konfigurační volby
---------------------------
```
    :set nocompatible
    :set ruler
    :set statusline=...
    :set (no)expandtab
    (:retab)
    :set backspace=[indent,eol,start]
    :set filetype=[dos,unix]
    :set selection=exclusive
        bloky se chovají podobně jako v ostatních editorech
    :set wildmenu
        bude se nabízet seznam souborů po TAB
    :set wildignore=*~,*.bak,*.log,*.aut,*.dvi,*.o
        soubory (masky nazvů), které se nebudou zobrazovat
```

Volby způsobu zobrazení textů
-----------------------------
```
    :set number
    :set list
    :set tabstop=xxx
    :set showmatch
    :set matchpairs=(:),[:],{:},<:>
```

Chování editoru při chybě
-------------------------
```
    :set novisualbell
    :set vb t_vb="
```

Zvýraznění aktuálního řádku/sloupce
-----------------------------------
```
    :set cursorcolumn
    :set cursorline
    :hi CursorLine   guibg=#2d2d2d
    :hi CursorColumn guibg=#2d2d2d
```

Taby nebo mezery?
-----------------
```
    :syn match Tab "\t"
    :syn match Tab2 "\t\t"
    :hi def Tab  ctermbg=lightgreen guibg=#e0ffe0
    :hi def Tab2 ctermbg=lightred guibg=#ffe0e0
```

Zalamování textu
----------------
```
    :set wrap
        pouze vizuální zalamování (do souborů se nevkládá CR)
    :set nowrap
        vypnutí vizuálního zalamování
    :set linebreak
        vizuální zalamování na hranicích slov (vhodné pro texty)
    :set nolinebreak
        vypnutí vizuálního zalamování na hranicích slov
    :set tw=xxx
        automatické zalamování na xxx sloupci (vkládá se CR)
```

Konfigurace Vimu s GUI
----------------------
* vim -g, gvim ...
* .gvimrc
* Konfigurační volby
```
    :set guifont?
    :set guifont=DejaVu\ Sans\ Mono\ 12
    :set guifont=*
    :set linespace=počet_pixelů
    :set guioptions?
    :set guioptions+=a       " kdyz neco oznacime pres <v>, tak se to ulozi do clipboardu
    :set guioptions-=T       " vypnuti toolbaru
    :set guioptions-=mM      " vypnuti menu
```

Příliš mnoho konfiguračních voleb?
----------------------------------
* :options

Taby, okna, buffery
-------------------
* Lze vzájemně kombinovat
    - Taby
        • Rozdělení plochy na okna
* Rozdělení plochy na okna
    - Základ většiny pluginů, které z Vimu dělají IDE

Taby
----
```
    :tabnew
    :tabnew soubor
    :tabnext
    :tabfirst
    Ctrl+W gf
```

Okna
----
* Vytvoření a zrušení oken
```
    Ctrl+W n (new)
    Ctrl+W s (split)
    Ctrl+W v (vertical split)
    Ctrl+W f (file)
    :q
```
* Přepínání mezi okny, přesuny oken
```
    Ctrl+W w (přepínání oken)
    Ctrl+W Ctrl+W (dtto, ale rychlejší)
    Ctrl+W h/j/k/l (přepínání oken v daném směru)
    Ctrl+W<Shift>h/j/k/l (přesun oken)
```

Okna
----
```
    Ctrl++   (zvětšení pro horizontálně rozdělené okno)
    Ctrl+-   (zmenšení pro horizontálně rozdělené okno)
    Ctrl+=   (stejná velikost)
    Ctrl+>   (zvětšení pro vertikálně rozdělené okno)
    Ctrl+<   (zmenšení pro vertikálně rozdělené okno)
```

Buffery
-------
```
    :bn(ext)
    :bp(rev)
    :bf(irst)
    :bl(ast)
```

Folding
-------
```
    :set foldmethod
        manual
        indent
        expr
        marker
        syntax
        diff   (diff mode)
    zf  (fold)  - jen při foldmethod=manual
        - pracuje jako operátor
    zo  (open)  zO - rekurze
    zc  (close) zC - rekurze
    zv  (view cursor line)
    zd  (delete)   - ne pro text
```

Práce s tagy
------------
* Vytvoření souborů taglist.txt
    - ctags
    - ctags -R
    - ctags -R /usr/lib/include
        - Obrovské soubory, lepší skok na manuálovou stránku
        - Shift+K
* Skok na definici
    :tag jméno funkce        lze zadat i regulárním výrazem
     g+Levé tlačítko myši    nefunkční v terminálu
     Ctrl+Levé tlačítko myši nefunkční v terminálu
     Ctrl+]                  ve vizuálním režimu podobné :tag
* Návrat zpět
    - Ctrl+T
* Pohyb po nápovědě Vimu je řešen právě tímto způsobem

Operátory
---------
```
    c   change      změna textu (delete a následný přechod do vkládacího režimu)
    d   delete      vymazání textu
    y   yank        kopie textu do registru
    !   filter      filtrace přes externí příkaz
    >   shift right posun textu doprava o shiftwidth
    <   shift left  posun textu doleva o shiftwidth
    g~  swap case   změna malých písmen na velké a naopak
    gu  lowercase   změna na malá písmena (mínusky)
    gU  Uppercase   změna na velká písmena (verzálky)
    gq  format      zformátování textu
    g?  ROT13
    =   indent      změna zarovnání textu, buď interním algoritmem,
                    nebo pomocí externího programu definovaného v equalprg
    zf  fold        viz další slajdy
```

Pohyb po zdrojovém kódu
-----------------------
```
    %   přeskok mezi znaky definovanými volbou matchpairs
    :set matchpairs=(:),[:],{:},<:>
```

Editace zdrojového kódu (1)
---------------------------
```
    dab delete a block     (omezeno kulatými závorkam)
    dib delete inner block (omezeno kulatými závorkami)
    daB delete a Block     (omezeno složenými závorkami)
    diB delete inner Block (omezeno složenými závorkami)
    dat delete a tag       vymazání textu umístěného v párové značce
    dit delete inner tag   vymazání textu umístěného v párové značce
    cab change a block     (kulaté závorky)
    cib change inner block (kulaté závorky)
    caB change a Block     (složené závorky)
    ciB change inner Block (složené závorky)
```

Editace zdrojového kódu (2)
---------------------------
```
    =   zarovnání textu vybraného libovolnou výběrovou operací
    =aB indent a Block  kombinace operátoru = a výběru bloku mezi {}
    >   posun vybraného textu doprava o shiftwidth
    <   posun vybraného textu doleva o shiftwidth
        - lze kombinovat s Shift+V
    >>  posun jediného řádku doprava
    <<  posun jediného řádku doleva
```

Obecné moduly
-------------
    Modul netrw
        dnes standarní součást Vimu
        :Explore
        :HExplore
        vim scp://uživatel@jméno_vzdáleného_počítače/cesta
    Modul TagList
        :TlistAddFiles *.c
        :Tlist
        :TlistAddFilesRecursive .
        :Tlist
    Modul matchit.vim
    Modul NERD Tree

Překlad programů z Vimu
------------------
```
    :make   spuštění překladu
    :clist  výpis všech chybových hlášení
    :cfirst přechod na první chybu
    :clast  přechod na poslední chybu
    :cp     přechod na předchozí chybu
    :cn     přechod na následující chybu
    :set makeprg=javac\ %
```

Vim a jazyky C/C++
------------------
* c.vim
    - Komentáře
    - Šablony
    - Překlady
    - Spouštění
    - Ideální si zobrazit menu

Vim a jazyky C/C++
------------------
    - ctags
    - cscope
        :cscope add cscope.out
    :cs show
        výpis propojení mezi Vimem a utilitou cscope
    :cs f f stdio.h
        nalezení souboru specifikovaného ve třetím parametru
    :cs f t xyzzy
        nalezení textu uvnitř řetězců (nikde jinde)
    :cs f g test
        nalezení definice funkce test (skok na začátek definice)
    :cs f d main
        zjištění, které funkce se volají z funkce main
    :cs f c fclose
        zjištění, odkud se volá funkce fclose

Vim a jazyky C/C++
------------------
    - Formátování zdrojového kódu (C, C++, Java)
        :set shiftwidth=???
        :set cindent
        :set cinoptions
        fN  úroveň posunutí otevírací levé závorky { pod jménem funkce
        :N  úroveň odsazení větví case/default v konstrukci switch-case
        =N  odsazení příkazu/příkazů za klíčovým slovem case/default
        bN  odsazení příkazu break v konstrukci switch-case
        hN  podobné volbě =N, ale platné pro klíčová slova public atd. (C++)

Vim a jazyky C/C++
------------------
    - Speciální nastavení pro Makefile
        augroup __makefile__
        au!
        au BufRead,BufNewFile Makefile set noexpandtab
        augroup END

Omnicompletion
--------------
    Ctrl+X Ctrl+L
        nalezení a doplnění celého (shodného) řádku,
        užitečné především pro konfiguračních soubory
    Ctrl+X Ctrl+N
        doplnění slova, které se nalézá v aktuálně
        editovaném souboru
    Ctrl+X Ctrl+I
        podobné Ctrl+N, ovšem prohledávají se i všechny vkládané (included) soubory
    Ctrl+X Ctrl+K
        podobné Ctrl+N, ovšem slova se hledají v souborech
        specifikovaných pomocí konfiguračního parametru dictionary
    Ctrl+X Ctrl+T
        podobné Ctrl+T, ovšem slova se hledají v souborech
        specifikovaných pomocí konfiguračního parametru thesaurus

Omnicompletion
--------------
    Ctrl+X Ctrl+]
        vyhledávání v seznamu značek
    Ctrl+X Ctrl+F
        doplnění názvu souboru a/nebo cesty, postačuje například zadat text ~/ za
        nímž následuje klávesová zkratka Ctrl+X Ctrl+F a zobrazí se výpis
        souborů v domácím adresáři
    Ctrl+X Ctrl+D
        vyhledání definice makra a doplnění jména tohoto makra
    Ctrl+X Ctrl+U
        zavolání funkce zadané v konfiguračním parametru completefunc, které se předá právě editovaný text
    Ctrl+X Ctrl+O
        vyvolání omni completion

Vim a Java
----------
augroup __java__
au!
au BufReadPre,BufNewFile *.java set fileencodings=utf-8 fileencoding=utf-8 encoding=utf-8
au BufRead,BufNewFile *.java set tw=0 foldmethod=indent cindent
au BufRead,BufNewFile *.java set tabstop=4 expandtab
au BufRead,BufNewFile *.java set foldmethod=syntax foldclose=all foldnestmax=1
au BufRead,BufNewFile *.java set guioptions=
au BufRead,BufNewFile *.java syn region myFold start="{" end="}" transparent fold
au BufRead,BufNewFile *.java noremap <Tab> >>
au BufRead,BufNewFile *.java so ~/javabrowser.vim
au BufRead,BufNewFile *.java noremap ,c O/**<CR>*<CR>*/<Esc>
au BufRead,BufNewFile *.java inoremap ,p * @param<Space>
augroup END

Vim a Java
----------
    Modul JavaBrowser
        Enter   přeskok kurzoru na definici metody/atributu
        o   dtto, ale otevře se nové okno
        +   rozbalení podstromu
        -   zabalení podstromu
        *   rozbalení celého stromu
        x   skrytí či zobrazení okna se zdrojovým kódem

Vim a assembler
---------------
augroup __asm__
au!
au BufRead,BufNewFile *.asm set tw=0 nowrap
au BufRead,BufNewFile *.asm noremap <C-F9> :!nasm -f bin % -o output.com -l output.lst<CR>
au BufRead,BufNewFile *.asm noremap <F9> :!start output.com<CR>
augroup END

Vim a Lua
---------
* lua-support.vim a.k.a. Lua-IDE
    - Šablony (soubory s nimi lze upravovat)
* Luaref
    - Kompletní referenční příručka ve formátu Vim helpu!

Vim a Clojure
-------------
* Slime for Vim
    - Využívá screen a posílání příkazů do běžícího REPLu
    - Jednoduché a přitom velmi snadno použitelné (kompletní IDE :-)
* Vimclojure

Vim a XML
---------
* Modul xml.vim
    - http://www.vim.org/scripts/script.php?script_id=301
    - Uzavírání tagů, kompletace tagů, ...
:%!xmllint --format -
:'<,'>!xmllint --format -
:map =. :%!xmllint --format - <cr>

Vim a HTML
----------
* Taktéž lze použít xml.vim
```
" Settings for HTML files {{{
"*********************************************************************
augroup __html__
au!
au BufRead,BufNewFile *.html set spell spelllang=cs spellfile=~/temp/cs.iso-8859-2.add iskeyword=@,48-57,_,128-255
au BufReadPre,BufNewFile *.html set fileencodings=utf-8 fileencoding=utf-8 encoding=utf-8
au BufRead,BufNewFile *.html set tw=0 linebreak
au BufRead,BufNewFile *.html imap ,x &times;
au BufRead,BufNewFile *.html imap ,pi &pi;
au BufRead,BufNewFile *.html imap ,phi &phi;
au BufRead,BufNewFile *.html imap ,sp &nbsp;
au BufRead,BufNewFile *.html imap ,tt <tt></tt><C-O>F<
au BufRead,BufNewFile *.html imap ,tb <tt>
au BufRead,BufNewFile *.html imap ,te </tt>
au BufRead,BufNewFile *.html imap ,ii <i></i><C-O>F<
au BufRead,BufNewFile *.html imap ,ee <em></em><C-O>F<
au BufRead,BufNewFile *.html imap ,ib <i>
au BufRead,BufNewFile *.html imap ,ie </i>
au BufRead,BufNewFile *.html imap ,bb <strong></strong><C-O>F<
au BufRead,BufNewFile *,html imap ,be </strong>
au BufRead,BufNewFile *.html imap ,uu <u></u><C-O>F<
au BufRead,BufNewFile *.html imap ,ub <u>
au BufRead,BufNewFile *.html imap ,ue </u>
au BufRead,BufNewFile *.html imap ,h1 <h1></h1><C-O>F<
au BufRead,BufNewFile *.html imap ,h2 <h2></h2><C-O>F<
au BufRead,BufNewFile *.html imap ,h3 <h3></h3><C-O>F<
au BufRead,BufNewFile *.html imap ,h4 <h4></h4><C-O>F<
au BufRead,BufNewFile *.html imap ,h5 <h5></h5><C-O>F<
au BufRead,BufNewFile *.html imap ,h6 <h6></h6><C-O>F<
au BufRead,BufNewFile *.html imap ,br <br />
au BufRead,BufNewFile *.html vmap <C-I> omaomb<esc>`bi</i><esc>`ai<i><esc>
au BufRead,BufNewFile *.html vmap <C-E> omaomb<esc>`bi</em><esc>`ai<em><esc>
au BufRead,BufNewFile *.html vmap <C-B> omaomb<esc>`bi</strong><esc>`ai<strong><esc>
au BufRead,BufNewFile *.html vmap <C-T> omaomb<esc>`bi</tt><esc>`ai<tt><esc>
au BufRead,BufNewFile *.html vmap <C-U> omaomb<esc>`bi</u><esc>`ai<u><esc>
au BufRead,BufNewFile *.html vmap <C-A> omaomb<esc>`bi</a><esc>`ai<a href=""><esc>
au BufRead,BufNewFile *.html vmap <C-P> omaomb<esc>`ba</p><esc>`ai<p><esc>
augroup END
```

Režim diff
----------
* vim -d test_old.c test_new.c
* vim -d test.c ../test-sources/
* Příkazy
    [c skok na začátek předchozího bloku se změnami
    ]c skok na začátek následujícího bloku se změnami
    dp přenos změny do druhého souboru
    do opak předchozího příkazu – získání změny
    :diffupdate tento příkaz provede nové vyhodnocení
       rozdílů mezi oběma

Editace binárních souborů
-------------------------
* Editace binárních souborů velmi obtížná
* Mnoho programátorů preferuje hexa editory
* xxd
* Příklad použití pro soubory *.class
augroup Binary_Java_Class
    au!
    au BufReadPre   *.class let &bin=1
    au BufReadPost  *.class if &bin | %!xxd -g1
    au BufReadPost  *.class set ft=xxd | endif
    au BufWritePre  *.class if &bin | %!xxd -g1 -r
    au BufWritePre  *.class endif
    au BufWritePost *.class if &bin | %!xxd -g1
    au BufWritePost *.class set nomod | endif
augroup END

Editace binárních souborů
-------------------------
0000000: ca fe ba be 00 00 00 32 00 0f 0a 00 03 00 0c 07  .......2........
0000010: 00 0d 07 00 0e 01 00 06 3c 69 6e 69 74 3e 01 00  ........<init>..
0000020: 03 28 29 56 01 00 04 43 6f 64 65 01 00 0f 4c 69  .()V...Code...Li
0000030: 6e 65 4e 75 6d 62 65 72 54 61 62 6c 65 01 00 04  neNumberTable...
0000040: 6d 61 69 6e 01 00 16 28 5b 4c 6a 61 76 61 2f 6c  main...([Ljava/l
0000050: 61 6e 67 2f 53 74 72 69 6e 67 3b 29 56 01 00 0a  ang/String;)V...
0000060: 53 6f 75 72 63 65 46 69 6c 65 01 00 09 54 65 73  SourceFile...Tes
0000070: 74 2e 6a 61 76 61 0c 00 04 00 05 01 00 04 54 65  t.java........Te
0000080: 73 74 01 00 10 6a 61 76 61 2f 6c 61 6e 67 2f 4f  st...java/lang/O
0000090: 62 6a 65 63 74 00 21 00 02 00 03 00 00 00 00 00  bject.!.........
00000a0: 02 00 01 00 04 00 05 00 01 00 06 00 00 00 1d 00  ................
00000b0: 01 00 01 00 00 00 05 2a b7 00 01 b1 00 00 00 01  .......*........
00000c0: 00 07 00 00 00 06 00 01 00 00 00 01 00 09 00 08  ................
00000d0: 00 09 00 01 00 06 00 00 00 19 00 00 00 01 00 00  ................
00000e0: 00 01 b1 00 00 00 01 00 07 00 00 00 06 00 01 00  ................
00000f0: 00 00 03 00 01 00 0a 00 00 00 02 00 0b           .............

Změna obarvení zdrojových kódů
------------------------------
* Jaké barvy dokáže zobrazit váš terminál?
    :source $VIMRUNTIME/syntax/colortest.vim
* Převod zdrojového kódu na HTML
    :source $VIMRUNTIME/syntax/2html.vim

Příklad obarvení - tyto slajdy :-)
----------------------------------
augroup __ascii__
  au!
  au BufRead,BufNewFile *.txt syn match odrazka1 "^\%d9654.*"
  au BufRead,BufNewFile *.txt syn match odrazka2 "^    .*""
  au BufRead,BufNewFile *.txt syn match odrazka3 "^        .*"
  au BufRead,BufNewFile *.txt syn match nadpis "^[A-Z].*"
  au BufRead,BufNewFile *.txt hi odrazka1 ctermfg=lightgreen guifg=#e0ffe0
  au BufRead,BufNewFile *.txt hi odrazka2 ctermfg=yellow   guifg=yellow
  au BufRead,BufNewFile *.txt hi odrazka3 ctermfg=lightcyan  guifg=#e0e0ff
  au BufRead,BufNewFile *.txt hi nadpis   ctermfg=white  guifg=white
augroup END

Další příklad obarvení - logo Vimu
----------------------------------
augroup __logo__
  au BufRead,BufNewFile vim.logo syn match zeleny_ctverec "+"
  au BufRead,BufNewFile vim.logo syn match ide "[#m\"]"
  au BufRead,BufNewFile vim.logo syn match okraj "[\\|/'_]"
  au BufRead,BufNewFile vim.logo hi  zeleny_ctverec ctermfg=lightgreen guifg=lightgreen
  au BufRead,BufNewFile vim.logo hi  okraj          ctermfg=white      guifg=white
  au BufRead,BufNewFile vim.logo hi  ide            ctermfg=yellow     guifg=yellow
  au BufRead,BufNewFile vim.logo hi  normal guifg=gray
augroup END

Mapování kláves
---------------
    au BufRead,BufNewFile *.java noremap <F10> :JavaBrowser<CR>
    au BufRead,BufNewFile *.java inoremap <F10> <Esc>:JavaBrowser<CR>
    iabb Amaroute Amaurote

Caps Lock namísto ESC
---------------------
    xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'

Vimscript
---------
* Opět viz způsob zobrazení těchto slajdů
.
let g:slides=readfile("list.txt")
let g:index = 0
.
function! GotoFirstSlide()
    let g:index = 0
endfunction
.
function! GotoLastSlide()
    let g:index = len(g:slides) - 1
endfunction
.
function! BeforeFirstSlide()
    return g:index < 0
endfunction
.
function! AfterLastSlide()
    return g:index >= len(g:slides)
endfunction
.
function! ShowNextSlide()
    let g:index += 1
    if AfterLastSlide()
        call GotoFirstSlide()
    endif
    call ShowActualSlide()
endfunction
.
function! ShowPrevSlide()
    let g:index -= 1
    if BeforeFirstSlide()
        call GotoLastSlide()
    endif
    call ShowActualSlide()
endfunction
.
function! ShowFirstSlide()
    call GotoFirstSlide()
    call ShowActualSlide()
endfunction
.
function! ShowLastSlide()
    call GotoLastSlide()
    call ShowActualSlide()
endfunction
.
function! ShowActualSlide()
    execute "edit" g:slides[g:index]
endfunction
.
function! StatusLine()
    return "Slide " . (1+g:index) . "/" . len(g:slides) . " : " . g:slides[g:index]
endfunction
.
" Hot keys
map <PageUp>   :call ShowPrevSlide()<cr>
map <PageDown> :call ShowNextSlide()<cr>
map <Home>     :call ShowFirstSlide()<cr>
map <End>      :call ShowLastSlide()<cr>
.
" Setup
set statusline=%!StatusLine()
.
" Would be better to show status line even if only one window is displayed
set laststatus=2
:call ShowFirstSlide()

Odkazy
------
    www.vim.org
    vim.wikia.com/wiki/Vim_Tips_Wiki

```
      _____________________
     < Děkuji za pozornost >
      ---------------------
       \
        \   \_\_    _/_/
         \      \__/
                (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
     
```
