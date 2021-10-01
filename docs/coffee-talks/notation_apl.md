# Notations and the APL programming language

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

### Examples of notations

*
*
*
*
*

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

## Links

APL Wiki
https://aplwiki.com/wiki/

The Array Cast
https://www.arraycast.com/episodes/episode-03-what-is-an-array
