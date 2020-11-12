# Go vs. Rust: porovnání dvou progresivních kompilovaných jazyků
* Autor    Pavel Tišnovský, Red Hat
* Email    <ptisnovs 0x40 redhat 0x2e com>
* Datum    2018-10-07

## Obsah přednášky (1)

* Proč vlastně porovnávat Rust a Go?
* Ale jedná se SKUTEČNĚ o konkurenty?
* Charakteristické rysy Rustu
* Rust a C/C++
* Správce balíčků (Cargo)
* Charakteristické rysy Go
* Makra v Go?
* A samozřejmě oblíbené téma pro debaty...
* Vybrané společné rysy jazyků Go a Rust
* Porovnání Rustu a Go
* Proč Go?
* Proč Rust?
* Zajímavosti
* Odkazy

## Proč vlastně porovnávat Rust a Go?

* Flamewars!
    - Nejlepší forma prokrastinace je sledování fór na Rootu...

## Proč vlastně porovnávat Rust a Go?

* Jedná se skutečně o konkurenty?
    - Z pohledu mnoha vývojářů ano...
* Vznik zhruba ve stejný čas
    - Go veřejně představeno 2009
    - Rust 2010 (teoretické práce jsou starší)
* Společná snaha o vyřešení některých problémů céčka
    - bezpečná práce s paměti
        - nutnost
        - nikdo dnes nemůže přijít s jazykem
          s manuální správou paměti
    - vícevláknové aplikace
    - řetězce
    - výjimečné stavy a jejich detekce/řešení/řízení
    - problémy s textovými makry
* Překlad do nativního kódu
* Jazyky s podporovaným ekosystémem
    - Dnes prakticky nutnost
        - pypi
        - Ruby Gems
        - Rust: Cargo
        - Go: zpočátku přístup "jedno repo, jeden master"
        - dnes postupně vytvářený ekosystém (verzování?)

## Ale jedná se SKUTEČNĚ o konkurenty?

* Rust míří na vývojáře používající C++ či D
    - Pravděpodobné směřování i do oblasti výkonnějších MCU
      (tudíž složitějších aplikací)
* Go směřuje spíše do oblasti, kde se používá Node.js, Python, Ruby
    - Webové služby
    - Síťové nástroje

## Charakteristické rysy Rustu

* Multiparadigmatický jazyk
    - Funkcionální rysy
    - Imperativní
    - Má některé OO rysy (ne však systém tříd)
* Dostupný pro všechny „zajímavé“ systémy
    - Linux, (Free)BSD, macOS, Microsoft Windows
* Používaný na velkém množství architektur procesorů
    - i686, x86-64
    - MIPS, PowerPC, S390
    - ARMv6/v7 (32), AArch64
    - Cortex-A8, Cortex-A9
    - Částečně i:
        - Bare Cortex-M0, M0+, M1, M4(F), M7(F)
          bare = bez OS, jen core library
          (připravuje se i MSP430 - 16bit MCU!)
    - https://forge.rust-lang.org/platform-support.html
* Současná verze používá LLVM backend
    - Možnosti pro další vylepšování překladu
        - dovoluje i WebAssembly přes Emscripten
* Cíle
    - Bezpečné aplikace
    - Paralelní běh částí aplikace
    - Výkon srovnatelný s C a C++ (i pro nové prvky jazyka)
    - Překladač s rozumným chybovým hlášením
× Poučení z chyb, které najdeme například v C/C++
    - operátor =
    - řetězce
    - ukazatele
    - makrosystém
    - chybové stavy, výjimky

## Charakteristické rysy Rustu (2)

* Unicode řetězce (UTF-8)
* Odvození typů proměnných (type inference)
* Striktní typová kontrola
* OOP založené strukturách (struct) a traitech
    × třídy, objekty a rozhraní
* Životní cyklus hodnot (zejména ukazatelů)
    - (borrow)
* Bezpečná práce s objekty uloženými na zásobníku i haldě
    - NPE? co to znamená? :-)
* Sémantiky „copy“ a „move“
* Generické parametry funkcí, prvky struktur, ...
* Pattern matching
* Funkce jsou taktéž datovým typem
    ⇒ lambdy atd.
* Relativně malá runtime
* Zero-cost abstractions
    ⇒ sdílené do větší míry z C++

## Charakteristické rysy Rustu (3)

* Jednoduché věci se píšou jednoduše a stručně

```rust
fn main() {
    println!("Hello world!");
}
```

* × Jinde mnohdy vyžadováno příliš mnoho znalostí na začátku:

