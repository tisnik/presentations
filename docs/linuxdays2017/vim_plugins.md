Vim a pluginy
--------------------------------
* Globální instalace do $VIMRUNTIME/
    - `echo $VIMRUNTIME`
* Lokální instalace do `~/.vim`
* Problémy při větším množství pluginů
    - Sdílené adresáře autoload, doc, spell, syntax...
    - Podobné instalaci balíčků pro Linux :-)
    - A stejné řešení - správce pluginů
    - Vim Pathogen
    - Všechny balíčky ve `~/.vim/bundle` ve vlastních adresářích

Vim Pathogen
--------------------------------
* Popis
    - http://www.vim.org/scripts/script.php?script_id=2332
* Instalace a nastavení adresářů
    - `mkdir -p ~/.vim/autoload ~/.vim/bundle`
    - `curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim`
* Úprava `.vimrc`
    - `execute pathogen#infect()`
* Když se nebude zobrazovat dokumentace
    - `call pathogen#helptags()`
* Když to nepomůže
    - `set nocompatible` dříve než `execute pathogen#infect()` !!!

Pluginy pro Vim
--------------------------------
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
