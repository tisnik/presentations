# Jazyk Go pro úplné začátečníky

* Autor    Pavel Tišnovský, Red Hat
* Email    <ptisnovs 0x40 redhat 0x2e com>
* Datum    2019-03-01
* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2019/go.html](https://tisnik.github.io/presentations/installfest2019/go.html)
* Zdrojový kód prezentace:
    - [https://github.com/tisnik/presentations/blob/master/installfest2019/Go/go.txt](https://github.com/tisnik/presentations/blob/master/installfest2019/Go/go.txt)


## Obsah přednášky

* Charakteristické rysy jazyka Go
* Struktura programů psaných v Go
* Klíčová slova jazyka Go
* Základní datové typy
* Uživatelské datové typy
* Operátory
* Deklarace funkcí
* Řídicí příkazy
* Reakce na chybové stavy
* Rozhraní
* Metody
* Gorutiny
* Kanály
* Balíčky

## Last minute info

* 25.2.2019 vyšla verze Go 1.12
* žádné podstatné změny v jazyku
    - nástroje
    - knihovny

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
* Pro běžné architektury
    - x86 i x86-64
    - ARMv6
    - ARMv8
* I pro ty více exotické
    - s390x
    - PowerPC64 (LE)
* Současná verze používá vlastní backend
    - + cgo

## Charakteristické rysy jazyka Go

* Cíle
    - Jednoduchost, jednoznačnost
    - Jazyk postaven na jednoduchých a známých konceptech
        - Lze začít programovat po doslova několikaminutovém tutoriálu
        - Ovšem pokročilejší vlastnosti je potřeba nastudovat
    - Bezpečné aplikace
    - Mikroslužby
    - Skripty a nástroje pro DevOps od DevOps
    - Jazyk původně pro potřeby Googlu:
        - spíše pro mladší vývojáře
        - (C/C++, Java, Python ve škole)
    - Použití pro rozsáhlejší aplikace psané velkým týmem
    - Paralelní běh částí aplikace
        - komunikace mezi paralelně běžícími částmi
    - Rozumný výpočetní výkon
        - cílem je dosáhnout výkonnosti C/C++/Fortranu
    - Rychlý překlad
        - CI/CD
        - lokální vývoj i rozsáhlých systémů

## Charakteristické rysy jazyka Go (2)

* Poučení z chyb, které najdeme například v C/C++
    - Silný typový systém
        - explicitní konverze
    - Nepoužívají se makra založená na textové substituci
    - Nepoužívají se hlavičkové soubory
    - Systém balíčků, kontrola použití balíčků
    - Bezpečná práce s pamětí (+ GC)
    - Standardizovaný framework pro testování
    - Rychlé překlady
    - Syntaktické věci: ++/-- jen postfixové a nejsou to výrazy
    - Nepoužívá se ukazatelová aritmetika tak jako v C
        - práce s ukazateli je do značné míry omezena
    - Nepoužívají se šablony
    - Nejsou podporovány výjimky (prozatím)

## Charakteristické rysy jazyka Go (3)

* Správa paměti se přenáší do runtime
* Gorutiny a kanály
    - 600k gorutin, 90% CPU
* Typový systém
    - Snadné vytváření nových typů
    - Generické datové typy
        - chystají se
        - po stabilizaci jazyka (což nastalo)
        - Go 2?
* Více imperativních rysů
    - Explicitní zápis většiny operací
* Neexistuje podpora pro generické datové typy
    - Pravděpodobně se změní v další verzi Go
* Pragmaticky zaměřený jazyk
* Prozatím nedosahuje tak vysokého výpočetního výkonu jako C

## Charakteristické rysy jazyka Go (4)

* Výsledkem překladu může být binární soubor obsahující vše potřebné
    - jednodušší distribuce
    - "DLL hell"
    - Docker atd.
    - cross překlad

## Klíčová slova jazyka Go

```
break     default      func    interface  select
case      defer        go      map        struct
chan      else         goto    package    switch
const     fallthrough  if      range      type
continue  for          import  return     var
```

## Základní datové typy

* Jednoduché datové typy
    - Pravdivostní
        - Pravdivostní typ (*boolean*)
    - Ordinální
        - Celočíselné typy (*integer*)
    - Neordinální
        - Hodnoty s plovoucí řádovou čárkou (*float*)
        - Komplexní čísla (*complex*)
* Složené datové typy
    - Řetězce (*string*)
    - Pole (*array*)
    - Řezy (*slice*)
    - Záznamy (*struct*)
    - Mapy (*map*)
* Zvláštní datové typy
    - Ukazatel (*pointer*)
    - Funkce (*function*)
    - Rozhraní (*interface*)
    - Kanál (*channel*)

## Pravdivostní typ

* `bool`
    - `true`
    - `false`
* neprovádí se automatická konverze z/na `int`!

## Celočíselné datové typy

* nezávislé na použité architektuře
* implicitní (výchozí) hodnota = 0

```
Označení          Od                   Do           Stručný popis
int8                     -128                  127  osmibitové celé číslo se znaménkem
int16                  -32768                32767  16bitové celé číslo se znaménkem
int32             -2147483648           2147483647  32bitové celé číslo se znaménkem
int64    -9223372036854775808  9223372036854775807  64bitové celé číslo se znaménkem

uint8                       0                  255  osmibitové celé číslo bez znaménka
uint16                      0                65535  16bitové celé číslo bez znaménka
uint32                      0           4294967295  32bitové celé číslo bez znaménka
uint64                      0 18446744073709551615  64bitové celé číslo bez znaménka

int                     různý                různý  odpovídá buď typu int32 nebo int64
uint                    různý                různý  odpovídá buď typu uint32 nebo uint64

byte                        0                  255  alias pro typ uint8
rune              -2147483648           2147483647  alias pro typ int32
```

## Celočíselné datové typy

```go
        var a int8 = -10
        var b int16 = -1000
        var c int32 = -10000
        var d int32 = -1000000

        var r1 rune = 'a'
        var r2 rune = '\x40'
        var r3 rune = '\n'
        var r4 rune = '\u03BB'

        var x uint8 = 10
        var y uint8 = 010
        var z uint8 = 0x10
```

## Explicitní konverze!

```go
        var a int8 = -10
        var signed_int int32 = -100000
        var unsigned_int uint32 = 100000
        var e float32 = 1e4
        var f float64 = 1.5e30

        var x int32 = int32(a)
        var y int32 = int32(e)
        var z float32 = float32(f)

        var b2 uint8 = uint8(signed_int)
        var b3 uint8 = uint8(unsigned_int)
```

## Neordinální celočíselné datové typy

* opět nezávislé na použité architektuře
* implicitní (výchozí) hodnota = 0.0

```
Označení        Rozsah hodnot                          Stručný popis
float32         -3,4×10³⁸ až 3,4×10³⁸                  číslo s jednoduchou přesností podle IEEE 754
float64         -1,7×10³⁰⁸ až 1,7×10³⁰⁸                číslo s dvojitou přesností podle IEEE 754
complex64       ± rozsah float32 + i ± rozsah float32  dvojice hodnot s jednoduchou přesností
complex128      ± rozsah float64 + i ± rozsah float64  dvojice hodnot s dvojitou přesností
```

## Neordinální celočíselné datové typy

```go
        var a float32 = -1.5
        var b float32 = 1.5
        var c float32 = 1e30
        var d float32 = 1e-30

        var x complex64 = -1.5 + 0i
        var y complex64 = 1.5 + 1000i
        var z complex64 = 1e30 + 1e30i
        var w complex64 = 1i
```

## Řetězce (string)

* Řetězce (`string`)
    - podpora Unicode
    - neměnitelné (immutable)
    - známá délka (žádné počítání indexu \0)
        - ovšem udávaná v bajtech, nikoli ve znacích.
    - `[]` - zajišťuje přístup k bajtům, ne ke znakům
    - podpora konverze na `byte[]`
  
```go
        fmt.Println("╭─────────────────────╮")
        fmt.Println("│ příλiš žλuťΩučký kůň│")
        fmt.Println("╰─────────────────────╯")
```

## Pole bajtů tvořících řetězec

```go
        var s string = "Hello\nworld!\nžluťoučký kůň"

        for i := 0; i < len(s); i++ {
                fmt.Printf("%02x ", s[i])
        }
```

## Pole (array)

* Pole (array)
    - měnitelné (mutable)
    - konstantní počet prvků
    - automatická inicializace prvků (na "nulu")
  
```go
        var a1 [10]byte
        a2 := [10]int32{1,10,2,9,3,8,4,7,5,6}
        var matice [10][10]float32
 
        for i:= 0; i < len(a1); i++ {
                a[i] = i*2;
        }
```

## Kopie polí

```go
        a2 := a1
```
 
* V Go se provede skutečná kopie pole
    - výsledkem budou dvě na sobě nezávislá pole.
* V Javě (například) se jen přiřadí reference
    - dvě proměnné budou ukazovat na stejné pole.

## Řezy (slice)

* Řezy (slice)
    - neobsahuje přímo prvky, ale pouze referencuje existující pole
    - podpora pro operaci "slice" pole[od:do]
    - podpora pro přidání prvků na konec řezu
        - interně může dojít ke realokaci pole/vytvoření nového pole
    - interní struktura
        - ukazatel na prvek pole 
        - délka (počet prvků)
        - kapacita
    - funkce
        - `make`
        - `copy`
        - `append`

## Řezy (slice)

```go
        a := [6]string{"C", "C++", "Java", "Python", "Go", "Rust"}
  
        slice1 := a[1:4]
        slice2 := a[:3]
        slice3 := a[2:]
        slice4 := a[:]
  
        fmt.Println("Array a =", a)
        fmt.Println("slice1 =", slice1)
        fmt.Println("slice2 =", slice2)
        fmt.Println("slice3 =", slice3)
        fmt.Println("slice4 =", slice4)
```

## Řezy (slice)

* Výstup bude vypadat následovně:

```
Array a = [C C++ Java Python Go Rust]
slice1 = [C++ Java Python]
slice2 = [C C++ Java]
slice3 = [Java Python Go Rust]
slice4 = [C C++ Java Python Go Rust]
```

## Uživatelsky definované datové typy

```go
package main
  
import "fmt"
  
type Id uint32
type Name string
type Surname string
  
func register_user(id Id, name Name, surname Surname) {
        fmt.Printf("Registering: %d %s %s", id, name, surname)
}
  
func main() {
        var i Id = 1
        var n Name = "Jan"
        var s Surname = "Novák"
   
        register_user(i, n, s)
}
```

## Operátor :=

* Význam operátoru :=
    - deklarace proměnné
    - určení jejího typu
    - inicializace proměnné
  
```go
        a := 10
        fmt.Println(a)
        b := "hello"
        fmt.Println(b)
        c := true
        fmt.Println(c)
```

## Operátor :=

* Pokud je proměnná deklarována
    - není ji možné v daném bloku deklarovat znovu
    - tudíž ani není možné použít znovu přiřazení :=.

## Záznamy (struct)

* Záznamy (struct)
    - viditelnost prvků podle prvního znaku názvu
    - přístup k prvkům s využitím tečkové notace

## Záznamy (struct)

type User struct {
        id      uint32
        name    string
        surname string
}
   
var user1 User
   
user1.id = 1
user1.name = "Pepek"
user1.surname = "Vyskoč"

## Tisk obsahu záznamů a inicializace záznamů

* Záznamy je možné vytisknout s využitím funkce fmt.Println:
   
fmt.Println(user1)
   
* Inicializace záznamů
  
user1 := User{
        1,
        "Pepek",
        "Vyskoč"}

## Pole záznamů

type User struct {
        id      uint32
        name    string
        surname string
}
   
var users = [3]User{
        User{
                id:      1,
                name:    "Pepek",
                surname: "Vyskoč"},
        User{
                id:      2,
                name:    "Pepek",
                surname: "Vyskoč"},
        User{
                id:      3,
                name:    "Josef",
                surname: "Vyskočil"},
}

## Mapy (map)

* Mapy (map)
    - též asociativní pole
    - (heše/hashe)
* Tzv. nil map
    - var m1 map[int]string
    - var m2 map[string]User
* Prázdná mapa
    - var m3 map[int]string = make(map[int]string)
    - m1 := make(map[int]string)
* Přidání položek do prázdné mapy
    - m3[0] = "nula"
    - m3[1] = "jedna"
    - m3[2] = "dva"
    - m3[3] = "tri"

## Operace s mapami

* Přečtení hodnoty z mapy
    - value, exist := mapa[klíč]
   
if exist {
        // prvek byl nalezen
} else {
        // prvek nebyl nalezen
}
   
* Vymazání hodnot z map
    - delete(mapa, klíč)

## Mapy a struktury (záznamy)

type User struct {
        id      uint32
        name    string
        surname string
}
   
func main() {
        m1 := make(map[string]User)
        fmt.Println(m1)
  
        m1["prvni"] = User{
                id:      1,
                name:    "Pepek",
                surname: "Vyskoč"}
  
        m1["druhy"] = User{
                id:      2,
                name:    "Josef",
                surname: "Vyskočil"}
  
        fmt.Println(m1)
}

## Mapy a struktury, klíče jako uživatelský typ

type Key struct {
        id   uint32
        role string
}
   
type User struct {
        id      uint32
        name    string
        surname string
}
   
func main() {
        m1 := make(map[Key]User)
        fmt.Println(m1)
   
        m1[Key{1, "admin"}] = User{
                id:      1,
                name:    "Pepek",
                surname: "Vyskoč"}
   
        m1[Key{2, "user"}] = User{
                id:      2,
                name:    "Josef",
                surname: "Vyskočil"}
   
        fmt.Println(m1)
}

## Zvláštní datové typy

* Ukazatel (pointer)
* Funkce (function)
* Rozhraní (interface)
* Kanál (channel)

## Ukazatele

* Vždy ukazatele na hodnotu určitého typu (ne void)
* Implicitní hodnota je `nil`
* Získání adresy unárním operátorem &
* Nepřímý přístup k hodnotě unárním operátorem *
  
var p_i *int
p_i = &i
*p_i++

## Ukazatel na strukturu

var u User
   
var p_u *User
p_u = &u
  
* Není podporován operátor ->
(*p_u).id = 10000
  
* Ovšem je podporována automatická dereference
p_u.id = 20000
  
* Ukazatel na položku záznamu
p_n = &u.name

## Konstanty

const Pi float64 = 3.1415927
const E = 2.71828
   
const z0 int = 0
const z1 = 0
  
const z2 = z0 + z1

## Funkce

* Funkce je v Go datovým typem
func funkce1(x int) int {
        return 2 * x
}
  
var a func(int) int
  
a = funkce1
  
fmt.Println(a)
fmt.Println(a(10))
  
type two_int_param_function func(int, int) int
var b two_int_param_function

## Deklarace funkcí

* Funkce bez parametrů a bez návratové hodnoty
func printHello() {
        fmt.Println("Hello world!")
}
  
* Funkce s jedním parametrem, bez návratové hodnoty
func printMessage(message string) {
        fmt.Println(message)
}
  
* Funkce s jednou návratovou hodnotou
func getMessage() string {
        return "Hello world!"
}
  
* Alternativní zápis
func getMessage() (message string) {
        message = "Hello world!"
        return
}
  
* Více návratových hodnot
func swap(a int, b int) (int, int) {
        return b, a
}

## Staticky typovaný jazyk bez zbytečného "boilerplate"

func swap(a int, b int) (int, int) {
        return b, a
}
  
        x := 1
        y := 2
        z, w := swap(x, y)

## Operátory

aritmetické                +   -   *   /   %
aritmetické s přiřazením   +=  -=  *=  /=  %=
logické                    &&  ||  !
posuny a bitové operace    <<  >>  &   |   ^   &^
-//- s přiřazením          <<= >>= &=  |=  ^=  &^=
relační                    ==  !=  <   <=  >   >=
operace s adresami         *   &
unární operátory           +   -   ^
další operátory            <-  :=

## Operátory - výběr zajímavostí

^             negace bit po bitu (podobně jako operátor ~ v C)
               
&      &=     logický součin prováděný bit po bitu
|      |=     logický součet prováděný bit po bitu
^      ^=     logická nonekvivalence prováděná bit po bitu
&^     &^=    maskování bitů vybraných zadanou maskou (operace AND NOT)
 
## Operátory/příkazy ++ a --

* Operátory ++ a --
    - Musí být zapsány jako příkaz
        - (proto se většinou ani neuvádí v tabulce operátorů)
    - Zapisují se vždy za operand

## Řídicí příkazy

* Příkaz return
* Rozhodovací konstrukce
* Programové smyčky
* Příkaz goto
* Speciální řízení (defer)

## Příkaz return

// kontrola existence return hodnota i u nedosažitelného kódu
func f2() int {
        println("f2() před příkazem return")
        return 42
        println("f2() po příkazu return")
        return -1
}

## Rozhodovací konstrukce if

func classify_char(c rune) string {
        if c >= 'a' && c <= 'z' {
                return "male pismeno"
        } else if c >= 'A' && c <= 'Z' {
                return "velke pismeno"
        } else {
                return "neco jineho"
        }
}

## Příkaz zapsaný za klíčovým slovem if

func x() string {
        if value := funkce(); value < 0 {
                return "záporná hodnota"
        } else if value > 0 {
                return "kladná hodnota"
        } else {
                return "nula"
        }
}

## Rozvětvení běhu programu s využitím konstrukce switch

switch {
}
  
switch {
default:
        println("proč jsem vlastně použil switch?")
}
   
switch {
case true:
        println("true")
case false:
        println("false")
}
  
switch {
case false:
        println("false")
case true:
        println("true")
default:
        println("default")
}
  
switch {
case false:
        println("false")
default:
        println("default")
case true:
        println("true")
}

## Porovnání výrazu s konstantami v konstrukci switch

func classify(x int) string {
        switch x {
        case 0:
                return "nula"
        case 2, 4, 6, 8:
                return "sudé číslo"
        case 1, 3, 5, 7, 9:
                return "liché číslo"
        default:
                return "?"
        }
}

## Porovnání výrazu s vypočtenými hodnotami v konstrukci switch

func classify(x int, zero_value int) string {
        switch x {
        case zero_value:
                return "nula"
        case 2, 4, 6, 8:
                return "sudé číslo"
        case 1, 3, 5, 7, 9:
                return "liché číslo"
        default:
                return "?"
        }
}

## Vyhodnocení a porovnání výsledků podmínek zapsaných ve větvích case

func classify(x int) string {
        switch {
        case x == 0:
                return "nula"
        case x%2 == 0:
                return "sudé číslo"
        case x%2 == 1:
                return "liché číslo"
        default:
                return "?"
        }
}

## Klíčové slovo fallthrough

// Pozor!!!
func classify(x int) string {
        switch x {
        case 0:
                return "nula"
        case 2:
        case 4:
        case 6:
        case 8:
                return "sudé číslo"
        case 1:
        case 3:
        case 5:
        case 7:
        case 9:
                return "liché číslo"
        default:
                return "?"
        }
        return "X"
}

## Klíčové slovo fallthrough

func classify(x int) string {
        switch x {
        case 0:
                return "nula"
        case 2:
                fallthrough
        case 4:
                fallthrough
        case 6:
                fallthrough
        case 8:
                return "sudé číslo"
        case 1:
                fallthrough
        case 3:
                fallthrough
        case 5:
                fallthrough
        case 7:
                fallthrough
        case 9:
                return "liché číslo"
        default:
                return "?"
        }
}

## Programové smyčky - klasická nekonečná smyčka

for {
        println("Diamonds are forever")
}

## Programové smyčky - podmínka uprostřed smyčky

for {
        ...
        ...
        ...
        if podmínka {
            break
        }
        ...
        ...
        ...
}

## Programové smyčky - podmínka na začátku smyčky

for i != 0 {
        println(i)
        i--
}

## Programové smyčky - počítaná smyčka

for i := 0; i < 10; i++ {
        println(i)
}

## Programové smyčky - iterace přes datové struktury

a := [...]int{1, 2, 10, -1, 42}
  
for index, item := range a {
        println(index, item)
}
  
println()
  
s := "Hello world ěščř Σ"
  
for index, character := range s {
        println(index, character)
}
  
for _, item := range a {
        println(item)
}

## Programové smyčky a mapy

var m1 map[int]string = make(map[int]string)
m1[0] = "nula"
m1[1] = "jedna"
m1[2] = "dva"
m1[3] = "tri"
m1[4] = "ctyri"
m1[5] = "pet"
m1[6] = "sest"
  
for key, val := range m1 {
        println(key, val)
}

## Break a continue (s návěštím)

Exit:
        for i := 1; i <= 10; i++ {
                for j := 1; j <= 10; j++ {
                        fmt.Printf("%3d ", i*j)
                        if i*j == 42 {
                                fmt.Println("\nodpověď nalezena!\n")
                                break Exit
                        }
                }
                fmt.Println()
        }

## Příkaz goto

func classify(x int) string {
        switch x {
        case 0:
                return "nula"
        case 2, 4, 6, 8:
                goto SudeCislo
        case 1, 3, 5, 7, 9:
                goto LicheCislo
        default:
                goto JineCislo
        }
JineCislo:
        return "?"
SudeCislo:
        return "sudé číslo"
LicheCislo:
        return "liché číslo"
}

## Používá se `goto` vůbec?

Počet použití   Klíčové slovo
189     fallthrough
550     goto
605     select
1711    chan
2346    interface
2412    default
3128    map
3443    continue
3831    import
3946    defer
4433    switch
4709    go
4929    const
5308    package
7125    else
9418    range
9885    struct
12313   type
19094   var
22073   case
29449   break
29736   for
57261   func
77351   return
111163  if

## Klíčové slovo defer

* defer - přidání volání do zásobníku
* Funkce ze zásobníku se zavolají po ukončení aktivní funkce
* Skutečné LIFO chování
* Parametry se vyhodnocují v čase volání defer
    - ne při vlastním volání funkce (to je pozdě :-)
* Funkce volaná přes defer může měnit návratové kódy "hlavní" funkce
    - musí být pojmenovány

## Speciální řízení (defer)

defer on_finish()
   
for i := 10; i >= 0; i-- {
        fmt.Printf("%2d\n", i)
}
fmt.Println("Finishing main() function")

## Speciální řízení (defer)

src, err := os.Open(srcName)
if err != nil {
        fmt.Printf("Cannot open file '%s' for reading\n", srcName)
        return
} else {
        fmt.Printf("File '%s' opened for reading\n", srcName)
}
defer closeFile(src)
// nebo přímo
defer src.Close()

## Ovlivnění návratové hodnoty přes blok defer

func funkce1() (i int) {
        i = 1
        return
}
   
func funkce2() (i int) {
        defer func() { i = 2 }()
        return 1
}
   
func funkce3() (i int) {
        defer func() { i += 2 }()
        return 1
}

## Reakce na chybové stavy

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

## Reakce na chybové stavy - panic

* Funkce se ihned ukončí
* Zavolají se případné bloky defer
* Probublávání chybového stavu
    * (defer se jakoby volá ve funkci výše)
* Zachycení funkcí recover

## Reakce na chybové stavy - panic

func copyFile(srcName, dstName string) (written int64, err error) {
        src, err := os.Open(srcName)
        if err != nil {
                panic(err)
        }
        defer closeFile(src)
 
        dst, err := os.Create(dstName)
        if err != nil {
                panic(err)
        }
        defer closeFile(dst)
 
        return io.Copy(dst, src)
}

## Rozhraní

* Datový typ
* Prázdné rozhraní interface{}
* Není zapotřebí specifikovat, jaký typ rozhraní implementuje!
* Jedna metoda (dosti časté)
type OpenShape interface {
        length() float64
}
  
* V rozhraní může být předepsáno větší množství metod:
type ClosedShape interface {
        area() float64
        perimeter() float64
}
  
* Nebo naopak nemusí být předepsána žádná metoda:
type Shape interface {
}

## Metody

* Koncept takzvaného příjemce metody
type Line struct {
        x1, y1 float64
        x2, y2 float64
}
  
func (line Line) length() float64 {
        ...
        ...
        ...
}
  
line1 := Line{x1: 0, y1: 0, x2: 100, y2: 100}
line_length := line1.length()

## Metody měnící příjemce

* Takto ne - sice se obsah line změní, ovšem jen lokálně
func (line Line) translate(dx, dy float64) {
        fmt.Printf("Translating line %v by %f %f\n", line, dx, dy)
        line.x1 += dx
        line.y1 += dy
        line.x2 += dx
        line.y2 += dy
}
* Korektní řešení (Go je v tomto případě konzistentní)
func (line *Line) translate(dx, dy float64) {
        fmt.Printf("Translating line %v by %f %f\n", *line, dx, dy)
        (*line).x1 += dx
        (*line).y1 += dy
        (*line).x2 += dx
        (*line).y2 += dy
}

## Rozhraní jako datový typ při volání funkcí

type OpenShape interface {
        length() float64
}
  
func length(shape OpenShape) float64 {
        return shape.length()
}
  
type Line struct {
        x1, y1 float64
        x2, y2 float64
}
  
func (line Line) length() float64 {
        return math.Hypot(line.x1-line.x2, line.y1-line.y2)
}
  
line1 := Line{x1: 0, y1: 0, x2: 100, y2: 100}
  
fmt.Println(line1)
  
line_length := length(line1)
fmt.Println(line_length)

## Složitější příklad

package main
  
import (
        "fmt"
        "math"
)
  
type ClosedShape interface {
        area() float64
}
  
func area(shape ClosedShape) float64 {
        return shape.area()
}
  
type Circle struct {
        x, y   float64
        radius float64
}
  
type Ellipse struct {
        x, y float64
        a, b float64
}
  
type Rectangle struct {
        x, y          float64
        width, height float64
}
  
func (rect Rectangle) area() float64 {
        return rect.width * rect.height
}
  
func (circle Circle) area() float64 {
        return math.Pi * circle.radius * circle.radius
}
  
func (ellipse Ellipse) area() float64 {
        return math.Pi * ellipse.a * ellipse.b
}
  
func main() {
        shapes := []ClosedShape{
                Rectangle{x: 0, y: 0, width: 100, height: 100},
                Circle{x: 0, y: 0, radius: 100},
                Ellipse{x: 0, y: 0, a: 100, b: 50}}
 
        for _, shape := range shapes {
                fmt.Println(shape)
                fmt.Println(area(shape))
                fmt.Println(shape.area())
                fmt.Println()
        }
}

## Gorutiny

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

## Kanály

* Technologie pro komunikaci mezi gorutinami
* Speciální operátory
* Kanály s kapacitou (buffery, fronty)
* Základní detekce deadlocku

## Kanály

func message(id int, channel chan int) {
        fmt.Printf("gorutina %d\n", id)
   
        // zápis libovolné hodnoty do kanálu
        channel <- 1
}
  
func main() {
        channel := make(chan int)
   
        fmt.Println("main begin")
        go message(1, channel)
   
        fmt.Println("waiting...")
   
        // blokující čtení z kanálu
        code, status := <-channel
   
        fmt.Printf("received code: %d and status: %t\n", code, status)
        fmt.Println("main end")
}

## Jednoduchá synchronizace v Go

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

## Čekání na data posílaná přes kanály

ch1 := make(chan int)
ch2 := make(chan int)
  
go worker(ch1, 1)
go worker(ch2, 2)
  
select {
case <-ch1:
        fmt.Println("Data z kanálu 1")
case <-ch2:
        fmt.Println("Data z kanálu 2")
}

## Větev default

ch1 := make(chan int)
ch2 := make(chan int)
  
go worker(ch1, 1)
go worker(ch2, 2)
  
for true {
        select {
        case <-ch1:
                fmt.Println("Data z kanálu 1")
        case <-ch2:
                fmt.Println("Data z kanálu 2")
        default:
                fmt.Println("Žádná data nejsou k dispozici")
        }
        time.Sleep(1 * time.Second)
}

## Posílání dat do workerů

ch1 := make(chan int)
  
go worker(ch1)
  
for i := 0; i < 10; i++ {
        select {
        case ch1 <- 0:
                fmt.Println("Poslána nula")
        case ch1 <- 1:
                fmt.Println("Poslána jednička")
        }
}

## Blokující zápis do kanálu

func worker(channel chan int, worker int) {
        for true {
                value, ok := <-channel
                if ok {
                        fmt.Printf("Worker %d přijal hodnotu %d\n", worker, value)
                } else {
                        fmt.Printf("Kanál je uzavřen pro workera %d\n", worker)
                }
                time.Sleep(1 * time.Second)
        }
}
   
func main() {
        ch1 := make(chan int)
   
        go worker(ch1, 1)
        go worker(ch1, 2)
   
        for i := 0; i < 10; i++ {
                select {
                case ch1 <- 0:
                        fmt.Println("Poslána nula")
                case ch1 <- 1:
                        fmt.Println("Poslána jednička")
                }
        }
}

## Kombinace čtení a zápisu v konstrukci select-case

select {
case ch1 <- 0:
        fmt.Println("Poslána nula")
case ch1 <- 1:
        fmt.Println("Poslána jednička")
case data, ok := <-ch2:
        if ok {
                fmt.Printf("Přijata data %d z kanálu 2\n", data)
        }
case data, ok := <-ch3:
        if ok {
                fmt.Printf("Přijata data %d z kanálu 3\n", data)
        }
}

## Balíčky

* klíčové slovo package 
* import balíčků přes příkaz import "název_balíčku"

## Makra v Go?

* Céčkový přístup:
    - řeší preprocesor
        #ifdef _DEBUG
        puts("something");
        #else
        puts("something else");
        #endif
* Částečně nahraditelná:
    - řeší překladač
        const debug = false
        if debug {
            fmt.Println("something")
        } else {
            fmt.Println("something else")
        }

## A samozřejmě oblíbené téma pro debaty...

* Formát zápisu programů
    - autoři Go: lepší je se soustředit na vlastní vývoj
    - Definován kanonický formát
        - gofmt
        - taby atd.:)