```java
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

* "Takto přesně to musíte napsat, jinak se program nepřeloží"

## Rust a C/C++

* Syntaxe Rustu jen částečně odvozena od C/C++
* Využití existujícího „ekosystému“
    * Použití již hotových C knihoven
        - Foreign Function Interface (FFI)
    * C++ knihovny
        - stále ještě problematické
* C ⇒ Rust
    Project Corrode

## Správce balíčků (Cargo)

* Vytvoření kostry nového projektu
* Nový projekt obsahuje i adresáře a soubory umožňující podporu SCM
    - Git
    - Mercurial
* Automatická kontrola, které soubory je zapotřebí přeložit
* Automatické stažení všech knihoven a jejich závislostí
* Spuštění projektu s možností předání parametrů příkazového řádku.
* Spuštění jednotkových testů
* Spuštění benchmarků
* Vyhledání knihovny v centrálním registru zaregistrovaných knihoven
* Publikování vlastního balíčku v centrálním registru (crates.io)
* Instalace aplikace

## Charakteristické rysy jazyka Go

„Less is more“
* Multiparadigmatický jazyk
    - Procedurální
    - Objekově orientovaný
    - Podpora konstrukcí pro paralelní programování
* Vznik
    - Snaha o přidání konstrukcí pro paralelní programování do C++
    - Serverové aplikace pro Google
* Dostupný pro všechny „zajímavé“ systémy
    - Linux, (Free)BSD, macOS, Microsoft Windows
* Současná verze používá vlastní backend

## Charakteristické rysy jazyka Go

* Cíle
    - Jednoduchost, jednoznačnost
    - Jazyk postaven na jednoduchých a známých konceptech
        ⇒ Lze začít programovat po doslova několikaminutovém tutoriálu
    - Bezpečné aplikace
    - Mikroslužby
    - Skripty a nástroje pro DevOps od DevOps
    - Jazyk pro potřeby Googlu:
        ⇒ spíše pro mladší vývojáře (C/C++, Java, Python ve škole)
    - Použití pro rozsáhlejší aplikace psané velkým týmem
    - Paralelní běh částí aplikace
    - Rozumný výpočetní výkon
        ⇒ cílem je dosáhnout C/C++/Fortranu

## Charakteristické rysy jazyka Go (2)

× Poučení z chyb, které najdeme například v C/C++
    - Silný typový systém
    - Nepoužívají se makra založená na textové substituci
    - Nepoužívají se hlavičkové soubory
    - Bezpečná práce s pamětí (+ GC)
    - Standardizovaný framework pro testování
    - Rychlé překlady
    - Syntaktické věci: ++/-- jen postfixové a nejsou to výrazy
    - Nepoužívá se ukazatelová aritmetika
    - Nepoužívají se šablony
    - Nejsou podporovány výjimky (prozatím)

## Charakteristické rysy jazyka Go (3)

* Správa paměti se přenáší do runtime
* Gorutiny a kanály
    - 600k gorutin, 90% CPU
* Typový systém
    - Snadné vytváření nových typů
    - Generické datové typy
        chystají se
        po stabilizaci jazyka (což nastalo)
* Více imperativních rysů
    - Explicitní zápis většiny operací
* Neexistuje podpora pro generické datové typy
    - Pravděpodobně se změní v další verzi Go
* Více pragmaticky zaměřený jazyk
* Prozatím nedosahuje tak vysokého výpočetního výkonu jako C

## Makra v Go?

* Céčkový přístup:
    - řeší preprocesor
    ```
        #ifdef _DEBUG
        puts("something");
        #else
        puts("something else");
        #endif
    ```
* Částečně nahraditelná:
    - řeší překladač
    ```
        const debug = false
        if debug {
            fmt.Println("something")
        } else {
            fmt.Println("something else")
        }
    ```

## Look and feel Go

```
func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }
    defer src.Close()

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }
    defer dst.Close()

    return io.Copy(dst, src)
}
```

## Poznámky

* Okolo podmínek nejsou závorky
* Nepovinný středník
* `nil`
* Více návratových hodnot
* Chyba je poslední navrácenou hodnotou, konvence
* Použití defer, viz další slajd
* Zkrácený zápis deklarace a inicializace lokálních proměnných
    ```
    var src, err...
    src, err := ...
    ```
* Pojmenované návratové hodnoty (nepovinné)

## Klíčové slovo defer

* defer - přidání volání do zásobníku
* Funkce ze zásobníku se zavolají po ukončení aktivní funkce
* Skutečné LIFO chování
* Parametry se vyhodnocují v čase volání defer
    - ne při vlastním voláni funkce (to je pozdě :-)
* Funkce volaná přes defer může měnit návratové kódy "hlavní" funkce
    - musí být pojmenovány

## Zpracování chybových stavů

```go
type error interface {
    Error() string
}

