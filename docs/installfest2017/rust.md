# Programovací jazyk Rust

* Autor    Pavel Tišnovský, Red Hat
* Email    <ptisnovs 0x40 redhat 0x2e com>
* Datum    2017-02-28
* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2017/rust.html](https://tisnik.github.io/presentations/installfest2017/rust.html)
* Zdrojový kód prezentace ve formátu Markdown:
    - [https://github.com/tisnik/presentations/blob/master/installfest2017/rust.md](https://github.com/tisnik/presentations/blob/master/installfest2017/rust.md)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/installfest2017/Rust/rust.txt](https://github.com/tisnik/presentations/blob/master/installfest2017/Rust/rust.txt)

## Obsah přednášky

* Charakteristické rysy Rustu
* Rust a C/C++
* Základ syntaxe
* Datové typy
* Zajímavé prvky jazyka
* Přístup k OO v Rustu
* Správa paměti
* Vlákna
* Správce balíčků (Cargo)

## Charakteristické rysy Rustu

* Multiparadigmatický jazyk
    - Funcionální rysy
    - Imperativní
    - Má některé OO rysy (ne však systém tříd)
* Dostupný pro všechny „zajímavé“ systémy
    - Linux, (Free)BSD, OS X, Windows
* Používaný na velkém množství architektur procesorů
    - i686, x86-64, ARMv6/v7 (32), AArch64, MIPS, PowerPC, S390
    - Bare Cortex-M0, M0+, M1, M4(F), M7(F)
        - bare = bez OS, jen core library
    - (připravuje se i MSP430 - 16bit MCU!)
    - [Platform Support (1)](https://forge.rust-lang.org/platform-support.html)
    - [Platform Support (2)](https://doc.rust-lang.org/nightly/rustc/platform-support.html)
* Současná verze používá LLVM backend
    - Možnosti pro další vylepšování překladu
    - (dovoluje i WebAssembly přes Emscripten)
* Cíle
    - Bezpečné aplikace
    - Paralelní běh částí aplikace
    - Výkon srovnatelný s C a C++ (i pro nové prvky jazyka)
    - Překladač s rozumným chybovým hlášením
* Poučení z chyb, které najdeme například v C/C++
    - (=, string, ptr, makrosystém)

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

## Rust a C/C++

(D, Go, Nimrod...)
* Syntaxe Rustu jen částečně odvozena od C/C++
* Využití existujícího „ekosystému“
    - Použití již hotových C knihoven
        - Foreign Function Interface (FFI)
    - C++ knihovny
        - Stále ještě problematické
* C ⇒ Rust
    - [Project Corrode](https://github.com/jameysharp/corrode)

## Chybová hlášení překladače

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
vs:

Generate the longest error message in C++
http://tinyurl.com/longest-error-message

## Základ syntaxe

* Funkce
* Proměnné
* Struktury
* Řídicí konstrukce

## Datové typy

* Primitivní datové typy
    - bool
    - char (Unicode!)
    - i8..i64, u8..u64
    - isize, usize
    - f32, f64
    - Pole (array)
    - slice (pohled na jinou strukturu)
    - N-tice (tuple)
    - str (UTF-8, interně ukazatel na data + délka)
* Homogenní struktury
    - Vektor
* Záznamy
* Funkce

## Zajímavé prvky jazyka

* Neměnitelné hodnoty
    - Výchozí modifikátor
    - Lze změnit pomocí „mut“
* Rozsah (range)
* Řídicí struktury
    - Vrací hodnotu
* Anonymní funkce
* Funkce vyššího řádu
    - map
    - filter
    - take
    - take_while
    - fold
    - Nekonečné sekvence
* Pattern matching
* Makra
* Unsafe bloky

## Základ syntaxe

```rust
// začínáme - funkce main()
fn main() {
    println!("Hello world!");
}
```

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

```rust
// měnitelná proměnná
// specifikace typu proměnné
// programová smyčka while
fn main() {
    let mut i: i8 = 0;
    while i < 200 {
        println!("pocitadlo: {}", i);
        i = i + 1;
    }
}
```

```rust
// smyčka typu for-each a typ range
fn main() {
    for i in 1..10 {
        println!("pocitadlo: {}", i)
    }
}
```

```rust
// smyčka typu for-each pro pole
fn main() {
    let array = [1, 2, 3, 4];
.
    for i in array.iter().rev() {
        println!("{}", i);
    }
}
```

```rust
// konstrukce "if" ve funkci výrazu
fn if_expression(value:i32) {
    let value_type =
        if value < 0 {
            "zaporna"
        } else {
            if value == 0 {
                "nulova"
            } else {
                "kladna"
            }
        };
    println!("Hodnota {} je {}", value, value_type);
}

fn main() {
    if_expression(0);
    if_expression(10);
    if_expression(-10);
}
```

```rust
// návratové typy funkcí
fn foo() -> i32 {
    42
}

fn bar(argument: i32) -> i32 {
    return argument * 2;
}

fn baz(argument: i32) -> i32 {
    argument * 2
}

fn main() {
    println!("{}", foo());
    println!("{}", bar(21));
    println!("{}", baz(21));
}
```

```rust
// příklad použití map() + anonymní funkce
fn main() {
    let sequence = 0..10;
    let squares = sequence.map(|x| x * x);
    for n in squares {
        println!("{}", n);
    }
}
```

```rust
// explicitní specifikace datového typu
fn main() {
    let sequence = -10..10;
    let squares = sequence.map(|x: i32| x * x);
    for n in squares {
        println!("{}", n);
    }
}
```

```rust
// nekonečné sekvence a práce s nimi
fn main() {
    let iter1 = 1..;
    let iter2 = iter1.filter(|x| x % 2 == 0);
    let iter3 = iter2.take(10);
    let suma  = iter3.fold(0, |sum, x| sum + x);
    println!("sum = {}", suma);
}
```

```rust
// faktoriály
fn main() {
    for n in 1..10 {
        let fact = (1..n + 1).fold(1, |prod, x| prod * x);
        println!("{}! = {}", n, fact);
    }
}
```

```rust
// anonymní funkce jsou "hodnotou"
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

```rust
// passing by value or reference
fn mutate_variable(arg1: i32, arg2: &mut i32) {
    println!("mutation ...");
    let x = arg1 * 2;
    *arg2 = x;
}

fn print_variables(arg1: i32, arg2: i32) {
    println!("function print_variables()");
    println!("Variable1: {}", arg1);
    println!("Variable2: {}", arg2);
}

fn pass_by_reference(arg1: &i32, arg2: &i32) {
    println!("function pass_by_reference()");
    println!("Variable1: {}", *arg1);
    println!("Variable2: {}", *arg2);
}

fn main() {
    let variable1 = 1;
    let mut variable2 = 1;
    print_variables(variable1, variable2);
    pass_by_reference(&variable1, &variable2);
    mutate_variable(variable1, &mut variable2);
    print_variables(variable1, variable2);
    pass_by_reference(&variable1, &variable2);
}
```

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

## OOP v Rustu

Vlastnictví objektů
    Reference
    Sémantika „move“
    Sémantika „copy“
Traity
    Kombinace trait+struktura+metody
Konstruktory a destruktory
    Trait „Drop“
    Přetěžování operátorů
        Přetížení = implementace traitu
Generické funkce

//
struct Complex {
    real: f32,
    imag: f32,
}
//
fn print_complex(c: Complex) {
    println!("complex number: {}+{}i", c.real, c.imag);
}
//
fn main() {
    let c1 = Complex { real:1.0, imag:2.0 };
    print_complex(c1);
    // nelze, vlastnictví přesunuto do print_complex
    let c2 = c1;
    print_complex(c2);
}

// copy trait
#[derive(Copy, Clone)]
struct Complex {
    real: f32,
    imag: f32,
}
//
fn print_complex(c: Complex) {
    println!("complex number: {}+{}i", c.real, c.imag);
}
//
fn main() {
    let c1 = Complex { real: 1.0, imag: 2.0 };
    print_complex(c1);
    let c2 = c1;
    print_complex(c2);
}

// metody
struct Complex {
    real: f32,
    imag: f32,
}
//
impl Complex {
    // konstruktor volany Complex::new(real, imag)
    fn new(real: f32, imag: f32) -> Complex {
        Complex { real: real, imag: imag }
    }
    // konstruktor volany Complex::zero()
    fn zero() -> Complex {
        Complex { real: 0.0, imag: 0.0 }
    }
//
    fn abs(&self) -> f32 {
        (self.real * self.real + self.imag * self.imag).sqrt()
    }
//
    fn print(&self) {
        println!("complex number: {}+{}i", self.real, self.imag);
    }
//
    fn add(&self, c:&Complex) -> Complex {
        Complex {
            real: self.real + c.real,
            imag: self.imag + c.imag,
        }
    }
}
//
fn main() {
    let c1 = Complex { real: 3.0, imag: 4.0 };
    c1.print();
    println!("absolute value: {}", c1.abs());
}

// deklarace traitu
trait Print {
    fn print(&self);
}
// nase datova struktura
struct Complex {
    real: f32,
    imag: f32,
}
// implementace traitu pro datovou strukturu
impl Print for Complex {
    fn print(&self) {
        println!("complex number: {}+{}i", self.real, self.imag);
    }
}

// genericka datova struktura
struct Complex<T> {
    real: T,
    imag: T,
}
// lze pouzit
let c1 = Complex { real: 10, imag: 20 };
let c2 = Complex { real: 10.1, imag: 20.1 };
let c3 = Complex { real: 10.2f64, imag: 20.2f64 };
let c4 = Complex { real: true, imag: false };

// pretizeni operatoru +
use std::ops::Add;
-
struct Complex {
    real: f32,
    imag: f32,
}
-
impl Complex {
-
    fn new(real: f32, imag: f32) -> Complex {
        Complex { real: real, imag: imag }
    }
-
    fn print(&self) {
        println!("complex number: {:}+{:}i", self.real, self.imag);
    }
}
-
impl Add for Complex {
-
    type Output = Complex;
-
    fn add(self, right: Complex) -> Self::Output {
        Complex {
            real: self.real + right.real,
            imag: self.imag + right.imag,
        }
    }
-
}
-
fn main() {
    let c1 = Complex::new(1.0, 1.0);
    let c2 = Complex::new(3.0, 4.0);
    c1.print();
    c2.print();
    let c3 = c1 + c2;
    c3.print();
}


## Správa paměti

* Zásobník versus halda
* Box
* Rc
* Arc
* Pole a vektory
    slice

Box
---
* Alokace objektu na haldě
* „Obaluje“ vlastní objekt (číslo, strukturu, pole)
* Trait Deref - snadný přístup k obalenému objektu
* Hlídání životnosti objektu i ukazatele
* Nemůže být NULL/nil

fn main() {
    let x = Box::new(42);
    println!("{}", x);
}
//
let c = Box::new(Complex::new(1.0, 2.0));

// deref
fn print_complex(c: Box<Complex>) {
    println!("Complex number: {:}+{:}i", c.real, c.imag);
}

Rc
--
* Počítání referencí
* Rc::clone()
* Pokud čítač dosáhne nuly, je Rc i objekt jím vlastněný zrušen
* Automatická dereference (Deref trait)

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

Arc
---
* Taktéž počítání referencí, ovšem atomické
* Arc::clone()
* Deref trait

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

## Pole

* V Rustu považováno za primitivní datový typ
* Dva typy konstruktorů
* Zjištění délky pole za běhu programu
* Přístup k prvkům přes indexy
* Indexy začínají od nuly (C-like  × Fortran, Lua)
* „Slice polí“ (efektivní operace)

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

## Vektory

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

## „Slice“ polí a vektorů

fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[2..6];
    for i in array2.iter() {
        println!("{}", i);
    }
}
//
fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[5..];
    for i in array2.iter() {
        println!("{}", i);
    }
}
//
fn main() {
    let vector = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("vector has {} items", vector.len());
    let slice = &vector[3..7];
    println!("slice has {} items", slice.len());
}

## Vlákna

fn main() {
    println!("Starting");
    for i in 1..10 {
        thread::spawn(move || {
            println!("Hello from a thread #{}", i);
        });
    }
    println!("Stopping");
}

## Testy

#[test]
fn ok_test() {
}
.
#[test]
fn failure() {
    assert!(false);
}

## Typ „Option“

fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x / y)
    } else {
        None
    }
}
//
fn main() {
    let z1 = div(2, 1);
    println!("{:?}", z1);
//
    let z2 = div(2, 0);
    println!("{:?}", z2);
}

## Typ „Result“

fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x / y)
    } else {
        Err("Divide by zero!")
    }
}
//
fn main() {
    let z1 = div(2, 1);
    println!("{:?}", z1);
//
    let z2 = div(2, 0);
    println!("{:?}", z2);
}

fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x / y)
    } else {
        Err("Divide by zero!")
    }
}
//
fn print_div_result(result: Result<i32, &'static str>) {
    match result {
        Ok(value)  => println!("value: {}", value),
        Err(error) => println!("error: {}", error),
    }
}
//
fn main() {
    let z1 = div(2, 1);
    print_div_result(z1);
//
    let z2 = div(2, 0);
    print_div_result(z2);
}

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

## Cargo.toml

[package]
name = "projectXYZ"
version = "0.1.0"
authors = ["Pepa z depa <pepa@installfest.cz>"]
.
[dependencies]
rand = "0.3.14"

## Použití nástroje Cargo

$ cargo build
    Compiling project1 v0.1.0 (file:///home/tester/temp/project1)
    Finished debug [unoptimized + debuginfo] target(s) in 0.37 secs
.
$ cargo build
    Finished debug [unoptimized + debuginfo] target(s) in 0.0 secs

$ cargo run
    Finished debug [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/project1`
Hello, world!

## Použití nástroje Cargo

$ cargo test
   Compiling project1 v0.1.0 (file:///home/tester/temp/project1)
    Finished debug [unoptimized + debuginfo] target(s) in 0.43 secs
     Running target/debug/project1-b888664ab405e319
.
running 0 tests
.
test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured

## Použití nástroje Cargo

$ cargo install
   Compiling libc v0.2.17
   Compiling rand v0.3.14
   Compiling projectXYZ v0.1.0 (file:///home/tester/temp/projectXYZ)
    Finished release [optimized] target(s) in 5.88 secs
  Installing /home/tester/.cargo/bin/projectXYZ
warning: be sure to add `/home/tester/.cargo/bin` to your PATH to be able to run the installed binaries

