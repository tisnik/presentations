# Použití programovacího jazyka Rust na produkčním systému

* Pavel Tišnovský, Red Hat
    - `ptisnovs@redhat.com`

---

## Anotace

Jazyk Rust se stává mezi programátory stále populárnější alternativou k C++ na
straně jedné a k jazykům vybavených automatickým správcem paměti (GC) na straně
druhé.  Na této přednášce si řekneme, které vlastnosti Rustu zjednodušují jeho
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
* Alternativní řešení
* Web Assembly

---

## Požadavky na produkční jazyk v současnosti

* Korektnost programů
* Udržovatelnost
* Bezpečnost
* Stabilita ekosystému
* Dostatek vývojářů
* Nároky na systémové zdroje
    - Více RAM -> větší náklady v kontejnerizovaném světě

---

## Popularita a rozšířenost Rustu

### Popularita Rustu

* Několik různých metodik, jak popularitu měřit
    - Tiobe index
    - PYPL (PopularitY of Programming Languages)
    - OpenHub (pro zaregistrované repositáře)
    - StackOverflow (každoroční dotazníky)

![images/so1.png](images/so1.png)

![images/so2.png](images/so2.png)

![images/so3.png](images/so3.png)

### Rozšířenost Rustu

* Mnoho statistických informací
    - Můžeme jim věřit?

![images/stat_pypl.png](images/stat_pypl.png)

![images/stat_openhub.png](images/stat_openhub.png)

![]()

---

## Charakteristické rysy Rustu

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

## Charakteristické rysy Rustu

* Multiparadigmatický jazyk
    - Funcionální rysy
    - Imperativní
    - Má některé OO rysy (ne však systém tříd)
* Dostupný pro všechny „zajímavé“ systémy
    - Linux, (Free)BSD, OS X, Windows
* Používaný na velkém množství architektur procesorů
    - i686, x86-64, ARMv6/v7 (32), AArch64, MIPS, PowerPC, S390
    - RISC-V
    - Bare Cortex-M0, M0+, M1, M4(F), M7(F) bare = bez OS, jen core library
    - (dokonce i pro MSP430 - 16bit MCU!)
    - [https://forge.rust-lang.org/platform-support.html](https://forge.rust-lang.org/platform-support.html)
    - [https://doc.rust-lang.org/nightly/rustc/platform-support.html](https://doc.rust-lang.org/nightly/rustc/platform-support.html)
* Současná verze používá LLVM backend
    - Možnosti pro další vylepšování překladu (dovoluje i WebAssembly přes Emscripten i přímo)
    - [https://www.rust-lang.org/what/wasm](https://www.rust-lang.org/what/wasm)

---

## Charakteristické rysy Rustu

* Unicode řetězce (UTF-8)
* Odvození typů proměnných (type inference)
* Striktní typová kontrola
* OOP založené strukturách (struct) a traitech
    - × třídy, objekty a rozhraní
* Životní cyklus hodnot (zejména referencí)
    - (borrow)
* Bezpečná práce s objekty uloženými na zásobníku i haldě
    - NPE? co to znamená? :-)
* Sémantiky „copy“ a „move“
* Generické parametry funkcí, prvky struktur, ...
* Pattern matching
* Funkce jsou taktéž datovým typem
    - ⇒ lambdy atd.

---

## Rust versus C/C++

(D, Go, Nimrod...)
* Syntaxe Rustu jen částečně odvozena od C/C++
* Využití existujícího „ekosystému“
    - Použití již hotových C knihoven
        - Foreign Function Interface (FFI)
    - C++ knihovny
        - Stále ještě v některých případech problematické
* C ⇒ Rust
    - Project Corrode
    - [https://github.com/jameysharp/corrode](https://github.com/jameysharp/corrode)

---

## Rust versus Go

---

## Komunikace s překladačem

### Chybová hlášení překladače

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
    vs:
    ↓
Generate the longest error message in C++
[http://tinyurl.com/longest-error-message](http://tinyurl.com/longest-error-message)
```

---

## Datové typy

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

### Typ `Option`

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

### Typ `Result`

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
* Rozsah (range)
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

### Tabulka faktoriálů

```rust
fn main() {
    for n in 1..10 {
        let fact = (1..n + 1).fold(1, |prod, x| prod * x);
        println!("{}! = {}", n, fact);
    }
}
```

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

### Pattern matching


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

---

## Správa paměti

* Zásobník versus halda
* Box
* Rc
* Arc
* Pole a vektory
    - slice

### Box

* Alokace objektu na haldě
* „Obaluje“ vlastní objekt (číslo, strukturu, pole)
* Trait Deref - snadný přístup k obalenému objektu
* Hlídání životnosti objektu i ukazatele
* Nemůže být NULL/nil

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

### Rc

* Počítání referencí
* Rc::clone()
* Pokud čítač dosáhne nuly, je Rc i objekt jím vlastněný zrušen
* Automatická dereference (Deref trait)

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

### Arc

* Taktéž počítání referencí, ovšem atomické
* Arc::clone()
* Deref trait

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

### Pole

* V Rustu považováno za primitivní datový typ
* Dva typy konstruktorů
* Zjištění délky pole za běhu programu
* Přístup k prvkům přes indexy
* Indexy začínají od nuly (C-like  × Fortran, Lua)
* „Slice polí“ (efektivní operace)

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

```rust
fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[5..];
    for i in array2.iter() {
        println!("{}", i);
    }
}
```

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

## Správce balíčků (Cargo)

![images/cargo.png](images/cargo.png)


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

### Statistika (tento týden)

* [https://crates.io/](https://crates.io/)
* 4,444,104,010 downloads
* 49,047 Crates in stock

### `Cargo.toml`

* [https://doc.rust-lang.org/cargo/reference/manifest.html](https://doc.rust-lang.org/cargo/reference/manifest.html)

```
```

---

## Vybrané balíčky

* Jak vybírat?
    - Awesome Rust
    - [https://awesome-rust.com/](https://awesome-rust.com/)

### Databáze

### API

### Logging

### Tracing

### Metriky

### Benchmarks

---

## Nasazení aplikací

---

## Alternativní řešení

---

## Web Assembly

---

## Dokumentace

* Generovaná ze zdrojových kódů
* Proč?
    - Source of truth
* Markdown

---