func div(x, y int32) (int32, error) {
        if y == 0 {
                return -1, errors.New("takto ne!")
        }
        return x / y, nil
}

func main() {
        res, err := div(10, 3)
        fmt.Println(res, err)
        res, err = div(10, 0)
        fmt.Println(res, err)
}
```

## Gorutiny

```go
func f(from string) {
    for i := 0; i < 3; i++ {
        fmt.Println(from, ":", i)
    }
}

func main() {
    f("direct")
    go f("goroutine")
    go func(msg string) {
        fmt.Println(msg)
    }("going")

    fmt.Scanln()
    fmt.Println("done")
}

func main() {
    messages := make(chan string)
    go func() { messages <- "ping" }()
    msg := <-messages
    fmt.Println(msg)
}
```

## Jednoduchá synchronizace v Go

```go
func worker(done chan bool) {
    fmt.Print("working...")
    time.Sleep(time.Second)
    fmt.Println("done")

    // ok uz jsme hotovi, posleme zpravu kanalem
    done <- true
}

func main() {
    // kanal s kapacitou == 1
    done := make(chan bool, 1)

    // asynchronni beh
    go worker(done)

    // cekame na zpravu
    <-done
}
```

## A samozřejmě oblíbené téma pro debaty...

* Formát zápisu programů
    - autoři Go: lepší je se soustředit na vlastní vývoj
    - Definován kanonický formát
        - gofmt
        - taby atd.:)

## Vybrané společné rysy jazyků Go a Rust

* Podporovány společnostmi soutěžícími na poli browserů
* Výsledkem překladu jsou nativní knihovny nebo spustitelné aplikace
* Dobré (nekryptické) chybové zprávy překladačů
    × chyba v šabloně v C++
* Syntaxe částečně připomínající "lepší" C
    - Go
        package main
        .
        import "fmt"
        .
        func main() {
            fmt.Println("hello world")
        }
    - Rust
        fn main() {
            println!("Hello world!");
        }
* Typ "slice"

## Vlákna

* Go
        go someFunction(args)
* Rust
        use std::thread;
        let handler = thread::spawn(|| {
            // 
        });
        handler.join().unwrap();

## Správa chyb

* Go
```go
func divideWith0Check(a float32, b float32) (float32, error) {
    if b == 0 {
        return 0, errors.New("divide by zero error!")
    }

    return a / b, nil
}
func main() {
    result, err := divideWith0Check(5, 4)
    if err != nil {
       log.Printf("an error occurred: %v", err)
    } else {
       log.Printf("The answer is: 5 / 4 = %f", result)
    }
}
```

* Rust
```rust
fn divide_with_0_check(a: f32, b: f32) -> Result<f32, &'static str> {
    if b == 0.0 {
        Err("divide by zero error!")
    } else {
        Ok(a / b)
    }
}
fn main() {
    match divide_with_0_check(5.0, 4.0) {
        Err(err) => println!("{}", err),
        Ok(result) => println!("5 / 4 = {}", result),
    }
}
```

## Porovnání Rustu a Go

* Vizuální porovnání programů zapsaných v Go a Rustu:
    http://rosetta.alhur.es/compare/go/rust/#

## Porovnání Rustu a Go - komunita, akceptace

```
Jazyk            Rust           Go
Adaptace         pomalejší      rychlejší
Tiobe index      #31 (0,396%)   #16 (1,081%)
Stackshare       313            2780
Stack overflow   10100          32700
GitHub           30900 *        47500 *
GitHub           5210 forků     6510 forků
SO survey        79%            66% (loved)
SO survey         8%            16% (wanted)
(most dreaded Visual Basic 6 89.9% :-)
```

## Porovnání Rustu a Go z hlediska vývojáře

```
Jazyk             Rust           Go
Přístup           moderní        konzervativní
Syntaxe           komplikovaná   jednoduchá, minimalistická
Učící křivka      menší sklon    větší sklon
Učící křivka      větší ampli.   menší amplituda
Rychlost překladu pomalejší      rychlejší
Backend           LLVM           vlastní
Linkování         static/dynamic přes -buildmode (//export!!!)
Rychlost kódu     rychlejší      pomalejší
Typový systém     rozsáhlý       bez generik
Neměnnost         explicitní     string, další přes rozhraní
Práce s pamětí    vlastnictví    GC
Detekce souběhu   ano            jen nepřímo
Závislosti        cargo          Go moduly
```
                                 
## Poznámka k souběhu

* Za běžné situace nemůže v Rustu nastat
    - Je to zajištěno modelem vlastnictví dat (ownership)
        - existuje jen jediný vlastník dat
        - toho je možné změnit pomocí move
        - vlastnictví si lze vypůjčit (borrow)
        - ovšem v tomto případě nelze vlastnictví změnit
          (forma transakce)
        - vše je řešeno v čase překladu!

## Rychlost přeložených aplikací

* Go - vlastní překladač
    - Self hosting
    - (bootstraping problem)
    - Rychlejší překlad
    - Méně optimalizovaný strojový kód
    - (projekt llgo - Go frontend pro LLVM)
* Rust - založen na LLVM
    - Pomalejší překlad
    - Optimalizace na úrovni dalších LLVM jazyků

## Rychlost přeložených aplikací

https://benchmarksgame-team.pages.debian.net/benchmarksgame/faster/rust-go.html
```
regex-redux
source  secs    mem      gz      cpu    cpu load
Rust    2.54    204,160  765     3.95   55% 30% 56% 18%
Go     28.69    407,444  802    60.43   46% 51% 68% 46%

binary-trees
source  secs    mem      gz      cpu    cpu load
Rust    3.98    165,920  721     14.61  90% 100% 90% 89%
Go     28.90    471,068  654    110.50  96% 95% 95% 97%

mandelbrot
source  secs    mem      gz      cpu    cpu load
Rust    1.75    34,176   1332    6.86   98% 98% 100% 98%
Go      5.47    31,280   905     21.73  99% 99% 99% 100%

k-nucleotide
source  secs    mem      gz      cpu    cpu load
Rust    5.34    138,504  1749    17.16  87% 100% 78% 58%
Go     15.36    148,056  1722    54.61  77% 96% 95% 88%

reverse-complement
source  secs    mem      gz      cpu    cpu load
Rust    1.61    995,100  1376    2.72   25% 81% 39% 28%
Go      4.00    824,412   611    4.15   86% 14% 5% 1%

spectral-norm
source  secs    mem      gz      cpu    cpu load
Rust    1.98    2,472    1126    7.86   100% 100% 99% 100%
Go      3.95    2,412     548   15.70   100% 99% 99% 99%

fannkuch-redux
source  secs    mem     gz      cpu     cpu load
Rust    9.60    1,752   1020    37.68   100% 96% 99% 99%
Go     17.82    1,472    900    71.03   100% 100% 100% 100%

n-body
source  secs    mem     gz      cpu     cpu load
Rust   13.31    1,768   1805    13.31   0% 0% 1% 100%
Go     21.00    1,532   1200    21.00   1% 0% 0% 100%

fasta
source  secs    mem     gz      cpu     cpu load
Rust    1.47    2,988   1906    4.97    88% 83% 90% 84%
Go      2.07    3,168   1358    5.87    39% 83% 84% 79%

pidigits
source  secs    mem     gz      cpu     cpu load
Rust    1.74    4,488   1366    1.74    1% 100% 1% 0%
Go      2.04    8,976    603    2.04    1% 0% 100% 0%
```

## Proč Go?

* Integrace s C (stávající moduly)
* Rychlá učící křivka
* Jednotná štábní kultura
* Potřeba paralelizace
* Typové kontroly
* Event-driven programy
* Nestarat se o správu paměti
* CSP (Communicating Sequential Processes)

## Proč Rust?

* Typové kontroly
* Rychlý běh programů dosahujících možností C/C++
* Nezávislost na GC a jeho vlivu na rychlost
* Možnost low-level práce (v případě potřeby)
* Nový jazyk, který se zbavil všech podivností, které
  se do ostatních jazyků dostaly za posledních > 30 let (C++)
* Bod zlomu
    - Koncepce vlastnictví objektů
* Správa paměti prakticky řešena jen v čase překladu

## Zkouška dospělosti

* Zcela IMHO
    - překlad pro DSP
        -  TI řada TMS32C.... TMS32F....
        -  Analog Devices SHARC DSP
           Super Harvard Architecture Single-Chip Compute

## A co jazyk D?

* Nechme promluvit samotného autora jazyka D
    - problém D - pomalá adaptace, prakticky žádný sex appeal
    - Go - má strategii (networking)
        ⇒ má branding
          stojí za ním silná a známá firma
    - Rust - vývojáři musí udělat mnoho práce kvůli memory managementu
        ⇒ skutečně tak řeší business problém?
        ⇒ postaven na skvělých teoretických základech

## Zajímavosti

* Rob Pike očekával, že Go začnou ve větším množství používat programátoři C++
× Ve skutečnosti se ke Go přiklánějí spíše vývojáři v Pythonu nebo Ruby

## Odkazy

* Less is exponentially more
  https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html
* Should I Rust, or Should I Go
  https://codeburst.io/should-i-rust-or-should-i-go-59a298e00ea9
