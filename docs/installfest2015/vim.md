# Pluginy pro Vim

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz>`
* Datum: 2015-03-07
* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2015/vim.html](https://tisnik.github.io/presentations/installfest2015/vim.html)
* Zdrojový kód prezentace ve formátu Markdown:
    - [https://github.com/tisnik/presentations/blob/master/installfest2015/vim.md](https://github.com/tisnik/presentations/blob/master/installfest2015/vim.md)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/installfest2015/vim/vim.txt](https://github.com/tisnik/presentations/blob/master/installfest2015/vim/vim.txt)

## Vim a pluginy

* Globální instalace do `$VIMRUNTIME/`
    - `echo $VIMRUNTIME`
* Lokální instalace do `~/.vim`
* Problémy při větším množství pluginů
    - Sdílené adresáře autoload, doc, spell, syntax...
    - Podobné instalaci balíčků pro Linux :-)
    - A stejné řešení - správce pluginů
    - Vim Pathogen
    - Všechny balíčky ve `~/.vim/bundle` ve vlastních adresářích

## Vim Pathogen

* Popis
    - http://www.vim.org/scripts/script.php?script_id=2332
* Instalace a nastavení adresářů
    ```
    mkdir -p ~/.vim/autoload ~/.vim/bundle 
    curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
    ```
* Úprava .vimrc
    - `execute pathogen#infect()`
* Když se nebude zobrazovat dokumentace
    - `call pathogen#helptags()`
* Když to nepomůže
    - `set nocompatible` dříve než `execute pathogen#infect()` !!!

## Pluginy pro Vim

* Viz také:
    - http://vimawesome.com/
    - http://www.vim.org/scripts/script_search_results.php?order_by=rating
* Zajímavé pluginy
    - Vim-airline
    - Vim-colors-solarized
    - Vim-indend-guides
    - Fugitive
    - GistVim
    - NERDTree
    - BufExplorer
    - SnipMate
    - Ctrl-P
    - Match It
    - Gundo
    - TVO
    - Tabular
    - Unite
    - Neocomplete
    - Neosnippet
    - Youcompleteme (YCM)
    - Syntastic
    - vim-prism

## Vim-airline

* Stažení
    - https://github.com/bling/vim-airline
    - `wget http://www.vim.org/scripts/download_script.php?src_id=22726`
* Po instalaci do `~/.vim/bundle `
    - `:help airline`
    - `:set laststatus=2`
    - `:AirlineToggle`
    - `:AirlineRefresh`
    - `:AirlineTheme dark`
    - `:AirlineTheme wombat`
    - `:AirlineTheme jellybeans`
    - `:AirlineTheme <Tab>`

## Vim-colors-solarized

* Stažení
    - https://github.com/altercation/vim-colors-solarized
    - `git clone git://github.com/altercation/vim-colors-solarized.git`
* Po instalaci do `~/.vim/bundle`
    - `:call pathogen#helptags()`
    - `:help solarized`
    - `:colorscheme solarized`
    - `:colorscheme <Tab>`
    - `:set background=dark`
    - `:set background=light`

## Vim-indent-guides

* Indent levels, prakticky bez konfigurace
  Taby, mezery, volba barev
* Stažení
    - `git clone git://github.com/nathanaelkane/vim-indent-guides.git`
* Po instalaci do `~/.vim/bundle`
    - `:IndentGuidesEnable`
    - `:IndentGuidesDisable`
    - `:IndentGuidesToggle`
    - `:let g:indent_guides_indent_levels = 30`

## Fugitive

* Stažení
    - http://www.vim.org/scripts/script.php?script_id=2975
    - https://github.com/tpope/vim-fugitive
* Po instalaci do `~/.vim/bundle`
    - `:call pathogen#helptags()`
    - `:help fugitive`
    - `:Git cokoli`
    - `:Gstatus`
    - `:Gcommit (spousta příkazů)`
    - `:Gbrowse`
    - `:Gblame :-)`
    - `:Gvdiff`

## GistVim

* Potřebuje ke své činnosti webapi
* Stažení
    - http://www.vim.org/scripts/script.php?script_id=2423
* Po instalaci do `~/.vim/bundle`
    - `:Gist`
* Výsledek:
    - https://gist.github.com/

## Netrw

* dnes standarní součást Vimu
    - `:Explore`
    - `:HExplore`
    - (klavesa `i`, `?`)
    - `vim scp://uživatel@jméno_vzdáleného_počítače/cesta`
    - `vim ftp://jméno_vzdáleného_počítače/cesta`
    - `:NetUserPass`
    - `:e ftp://uživatel@jméno_vzdáleného_počítače/cesta`
    - `:NetrwSettings`
    - `g:netrw_ftp_cmd="ftp"`
    - `g:netrw_http_cmd="elinks"`
    - `g:netrw_sftp_cmd="sftp"`

## TagList

* Modul TagList
    - `:TlistAddFiles *.c`
    - `:Tlist`
    - `:TlistAddFilesRecursive .`
    - `:Tlist`

## Modul matchit.vim

## NERD Tree

* Stažení
    - http://www.vim.org/scripts/script.php?script_id=1658
* Po instalaci do `~/.vim/bundle`
    - `:help NERDTree`
    - `:NERDTree`
    - (potom klávesa `?`)

## NERD Commenter

* Stažení
    - http://www.vim.org/scripts/script.php?script_id=1218
* Po instalaci
    - `:echo maplocalleader`
    - `<leader>cc`
    - `<leader>cn` (nesting)
    - `<leader>c<space>` - přepíná

## Vim Commander

* Stažení
    - http://www.vim.org/scripts/script.php?script_id=808
