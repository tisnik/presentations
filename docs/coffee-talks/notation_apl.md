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
* etc.

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
* linear text - from speech where it make sense
* a lot of context everywhere!

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
    - when teaching mathematics at Harvard,
    - "Mathematical notation to express computation"
* during his work for IBM (yes, IBM!) it was translater into aprogramming language
* in 1979, Iverson received the Turing Award for his work on APL
* "A shocking brevity"
* Common idioms are to be recognized in no time
    - like quadratic formula
* later IBM discouraged customers from using it
    - (but was used a lot by many IBM departments at the same time)
    - prefer to use languages based on "methodologies"
    - basically to split design, analytics, development, and testing
    - OTOH IBM was almost never good at PL design
* btw how to made money
    - $1 for one CPU second
    - $1 for 1kB of output

![APL](images/notation_this_is_apl.png)

### Kenneth E. Iverson

* IBM Fellow, IBM, 1970
* Harry H. Goode Memorial Award, IEEE Computer Society, 1975
* Member, National Academy of Engineering (USA), 1979
* Turing Award, Association for Computing Machinery, 1979
* Computer Pioneer Award (Charter recipient), IEEE Computer Society, 1982
* Honorary doctorate, York University, 1998
* ”Meeting Ken Iversion could cause mental transformations.”

### "Array languages"

* An array:
    - rectangular collection of numbers, characters and arrays
    - arranged along zero or more axes

### APL today

* APL developers
    - any kind of engineer other than a software engineer
    - do not feel comfortable discussing "programming"
    - i.e. not visible much on SO etc.
    - they generally hate software fashion waves
    - (Dyalog CTO Morten Kromberg)
* Fintec
    - Realtime trading
* Insurance companies
* Big data processing

## Feel of APL

* Vectors
* Functions
    - monadic
    - dyadic
* Operators
    - reduce
    - scan
    - inner product
    - outer product
* Combinators ("trains")
    - atop
    - fork

## Feel of APL

* Operators (function-like)

```
      monadic               dyadic
+     identity              addition
-     negation              subtraction
×     sign                  multiplication
÷     1/x                   division
ι     counter
⌹     matrix inversion      matrix division
⍉     matrix transposition
⌽     reverse               rotation
/                           reduce
.                           inner product
◦.                          outer product
```

* Expression

```apl
1+2×3
```

* From right to left, no priorities

```apl
2×3+1
```

* Vectors

```apl
⍴ 1 2 3 4

VECTOR ← 1 2 3 4 5 6
⍴VECTOR

EMPTY_LIST ← ι0

VECTOR[3]
VECTOR[1 3 5]

'xenobiotic'[10 10 1]
```

* Vector containing 1, 2, 3, 4 .. 10

```
ι10
```

* Item-by-item operations

```apl
÷1 2 3 4 5
10÷1 2 3 4 5
```

* Reduce operator

```apl
+/ 1 2 3 4
```

* Calculate the sum of all integers ranging from 1 to 100

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

* Average

```apl
X ← 1 2 3 4 5
(+/X)÷⍴X
```

* Scan operator
    - like reduce, but returns all intermediate results

```apl
+\ 1 2 3 4 5
```

* Factorial 1! to 10!

```apl
×\⍳10
```

* Take and drop functions

```apl
list ← ι10
1 ↑ list
1 ↓ list
```

* Absolute and relative change computation

```apl
revenues ← 56 59 67 64 60 61 68 73 78 75 81 84
(1↓revenues)-(¯1↓revenues)
100×((1↓revenues)÷(¯1↓revenues))-1
```

* Matrices

```apl
4 3 ⍴ ⍳12

Mat ← 3 3 ρ ι 9
Mat[2;2]
```

* Outer product
     - very powerful operation

```apl
(⍳5)∘.×(⍳5)
(⍳5)∘.=(⍳5)
(⍳5)∘.<(⍳5)
(⍳5)∘.≥(⍳5)
```

```apl
'abcd' ∘.= 'cabbage'
+/ 'abcd' ∘.= 'cabbage'
```

### Prime number generator (step-by-step)

* Well let's start with the final not-idiomatic form

```apl
(∼R∈R∘.×R)/R←1↓⍳x
```

* Step-by-step

```apl
⍳x
R←1↓⍳x
R∘.×R
R∊R∘.×R
~R∊R∘.×R
(~R∊R∘.×R)/R
```

* Number of primes in given range

```apl
⍴(~R∊R∘.×R)/R
```

* As a function

```apl
primes←{ {(~⍵∊⍵∘.×⍵)/⍵}1↓⍳⍵}
      primes 10
2 3 5 7
```

* Tacit variant

```apl
((⊢~∘.×⍨)1↓⍳)100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

## Implementations of APL

* dyalog
* GNU APL
* ngl/apl
* NARS2000

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
* [Dyalog Modern Programming Language, Morten Kromberg, Talks at Google](https://www.youtube.com/watch?v=PlM9BXfu7UY)
* [The J Language: Consistency, Adjacency, and Solution-Oriented Programming - Tracy Harms](https://www.youtube.com/watch?v=gLULrFY2-fI)
* [Un-directed programming](https://www.sacrideo.us/un-structured-programming/)
