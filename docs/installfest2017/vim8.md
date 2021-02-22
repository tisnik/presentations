# Novinky ve Vimu 8

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz>`
* Datum: 2017-02-16
* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2017/vim8.html](https://tisnik.github.io/presentations/installfest2017/vim8.html)
* Zdrojový kód prezentace ve formátu Markdown:
    - [https://github.com/tisnik/presentations/blob/master/installfest2017/vim8.md](https://github.com/tisnik/presentations/blob/master/installfest2017/vim8.md)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/installfest2017/Vim8/vim.txt](https://github.com/tisnik/presentations/blob/master/installfest2017/Vim8/vim.txt)

## Obsah přednášky

* Stručná historie verzí Vimu
* Nastavení breakindent
* Vylepšení práce se souborem `.viminfo`
* Standardní formát pluginů
* Vylepšení skriptovacího engine
* Blbinka na závěr
* Doplnění - překlad Vimu8

## Od QEDu k Vimu

```
1965   QED        řádkový editor
1971   ed         jednodušší řádkový editor, Ken Thompson, PDP-7
1975   em         „Editor for Mortals“, založen na ed
1976   ex         ed update, přímý předchůdce Vi
1976   vi         ex+new „VIsual“ mode
1987   Stevie     ST Editor for VI Enthusiasts
1988   Vim 1.0    první neoficiální verze
1990   Elvis      klon Vi s mnoha vylepšeními
1991   Vim 1.14   první oficiálně vydaná verze
```

## Stručná historie verzí Vimu

```
1991   Vim 1.14   první oficiálně vydaná verze
1992   Vim 1.22   port na Unix 
1993   Vim 2.0    Vim Improved
1994   Vim 3      horizontálně rozdělená okna, integrovaná nápověda
                  (screenshot)
1996   Vim 4      GUI
1998   Vim 5      zvýraznění syntaxe, vertikálně rozdělená okna
...               Unicode, diff mode, port na VMS, BeOS, Mac,
...               vylepšení regexpů o \{} 
2001   Vim 6      Easy Vim (používá to někdo?)
2006   Vim 7      podpora pro další skriptovací jazyky, taby
...               slovníky, omnicompletion
2016   Vim 8      viz zbytek přednášky
```

## Vim 8

## Nastavení `breakindent`

* Kombinace s `linebreak` a `wrap`
* Použití
    - (La)TeX
    - AsciiDoc
    - Markdown
    - ...

## Nastavení `breakindent` (ukázky)

1. `nowrap`
2. `wrap`
3. `wrap` + `showbreak=...`
4. `wrap` + `linebreak`
5. `wrap` + `breakindent`
6. `wrap` + `linebreak` + `breakindent`

## Vylepšení práce se souborem `.viminfo`

* `.viminfo`
    - makra (v registrech)
    - historie příkazů
    - historie vyhledávaných řetězců
    - obsah pracovních registrů
    - uživatelem definované značky (marks)
    - poslední pozice kurzoru v otevřených souborech
    - globální proměnné
* Původně: poslední instance přepsala předchozí změny
* Nové chování
    - časové značky + „merge změn“
    - užitečné ve chvíli, kdy je spuštěno více instancí Vimu

## Vylepšení práce se souborem `.viminfo`

```
# Command Line History (newest to oldest):
:q
|2,0,1487279026,,"q"
:e ~/temp/.viminfo
|2,0,1487279024,,"e ~/temp/.viminfo"
:set linebreak
|2,0,1487278557,,"set linebreak"
```

## Standardní formát pluginů

* Stávající řešení
    - Vundle
    - Pathogen
* Standardní správce balíčků
    - Struktura adresářů s balíčky
    - `~/.vim/pack`

## Struktura adresářů s balíčky

```
.
└── pack
    └── balicky
        ├── start
        │   ├── plugin1
        │   │   ├── doc
        │   │   │   └── plugin1.txt
        │   │   ├── LICENSE
        │   │   ├── plugin
        │   │   │   └── plugin1.vim
        │   │   └── README.md
        │   └── plugin2
        │       ├── doc
        │       │   └── plugin2.txt
        │       ├── LICENSE
        │       ├── plugin
        │       │   └── plugin2.vim
        │       └── README.md
        └── opt
            ├── makejob
            │   ├── doc
            │   │   └── makejob.txt
            │   ├── LICENSE
            │   ├── plugin
            │   │   └── makejob.vim
            │   └── README.md
            └── pluginZ
                ├── doc
                │   └── pluginZ.txt
                ├── LICENSE
                ├── plugin
                │   └── pluginZ.vim
                └── README.md