* Po instalaci
    - `:call VimCommanderToggle()`
    - `:map` --cokoli-- `:call VimCommanderToggle()<cr>`
    - `TAB`       = Go to the other panel.
    - `F3`        = View file under cursor.
    - `F4`        = Edit file under cursor.
    - `F5`        = Copy file.
    - `F6`        = Move/rename file.
    - `F7`        = Create directory.
    - `F8/DEL`    = Remove file.
    - `F10`       = Quit VimCommander.
    - `C-R`       = Refresh panels.
    - `Backspace` = Go to parent directory.
    - `C-U`       = Exchange panels.
    - `C-Left`    = Put directory under cursor on other panel, or grab other panel's dir.
    - `C-Right`   = Same.
    - `\H`        = Show hidden files (toggle).
    - `INS`       = Select file under cursor.
    - `"+"`       = Select file by pattern.
    - `"-"`       = De-select file by pattern.
    - `S-F4`      = Edit new file.
    - `C-t`       = Previous directory.
    - `C-y`       = Next directory.

## TVO: The VIM Outliner

* Stažení
    - http://www.vim.org/scripts/script.php?script_id=517
    - http://bike-nomad.com/vim/vimoutliner.html

## Vim a jazyky C/C++

* c.vim
    - Komentáře
    - Šablony
    - Překlady
    - Spouštění
    - Ideální si zobrazit menu

## Vim a jazyky C/C++

* `ctags`
* `cscope`
    - `:cscope add cscope.out`
    - `:cs show`
        - výpis propojení mezi Vimem a utilitou cscope
    - `:cs f f stdio.h`
        - nalezení souboru specifikovaného ve třetím parametru
    - `:cs f t xyzzy`
        - nalezení textu uvnitř řetězců (nikde jinde)
    - `:cs f g test`
        - nalezení definice funkce test (skok na začátek definice)
    - `:cs f d main`
        - zjištění, které funkce se volají z funkce main
    - `:cs f c fclose`
        - zjištění, odkud se volá funkce fclose

## Vim a jazyky C/C++

* Formátování zdrojového kódu (C, C++, Java)
    - `:set shiftwidth=???`
    - `:set cindent`
    - `:set cinoptions`
    - `fN`  úroveň posunutí otevírací levé závorky { pod jménem funkce
    - `:N`  úroveň odsazení větví case/default v konstrukci switch-case
    - `=N`  odsazení příkazu/příkazů za klíčovým slovem case/default
    - `bN`  odsazení příkazu break v konstrukci switch-case
    - `hN`  podobné volbě =N, ale platné pro klíčová slova public atd. (C++)

## Vim a jazyky C/C++

    - Speciální nastavení pro Makefile
    ```
    augroup __makefile__
    au!
    au BufRead,BufNewFile Makefile set noexpandtab
    augroup END
    ```

## Omnicompletion

* Součást Vimu
    - `Ctrl+X Ctrl+L`
        - nalezení a doplnění celého (shodného) řádku,
        - užitečné především pro konfiguračních soubory
    - `Ctrl+X Ctrl+N`
        - doplnění slova, které se nalézá v aktuálně
        - editovaném souboru
    - `Ctrl+X Ctrl+I`
        - podobné `Ctrl+N`, ovšem prohledávají se i všechny vkládané (included) soubory
    - `Ctrl+X Ctrl+K`
        - podobné `Ctrl+N`, ovšem slova se hledají v souborech
        - specifikovaných pomocí konfiguračního parametru dictionary
    - `Ctrl+X Ctrl+T`
        - podobné `Ctrl+T`, ovšem slova se hledají v souborech
        - specifikovaných pomocí konfiguračního parametru thesaurus

## Omnicompletion

* Součást Vimu
    - `Ctrl+X Ctrl+]`
        - vyhledávání v seznamu značek
    - `Ctrl+X Ctrl+F`
        - doplnění názvu souboru a/nebo cesty, postačuje například zadat text ~/ za
        - nímž následuje klávesová zkratka Ctrl+X Ctrl+F a zobrazí se výpis
        - souborů v domácím adresáři
    - `Ctrl+X Ctrl+D`
        - vyhledání definice makra a doplnění jména tohoto makra
    - `Ctrl+X Ctrl+U`
        - zavolání funkce zadané v konfiguračním parametru completefunc, které se předá právě editovaný text
    - `Ctrl+X Ctrl+O`
        - vyvolání omni completion

## Vim a Java

* Modul JavaBrowser
https://github.com/vim-scripts/JavaBrowser
    - Vyžaduje `ctags`
        - `Enter`   přeskok kurzoru na definici metody/atributu
        - `o`       dtto, ale otevře se nové okno
        - `Space`   prototyp
        - `u`       update
        - `s`       sort by name
        - `q`       quit/close
        - `+`       rozbalení podstromu
        - `-`       zabalení podstromu
        - `*`       rozbalení celého stromu
        - `x`       skrytí či zobrazení okna se zdrojovým kódem

## Vim a Lua

* lua-support.vim a.k.a. Lua-IDE
    - Šablony (soubory s nimi lze upravovat)
* Luaref
    - Kompletní referenční příručka ve formátu Vim helpu!

## Vim a Clojure

VimClojure
    - http://www.vim.org/scripts/script.php?script_id=2501

* Slime for Vim
    - Využívá `screen` a posílání příkazů do běžícího REPLu
    - Jednoduché a přitom velmi snadno použitelné (kompletní IDE :-)
* Vimclojure

## Vim a XML

* Modul xml.vim
    - http://www.vim.org/scripts/script.php?script_id=301
    - Uzavírání tagů, kompletace tagů, ...
`:%!xmllint --format -`
`:'<,'>!xmllint --format -`
`:map =. :%!xmllint --format - <cr>`

