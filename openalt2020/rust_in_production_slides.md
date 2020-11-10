# Použití programovacího jazyka Rust na produkčním systému

* Pavel Tišnovský, Red Hat
    - `ptisnovs@redhat.com`
* Prezentace:
    - [https://tisnik.github.io/presentations/openalt2020/rust_in_production.html](https://tisnik.github.io/presentations/openalt2020/rust_in_production.html)
* Zdrojový kód prezentace:
    - [https://github.com/tisnik/presentations/blob/master/openalt2020/rust_in_production.md](https://github.com/tisnik/presentations/blob/master/openalt2020/rust_in_production.md)

---

## Anotace

Jazyk Rust se stává mezi programátory stále populárnější alternativou k C++ na
straně jedné a k jazykům vybavených automatickým správcem paměti (GC) na straně
druhé. Na této přednášce si řekneme, které vlastnosti Rustu zjednodušují jeho
použití v produkčních systémech, které knihovny se nejčastěji používají a jak
se aplikace psané v Rustu zabezpečují.

![images/rust_logo.png](images/rust_logo.png)

---

## Obsah přednášky

* Požadavky na produkční jazyk v současnosti
* Popularita a rozšířenost Rustu
* Charakteristické rysy Rustu
* Rust versus C/C++
* Rust versus Go
* Komunikace s překladačem
* Datové typy
* Zajímavé prvky jazyka
* Přístup k OO v Rustu
* Správa paměti
* Vlákna
* Testování
* Správce balíčků (Cargo)
* Vybrané balíčky
* Nasazení aplikací
* Web Assembly
* Rozhraní s Pythonem
* Dokumentace

---

## Požadavky na produkční jazyk v současnosti

* Korektnost programů
* Udržovatelnost
* Bezpečnost
* Stabilita ekosystému
* Dostatek vývojářů
* Nároky na systémové zdroje
    - Více RAM -> větší náklady v kontejnerizovaném světě
* API a komunikace s dalšími (mikro)službami

---

![images/real_world.jpg](images/real_world.jpg)

---

## Popularita a rozšířenost Rustu

### Popularita Rustu

* Několik různých metodik, jak popularitu měřit
    - Tiobe index
    - PYPL (PopularitY of Programming Languages)
    - OpenHub (pro zaregistrované repositáře)
    - StackOverflow (každoroční dotazníky)

---

![images/so1.png](images/so1.png)

---

![images/so2.png](images/so2.png)

---

![images/so3.png](images/so3.png)

---

### Rozšířenost Rustu

* Dostupných mnoho statistických informací
    - Můžeme jim věřit?

---

![images/stat_pypl.png](images/stat_pypl.png)

---

![images/stat_openhub.png](images/stat_openhub.png)

---

![images/rust_tiobe_index.png](images/rust_tiobe_index.png)

---

## Charakteristické rysy Rustu

![images/rust_tree.png](images/rust_tree.png)

---

* Cíle
    - Bezpečné aplikace
    - Paralelní běh částí aplikace
    - Výkon srovnatelný s C a C++ (i pro nové prvky jazyka)
    - [https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html)
    - Překladač s rozumným chybovým hlášením
    - Nízkoúrovňový a současně vysokoúrovňový jazyk
* Poučení z chyb, které najdeme například v C/C++ nebo v Javě
    - (=, string, ptr, makrosystém)
    - NPE

---

![images/npe.jpg](images/npe.jpg)

* Další info
    - [Programovací jazyk Rust: náhrada C nebo slepá cesta?](https://www.root.cz/clanky/programovaci-jazyk-rust-nahrada-c-nebo-slepa-cesta/)

---

## Charakteristické rysy Rustu

* Multiparadigmatický jazyk
    - Funcionální rysy
    - Imperativní
    - Má některé OO rysy (ne však systém tříd)
* Dostupný pro všechny „zajímavé“ systémy
    - Linux, (Free)BSD, OS X, Windows

---

* Používaný na velkém množství architektur procesorů
    - i686, x86-64, ARMv6/v7 (32), AArch64, MIPS, PowerPC, S390
    - RISC-V
    - Bare Cortex-M0, M0+, M1, M4(F), M7(F) bare = bez OS, jen core library
    - (dokonce i pro MSP430 - 16bit MCU!)
    - [Platform Support (1)](https://forge.rust-lang.org/platform-support.html)
    - [Platform Support (2)](https://doc.rust-lang.org/nightly/rustc/platform-support.html)
* Současná verze používá LLVM backend
    - Možnosti pro další vylepšování překladu (dovoluje i WebAssembly přes Emscripten i přímo)
    - [https://www.rust-lang.org/what/wasm](https://www.rust-lang.org/what/wasm)
* Další info
    - [Object-Orientation in Rust](https://stevedonovan.github.io/rust-gentle-intro/object-orientation.html)

---

## Charakteristické rysy Rustu

* Unicode řetězce (UTF-8)
* Odvození typů proměnných (type inference)
* Striktní typová kontrola
* OOP založené strukturách (struct) a traitech
    - × třídy, objekty a rozhraní
* Životní cyklus hodnot (zejména referencí)
    - borrow
---

* Bezpečná práce s objekty uloženými na zásobníku i haldě
    - NPE? co to znamená? :-)
* Sémantiky „copy“ a „move“
* Generické parametry funkcí, prvky struktur, ...
* Pattern matching
* Funkce jsou taktéž datovým typem
    - ⇒ lambdy atd.

---

## Rust versus C/C++

* Syntaxe Rustu jen částečně odvozena od C/C++
* Využití existujícího „ekosystému“
    - Použití již hotových C knihoven
        - Foreign Function Interface (FFI)
    - C++ knihovny
        - Stále ještě v některých případech problematické
* C ⇒ Rust
    - [Project Corrode](https://github.com/jameysharp/corrode)

---

## Rust versus Go

![images/rust_go.png](images/rust_go.png)

* Jedná se skutečně o konkurenty?
    - Z pohledu mnoha vývojářů ano...
* Vznik zhruba ve stejný čas
    - Go veřejně představeno 2009
    - Rust 2010 (teoretické práce jsou starší)

---

* Společná snaha o vyřešení některých problémů céčka
    - bezpečná práce s paměti
        - nutnost
        - nikdo dnes nemůže přijít s jazykem
          s manuální správou paměti
    - vícevláknové aplikace
    - řetězce
    - výjimečné stavy a jejich detekce/řešení/řízení
    - problémy s textovými makry

---

* Překlad do nativního kódu
* Jazyky s podporovaným ekosystémem
    - Dnes prakticky nutnost
        - pypi
        - Ruby Gems
        - Rust: Cargo
        - Go: zpočátku přístup "jedno repo, jeden master"
        - dnes postupně vytvářený ekosystém okolo Go mod

---

### Dobře, ale jedná se SKUTEČNĚ o konkurenty?

* Rust míří na vývojáře používající C++ či D
    - Pravděpodobné směřování i do oblasti výkonnějších MCU
      (tudíž složitějších aplikací)
* Go směřuje spíše do oblasti, kde se používá Node.js, Python, Ruby
    - Webové služby
    - Síťové nástroje

---

### A samozřejmě oblíbené téma pro debaty...

* Formát zápisu programů
    - autoři Go: lepší je se soustředit na vlastní vývoj
    - Definován kanonický formát
        - gofmt
        - taby atd.:)

---

### Vybrané společné rysy jazyků Go a Rust

* Podporovány společnostmi soutěžícími na poli browserů
* Výsledkem překladu jsou nativní knihovny nebo spustitelné aplikace
* Dobré (nekryptické) chybové zprávy překladačů
    - × chyba v šabloně v C++
* Syntaxe částečně připomínající "lepší" C

---

### Porovnání Rustu a Go z hlediska vývojáře

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

---

### Rychlost přeložených aplikací

* Go - vlastní překladač
    - Self hosting
    - (bootstraping problem)
    - Rychlejší překlad
    - Méně optimalizovaný strojový kód
    - (projekt llgo - Go frontend pro LLVM)
* Rust - založen na LLVM
    - Pomalejší překlad
    - Optimalizace na úrovni dalších LLVM jazyků

---

### Více info

* [Rust vs Go in 2020](https://medium.com/@devathon_/rust-vs-go-in-2020-1d472b5ee15)
* [Go vs Rust: Which is Better and Why?](https://appinventiv.com/blog/go-vs-rust/)

---

## Některé význačné rysy Rustu

![images/rust_logo.png](images/rust_logo.png)

---

## Komunikace s překladačem

* Chybová hlášení musí být přesná a ideálně obsahovat nápovědu
* Ne všechny programovací jazyky toto dodržují
    - Generate the longest error message in C++
        - [http://tinyurl.com/longest-error-message](http://tinyurl.com/longest-error-message)

---

### Chybová hlášení překladače Rustu

```
error[E0382]: use of moved value: `c`
  --> an_example.rs:40:8
   |
39 |     funkce1(c);
   |        - value moved here
40 |     funkce2(c);
   |        ^ value used here after move
   |
   = note: move occurs because `c` has type `std::rc::Rc<Complex>`, which does not implement the `Copy` trait
```

---

### Další příklad

* Několik začátečnických chyb v programovém kódu:

```rust
fn foo(a int32) {
  println!(a)
}

fn main() {
  let x:i32 = 10
  foo(x);
}
```

---

* Výsledek běhu překladače Rustu:

![images/rust_error.png](images/rust_error.png)

---

## Datové typy

* Skalární
    - celá čísla `i8`, `u128` atd.
    - s plovoucí řádovou čárkou
    - pravdivostní
    - znak
* Složené
    - n-tice
    - pole
    - struktury
    - enum
* Odvozené
    - vektory
    - řetězce
    - ...
* Další info
    - [Rust: struktury, n-tice a vlastnictví objektů](https://www.root.cz/clanky/rust-struktury-n-tice-a-vlastnictvi-objektu/)

---

### Odvození typů

```rust
// odvození typu všech proměnných (i z)
// použití makra println!
fn main() {
    let x = 6;
    let y = 7;
    let z;
    // překladač až nyní získá informace o typu
    z = x * y;
    println!("{} * {} = {}", x, y, z);
}
```

---

### Typ `Option`

* Nahrazuje koncept `null`
* Lze použít pattern matching
* Další info
    - [Datový typ Option v programovacím jazyku Rust](https://www.root.cz/clanky/datovy-typ-option-v-programovacim-jazyku-rust/)

---

```rust
fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x / y)
    } else {
        None
    }
}

fn main() {
    let z1 = div(2, 1);
    println!("{:?}", z1);

    let z2 = div(2, 0);
    println!("{:?}", z2);
}
```

---

### Typ `Result`

* Nahrazuje koncept `null` popř. speciálních chybových hodnot
* Lze použít pattern matching
* Další info
    - [Reakce na chyby v programovacím jazyku Rust](https://www.root.cz/clanky/reakce-na-chyby-v-programovacim-jazyku-rust/)

---

```rust
fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x / y)
    } else {
        Err("Divide by zero!")
    }
}

fn main() {
    let z1 = div(2, 1);
    println!("{:?}", z1);

    let z2 = div(2, 0);
    println!("{:?}", z2);
}
```

---

### Typ `Result` a pattern matching

```rust
fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x / y)
    } else {
        Err("Divide by zero!")
    }
}

fn print_div_result(result: Result<i32, &'static str>) {
    match result {
        Ok(value)  => println!("value: {}", value),
        Err(error) => println!("error: {}", error),
    }
}

fn main() {
    let z1 = div(2, 1);
    print_div_result(z1);

    let z2 = div(2, 0);
    print_div_result(z2);
}
```

---

* Další info
    - [Rust: funkce, lambda výrazy a rozhodovací konstrukce match](https://www.root.cz/clanky/rust-funkce-lambda-vyrazy-a-rozhodovaci-konstrukce-match/)

---

### Použití typu `Result` při výpočtech

```rust
fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x / y)
    } else {
        Err("Divide by zero!")
    }
}

fn print_div_result(result: Result<i32, &'static str>) {
    match result {
        Ok(value)  => println!("value: {}", value),
        Err(error) => println!("error: {}", error),
    }
}

--

fn inc(x: i32) -> i32 {
    x + 1
}

fn main() {
    let z0 = div(0, 1);
    print_div_result(z0);
    print_div_result(z0.map(inc));
    let z2 = div(2, 0);
    print_div_result(z2);
    print_div_result(z2.map(inc));
}
```
---


### Anonymní funkce jsou hodnotami

```rust
fn main() {
    let is_odd = |x: i32| x & 1 == 1;
    //let is_even = |x: i32| !is_odd(x);
    let square = |x: i32| x*x;
    for x in 0..10 {
        println!("{}*{}={}, {} is {} number",
                 x, x, square(x), x, if is_odd(x) {"odd"} else {"even"})
    }
}
```

* Další info
    - [Rust: funkce, lambda výrazy a rozhodovací konstrukce match](https://www.root.cz/clanky/rust-funkce-lambda-vyrazy-a-rozhodovaci-konstrukce-match/)

---

### (Anonymní) funkce jsou hodnotami

```rust
fn main() {
    let is_odd = |x: i32| x & 1 == 1;
    //let is_even = |x: i32| !is_odd(x);
    let square = |x: i32| x*x;
    for x in 0..10 {
        println!("{}*{}={}, {} is {} number",
                 x, x, square(x), x, if is_odd(x) {"odd"} else {"even"})
    }
}
```

---

## Zajímavé prvky jazyka

* Neměnitelné hodnoty
    - Výchozí modifikátor
    - Lze změnit pomocí `mut`
* Rozsah (`range`)
* Řídicí struktury
    - Vrací hodnotu
* Anonymní funkce
* Funkce vyššího řádu
    - `map`
    - `filter`
    - `take`
    - `take_while`
    - `fold`
    - Nekonečné sekvence
* Pattern matching
* Makra
* Unsafe bloky

---

### Tabulka faktoriálů

* Použití anonymních funkcí a funkcí vyššího řádu

```rust
fn main() {
    for n in 1..10 {
        let fact = (1..n + 1).fold(1, |prod, x| prod * x);
        println!("{}! = {}", n, fact);
    }
}
```

---

### Nekonečné sekvence

```rust
fn main() {
    let iter1 = 1..;
    let iter2 = iter1.filter(|x| x % 2 == 0);
    let iter3 = iter2.take(10);
    let suma  = iter3.fold(0, |sum, x| sum + x);
    println!("sum = {}", suma);
}
```

---

### Pattern matching

* Je nutné uvést všechny možné větve
    - hlídáno překladačem

```rust
// matching (nejjednodušší varianta)
fn main() {
    let x: i32 = 1;
    match x {
        0 => println!("zero"),
        1 => println!("one"),
        2 => println!("two"),
        3 => println!("three"),
        _ => println!("something else"),
    }
}
```

---

### Pattern matching: složitější konstrukce

```rust
// matching, složitější ukázka
fn classify(x:i32) -> &'static str {
    match x {
        0         => "zero",
        1 | 2     => "one or two",
        3 | 4 | 5 => "from three to five",
        10 ... 20 => "from ten to twenty",
        _         => "something else",
    }
}

fn main() {
    for x in 0..10 {
        println!("{}:{}", x, classify(x))
    }
}
```

---

## Přístup k OO v Rustu

* Vlastnictví objektů
    - Reference
    - Sémantika „move“
    - Sémantika „copy“
* Traity
    - Kombinace trait+struktura+metody
* Konstruktory a destruktory
    - Trait „Drop“
    - Přetěžování operátorů
        - Přetížení = implementace traitu
* Generické funkce
* Další info
    - [Programovací jazyk Rust: metody a traity](https://www.root.cz/clanky/programovaci-jazyk-rust-metody-a-traity/)
    - [Generické typy v programovacím jazyku Rust](https://www.root.cz/clanky/genericke-typy-v-programovacim-jazyku-rust/)

---

## Správa paměti

* Zásobník versus halda
* Box
* Rc
* Arc
* Pole a vektory
    - slice
* Další info
    - [Správa paměti v programovacím jazyku Rust s počítáním referencí](https://www.root.cz/clanky/sprava-pameti-v-programovacim-jazyku-rust-s-pocitanim-referenci/)
    - [Práce s poli v programovacím jazyku Rust](https://www.root.cz/clanky/prace-s-poli-v-programovacim-jazyku-rust/)
    - [Práce s vektory v programovacím jazyku Rust](https://www.root.cz/clanky/prace-s-vektory-v-programovacim-jazyku-rust/)

---

### Box

* Alokace objektu na haldě
* „Obaluje“ vlastní objekt (číslo, strukturu, pole)
* Trait Deref - snadný přístup k obalenému objektu
* Hlídání životnosti objektu i ukazatele
* Nemůže být `NULL`/`nil`

```rust
fn main() {
    let x = Box::new(42);
    println!("{}", x);
}

let c = Box::new(Complex::new(1.0, 2.0));

// deref
fn print_complex(c: Box<Complex>) {
    println!("Complex number: {:}+{:}i", c.real, c.imag);
}
```

---

### Rc

* Počítání referencí
* `Rc::clone()`
* Pokud čítač dosáhne nuly, je Rc i objekt jím vlastněný zrušen
* Automatická dereference (`Deref` trait)

---

```rust
fn main() {
    println!("main begin");
    let c = Rc::new(Complex::new(0.0, 0.0));
    c.print();
    {
        println!("inner block begin");
        let c2 = Rc::new(Complex::new(0.0, 0.0));
        c2.print();
        {
            println!("inmost block begin");
            let c3 = Rc::new(Complex::new(0.0, 0.0));
            c3.print();
            println!("inmost block end");
        }
        println!("inner block end");
    }
    println!("main end");
}

// jeden sdílený objekt referencovaný třikrát
fn main() {
    println!("main begin");
    let c = Rc::new(Complex::new(0.0, 0.0));
    c.print();
    {
        println!("inner block begin");
        let c2 = c.clone();
        c2.print();
        {
            println!("inmost block begin");
            let c3 = c.clone();
            c3.print();
            println!("inmost block end");
        }
        println!("inner block end");
    }
    println!("main end");
}
```

---

### Arc

* Taktéž počítání referencí, ovšem atomické
    - obecně pomalejší
    - možnost přístupu z více vláken
* `Arc::clone()`
* `Deref` trait

---

```rust
fn start_threads() {
    let c = Arc::new(Complex::new(1.0, 1.0));
    for id in 0..10 {
        let owner = ComplexNumberOwner { id: id, value: c.clone() };
        // move protože objekt může přežít toto vlákno
        thread::spawn(move || {
                owner.print();
                delay(400);
        });
    }
}
```

---

### Pole

* V Rustu považováno za primitivní datový typ
* Dva typy konstruktorů
* Zjištění délky pole za běhu programu
* Přístup k prvkům přes indexy
* Indexy začínají od nuly (C-like × Fortran, Lua)
* „Slice polí“ (efektivní operace)

---

```rust
fn main() {
    let array = [10, 20, 30, 40];
    // délka pole
    println!("array has {} items", array.len());
    // range + délka pole
    for i in 0..array.len() {
        println!("item #{} = {}", i + 1, array[i]);
    }
    // for-each
    for i in array.iter() {
        println!("{}", i);
    }
}
```

---

```rust
fn main() {
    let array = [1; 10];
    // délka pole
    println!("array has {} items", array.len());
    // range + délka pole
    for i in 0..array.len() {
        println!("item #{} = {}", i + 1, array[i]);
    }
    // for-each
    for i in array.iter() {
        println!("{}", i);
    }
}
```

---

### Vektory

```rust
fn main() {
    let vector = vec![1, 2, 3, 4, 5];
    // délka vektoru
    println!("vector has {} items", vector.len());
    // range + délka pole
    for i in 0..vector.len() {
        println!("item #{} = {}", i + 1, vector[i]);
    }
    // for-each
    for item in vector.iter() {
        println!("{}", item);
    }
    // také funguje
    for item in &vector {
        println!("{}", item);
    }
}
```

---

### „Slice“ polí a vektorů

```rust
fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[2..6];
    for i in array2.iter() {
        println!("{}", i);
    }
}
```

---

```rust
fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[5..];
    for i in array2.iter() {
        println!("{}", i);
    }
}
```

---

```rust
fn main() {
    let vector = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("vector has {} items", vector.len());
    let slice = &vector[3..7];
    println!("slice has {} items", slice.len());
}
```

---

## Vlákna

* Konformní práce s vlákny velmi důležitá, zejména v současnosti

![images/Amdahl.png](images/Amdahl.png)

---

* Více info
    - [Programovací jazyk Rust: vlákna a sdílení objektů mezi nimi](https://www.root.cz/clanky/programovaci-jazyk-rust-vlakna-a-sdileni-objektu-mezi-nimi/)

```rust
use std::thread;

fn main() {
    println!("Starting");
    for i in 1..10 {
        thread::spawn(move || {
            println!("Hello from a thread #{}", i);
        });
    }
    println!("Stopping");
}
```

---

## Testování

* Problematika testování stále složitějších aplikací a systémů
* CI/CD
* Základní problém
    - čím později je chyba odhalena, tím dražší je její oprava
    - z jiného oboru:
        - triviální úprava ventilu při návrhu motoru
        - vs svolávání aut do servisu
        - vs případné žaloby v případě, že chyba způsobí nehody
* Další časté problémy dnešních aplikací
    - velký vývojářský tým
    - používá se větší množství jazyků (jak se domluvit?)
    - zákazník a jeho role při vývoji
    - někdy nejasné role (vývojář či tester?)

---

### "Pyramida" s různými typy testů

* Business část
    - Beta testy
    - Alfa testy
    - Akceptační testy
* Technologická část
    - UI testy
    - API testy
    - Integrační testy
    - Testy komponent
    - Unit testy
* Další typy testů
    - Benchmarky

---

### Jednotkové testy v Rustu

* Spouštěné přes `cargo test`

```rust
#[test]
fn ok_test() {
}

#[test]
fn failure() {
    assert!(false);
}
```

---

### Další testy

* `mockiato` - mocking
* `mockito` - HTTP mocking
* `rust-fuzz/afl.rs ` - fuzzer postavený nad AFL

---

## Správce balíčků (Cargo)

![images/cargo.png](images/cargo.png)


---

### Základní funkce

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
* Další info
    - [Cargo: správce projektů a balíčků pro programovací jazyk Rust](https://mojefedora.cz/cargo-spravce-projektu-a-balicku-pro-programovaci-jazyk-rust/)

---

### Statistika (tento týden)

* [https://crates.io/](https://crates.io/)
* 4,444,104,010 downloads
* 49,047 Crates in stock

---

### `Cargo.toml`

* De facto popis projektu/modulu
* [https://doc.rust-lang.org/cargo/reference/manifest.html](https://doc.rust-lang.org/cargo/reference/manifest.html)

```toml
[package]
name = "projectXYZ"
version = "0.1.0"
authors = ["Pepa z depa <pepa@openalt.cz>"]

[dependencies]
rand = "0.3.14"
```

---

### Použití nástroje Cargo

* První překlad a sestavení

```
$ cargo build
    Compiling project1 v0.1.0 (file:///home/tester/temp/project1)
    Finished debug [unoptimized + debuginfo] target(s) in 0.37 secs
```

* Další překlad a sestavení

```
$ cargo build
    Finished debug [unoptimized + debuginfo] target(s) in 0.0 secs
```

---

* Spuštění

```
$ cargo run
    Finished debug [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/project1`
Hello, world!
```

---

### Použití nástroje Cargo

* Jednotkové testy

```
$ cargo test
   Compiling project1 v0.1.0 (file:///home/tester/temp/project1)
    Finished debug [unoptimized + debuginfo] target(s) in 0.43 secs
     Running target/debug/project1-b888664ab405e319

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured
```

---

### Použití nástroje Cargo

* Instalace modulu

```
$ cargo install
   Compiling libc v0.2.17
   Compiling rand v0.3.14
   Compiling projectXYZ v0.1.0 (file:///home/tester/temp/projectXYZ)
    Finished release [optimized] target(s) in 5.88 secs
  Installing /home/tester/.cargo/bin/projectXYZ
warning: be sure to add `/home/tester/.cargo/bin` to your PATH to be able to run the installed binaries
```

---

## Vybrané balíčky

* Jak vybírat?
    - Awesome Rust
    - [https://awesome-rust.com/](https://awesome-rust.com/)

---

### Databáze

* `mysql-proxy-rs`
* `rust-postgres`
* `redis-rs`
* `mongo-rust-driver`

---

### ORM

* `diesel`

---

### Data processing

* `ndarray`
* Více info
    - [Rust: knihovna ndarray pro práci s n-rozměrnými poli](https://www.root.cz/clanky/rust-knihovna-ndarray-pro-praci-s-n-rozmernymi-poli/)
    - [Programovací jazyk Rust: knihovna ndarray pro práci s n-rozměrnými poli (2)](https://www.root.cz/clanky/programovaci-jazyk-rust-knihovna-ndarray-pro-praci-s-n-rozmernymi-poli-2/)
    - [Programovací jazyk Rust: knihovna ndarray pro práci s n-rozměrnými poli (dokončení)](https://www.root.cz/clanky/programovaci-jazyk-rust-knihovna-ndarray-pro-praci-s-n-rozmernymi-poli-dokonceni/)

---

### Web

* `cargo-web`
* `hyper` (HTTP client)
* `Gotham` (web framework)
* `tiny-http`
* `Iron` (založeno na konceptu middleware)
    - [https://github.com/iron/iron](https://github.com/iron/iron)

---

### API a message brokery

* `futures-jsonrpc`
* `nanomsg-rs`
* `stomp-rs`
* `rust-zmq`

---

## Nasazení aplikací

* Kontejnerizace
* Statické linkování
* Více info
    - [Linkage](https://doc.rust-lang.org/reference/linkage.html)
    - [Packaging a Rust web service using Docker](https://blog.logrocket.com/packaging-a-rust-web-service-using-docker/)

---

## Web Assembly

---

## Rozhraní s Pythonem

* Name mangling lze zakázat
* `ctypes` nebo `CFFI`
* Více info
    - [Programovací jazyk Rust: rozhraní mezi Rustem a Pythonem](https://www.root.cz/clanky/programovaci-jazyk-rust-rozhrani-mezi-rustem-a-pythonem/)

---

```rust
#[no_mangle]
pub extern fn add_integers(x: i32, y: i32) -> i32 {
    x + y
}
```

---

```python
#!/usr/bin/env python3
import ctypes
 
testlib1 = ctypes.CDLL("target/debug/libtest1.so")
 
result = testlib1.add_integers(1, 2)
print("1 + 2 = {}".format(result))
 
result = testlib1.add_integers(1.5, 2)
print("1.5 + 2 = {}".format(result))
```

---

## Dokumentace

* Generovaná ze zdrojových kódů
* Proč?
    - Source of truth
* Markdown

---

## Odkazy

* For Complex Applications, Rust is as Productive as Kotlin
  [https://ferrous-systems.com/blog/rust-as-productive-as-kotlin/](https://ferrous-systems.com/blog/rust-as-productive-as-kotlin/)