```

## Vylepšení skriptovacího engine

* ID oken
* Anonymní funkce (lambdy)
* Časovače
* Podpora formátu JSON
* Kanály
* Úlohy

## ID oken

```
" Funkce bude obecně vracet různá čísla:
function! PrintWindowNumbers()
    let windowNumbers = []
    windo call add(windowNumbers, winnr()) 
    for windowNumber in windowNumbers
        echo windowNumber
    endfor
endfunction
```

```
" Funkce bude pro jedno okno vždy vracet stejné ID
function! PrintWindowIDs()
    let windowIDs = []
    windo call add(windowIDs, win_getid(winnr())) 
    for windowID in windowIDs
        echo windowID
    endfor
endfunction
```

## Anonymní funkce (lambdy)

* Zápis:
    `{x,y -> x + y}`
* Otestování:
    `:echo {x,y -> x + y}(1,2)`
* Přiřazení do proměnné (pojmenování):
    `:let Fce={x,y -> x + y}`
    `:echo Fce(1,2)`
    `3`

## Funkce vyššího řádu

```
let  sequence = range(10)
echo sequence

call map(sequence, {index, value -> value * 2})
echo sequence

call map(sequence, {index, value -> value * 2})
echo sequence

let  sequence2 = filter(copy(sequence), {index, value -> value % 2 == 0})
let  sequence3 = filter(copy(sequence), {index, value -> value % 3 == 0})
echo "sequence1=" sequence
echo "sequence2=" sequence2
echo "sequence3=" sequence3
```

## Časovače

* Vytvoření časovače:
    `timer_start(interval, funcref či anonymní funkce)`
    `timer_start(interval, funcref či anonymní funkce, {'repeat':počet_opakování})`
* Periodické opakování:
    `timer_start(interval, funcref či anonymní funkce, {'repeat':-1})`

## Podpora formátu JSON

`json_encode(výraz)`
    - převod výrazu do JSON formátu, který se vrátí ve formě řetězce
`json_decode(řetězec)`
    - opak předchozí funkce, parsování řetězce s daty uloženými v JSON formátu do interních datových struktur VimScriptu
`js_encode(výraz)`
    - podobné funkci `json_encode()`, ovšem klíče nejsou umístěny v uvozovkách
`js_decode(řetězec)`
    podobné funkci `json_decode()`, ovšem při parsingu se nevyžaduje, aby byly klíče umístěny v uvozovkách

## Režimy pluginů

```
Režim        Připojení    Popis
démon        socket       proces pro více instancí Vimu
úloha (job)  socket/pipe  proces pro jednu instanci Vimu
krátká úloha socket/pipe  neběží po celou dobu existence Vimu
filtr        pipe         spouští se synchronně
```

Úlohy
-----
* Při spuštění pluginu v samosatatném procesu
    - `job_start()`   - cesta ke skriptu + options
    - `job_status()`  - "run", "fail", "dead" ...
    - `job_stop()`    - "term", "hup", "quit", ...
    - `job_channel()` - získání kanálu pro komunikaci

## Kanály

* Slouží pro komunikaci mezi Vimem a externími pluginy
* Využívají se sockety nebo pipe

```
Typ zprávy  Význam
RAW         obecný formát
NL          textová zpráva je ukončena znakem (NL)
JSON        formát JSON
JS          formát JSON s klíči odpovídajícími JavaScriptu
```

## Blbinka na závěr

Příkaz `:smile`
(ukázka)

## Doplnění - překlad Vimu8

* Prerekvizity
    - `sudo dnf install ncurses-devel`
    - `sudo apt-get install libncurses-dev`
* Stažení a rozbalení zdrojových kódů
    - `wget https://github.com/vim/vim/archive/master.zip  `
    - `unzip master.zip`
* Překlad
    - `cd vim-master`
    - `cd src/`
    - `./configure`
    - `make`

## Doplnění - překlad Vimu8

* Kontrola
    - `file vim`
    `vim: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=a4a8c0450e172314d87769e0b0ed072e164c7f82, not stripped`
    - `ls -la vim`
    `-rwxr-xr-x 1 tester tester 8904520 lis 26 22:04 vim`
    - (`strip vim` pokud vás děsí  ^^^^^^^)
* Instalace
    `sudo make install`
    `/usr/local/bin/vim`
* Pozor na nastavení `$PATH`
