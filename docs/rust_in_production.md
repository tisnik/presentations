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

---

## Popularita a rozšířenost Rustu

---

## Charakteristické rysy Rustu

* Cíle
    - Bezpečné aplikace
    - Paralelní běh částí aplikace
    - Výkon srovnatelný s C a C++ (i pro nové prvky jazyka)
    - https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html
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
    - https://forge.rust-lang.org/platform-support.html
    - https://doc.rust-lang.org/nightly/rustc/platform-support.html
* Současná verze používá LLVM backend
    - Možnosti pro další vylepšování překladu (dovoluje i WebAssembly přes Emscripten i přímo)
    - https://www.rust-lang.org/what/wasm

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
    - https://github.com/jameysharp/corrode

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
http://tinyurl.com/longest-error-message
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
    Nekonečné sekvence
* Pattern matching
* Makra
* Unsafe bloky

---

### Tabulka faktoriálů

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

## Přístup k OO v Rustu

---

## Správa paměti

---

## Vlákna

---

## Testování

---

## Správce balíčků (Cargo)

---

## Vybrané balíčky

---

## Nasazení aplikací

---

## Alternativní řešení

---

## Web Assembly

---

