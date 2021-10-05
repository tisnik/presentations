# Importance of notations and the APL programming language

## Notations

* notation is a system of
    - graphics or symbols
    - characters
    - abbreviated expressions

* a collection of related symbols
    - that are each given an arbitrary meaning
    - created to facilitate structured communication
    - within a domain knowledge or field of study!

* symbols
    - mark, sign, word
    - indication
    - is understood as representing an idea, object, or relationship
    - pictorial/associative/abstract/conceptual
    - stop sign, arrow

### Why?

* human brain is excellent in recognizing patterns
* and can be train to recognize new set of patterns
* **Notation as a tool of thought**

### Examples of notations

* Music notation
* Chemistry notations (a lot of in fact)
* Chess moves notation
* Feynman diagrams
*

#### Music notation

![Music](images/notation_music.png)

#### Chemistry notation

![Chemistry](images/notation_chemistry.png)

#### Traffic

![Traffic](images/notation_traffic.jpg)

#### Math

![Math1](images/notation_math_1.png)

![Math2](images/notation_math_2.png)

![Math3](images/notation_math_3.png)

#### Chess moves notation

```
♘f3 ♞c6
♗xc6 dxc6
0-0 ♝xc3
```

## Classic programming languages

* i.e. almost all languages with some exceptions
* most are based on "1.5D" text flow
   - from left to right
   - from top to bottom
* usually just basic ASCII characters are used

### Exceptions

* Fortress
    - rendered via LaTeX
* Algol 68 Report
    - ∧, ∨
    - ×, ÷, ÷×, ÷*, %×
    - ≤, ≥, ≠, ¬=
    - →, ○, ¢, ⏨, □
    - ×:=, ÷:=, ÷×:=, ÷*:=,  %×:=
    - ¬, ↑, ↓, ⌊, ⌈, ⊥
    - ⊂, ≡, ␣, ⊃, ⎩, ⎧
* Epigram
    - "2D" blocks
    - rendered via LaTeX

### Examples

#### Algol

```algol
¢ this is a comment
real avogadro = 6.0221415⏨23
```

#### Epigram

```epigram
     (         !       (          !   (  n : Nat  !
data !---------! where !----------! ; !-----------!
     ! Nat : * )       !zero : Nat)   !suc n : Nat)
```

![Epigram1](images/notation_epigram1.png)

```
plus x y <= rec x {
  plus x y <= case x {
    plus zero y => y
    plus (suc x) y => suc (plus x y)
  }
}
```

![Epigram2](images/notation_epigram2.png)

#### Fortress

![Fortress1](images/notation_fortress1.png)

![Fortress2](images/notation_fortress2.png)

![Fortress3](images/notation_fortress3.png)



## APL programming language

* "A Programming Language"
    - impossible to come with shorter term :)

### Origins of APL

* Kenneth E. Iverson
* it was invented as new form of mathematical notation
* during his work for IBM (yes, IBM!) it was translater into aprogramming language
* in 1979, Iverson received the Turing Award for his work on APL
* "A shocking brevity"
* later IBM discouraged customers from using it
    - (but was used a lot by many IBM departments at the same time)
    - prefer to use languages based on "methodologies"
    - basically to split design, analytics, development, and testing
    - OTOH IBM was almost never good at PL design

### Kenneth E. Iverson

* IBM Fellow, IBM, 1970
* Harry H. Goode Memorial Award, IEEE Computer Society, 1975
* Member, National Academy of Engineering (USA), 1979
* Turing Award, Association for Computing Machinery, 1979
* Computer Pioneer Award (Charter recipient), IEEE Computer Society, 1982
* Honorary doctorate, York University, 1998

### "Array languages"

* An array:
    - rectangular collection of numbers, characters and arrays
    - arranged along zero or more axes

## Feel of APL

* Vector containing 1, 2, 3, 4 .. 10

```
ι10
```

* Calculate the sum of all integers ranging from 1 to 100
     - reduction operator

```apl
+/ι100
```

* Factorial computation

```apl
*/ι100
```

* Factorial function

```apl
fact←{×/⍳⍵}
```

## Links

* [APL Wiki](https://aplwiki.com/wiki/)
* [The Array Cast](https://www.arraycast.com/episodes/episode-03-what-is-an-array)
* [EnthusiastiCon 2019 – An Introduction to APL](https://www.youtube.com/watch?v=UltnvW83_CQ)
* [Dyalog](https://www.dyalog.com/)
* [Try APL!](https://tryapl.org/)
* [APL na replit](https://replit.com/languages/apl)
* [Advent of Code 2020 in APL!](https://www.youtube.com/watch?v=0RQFW6P1Tt0)
* [Python vs APL (1 Problem)](https://www.youtube.com/watch?v=APdKFJkmBbM)
* [APL Wins (vs C++, Java & Python)](https://www.youtube.com/watch?v=59vAjBS3yZM)
* [A Tour de Force of APL in 16 Expressions by Roger Hui](https://www.youtube.com/watch?v=e0rywC7-i0U)
* [Conway's Game Of Life in APL](https://www.youtube.com/watch?v=a9xAKttWgP4)
* [A List of companies that use Array Languages (J, K, APL, q)](https://github.com/interregna/arraylanguage-companies)
* [APL - one of the greatest programming languages ever](http://www.vaxman.de/publications/apl_slides.pdf)
* ["The J Programming Language" by Tracy Harms (2013)](https://www.youtube.com/watch?v=RWYkx6-L04Q)
* [Dyalog Modern Programming Language | Morten Kromberg | Talks at Google](https://www.youtube.com/watch?v=PlM9BXfu7UY)
* [The J Language: Consistency, Adjacency, and Solution-Oriented Programming - Tracy Harms](https://www.youtube.com/watch?v=gLULrFY2-fI)
