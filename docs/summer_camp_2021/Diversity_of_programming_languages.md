# Diversity of programming languages

## Paradigmas

* Imperative
    - Procedural
    - Object-oriented
* Declarative
    - Functional
    - Logic
    - Dataflow
* Metaprogramming
* Array-oriented
etc.

## Domain-specific languages
* SQL
    - one of most popular languages
* array languages
    - APL, J
* pattern matching
    - regexp now used everywhere
* specialized query languages
    - GraphQL
    - jq
    - xml path
    - etc. etc.
* data flow languages
* numeric analysis
    - Matlab
    - Julia
* computational science
    - Julia
* statistic
    - R

## Abstraction level

* Levels from the real HW
    - 5   applications
    - 4½  (scripting languages, VM-based languages)
    - 4   C-like languages
    - 3   assembler
    - 2   machine code
    - 1   syscalls
    - 0   HW

## Technological differences

* Interpreters
* Compilers
* Transpilers
* "Blended" approach

## Historical view (simplified)

* FORTRAN
    - ad-hoc compiler
    - semi-procedural language
    - no truly recursive
* Algol
    - compiler based on quite good theory
    - procedural, structured
    - recursive
* Pascal, Modula
    - loosely based on Algol
    - simpler and faster one-pass compilers!

## Language popularity is based on
* language design
* syntax, semantic (usually in this order!)
* difficulty to master it
* fashion trends
* what's used in curricula (secondary schools, uni)
* positive feedback (in both directions)
* ecosystem
* quality of compiler (speed, error messages)

## Fashion trends
* functional
* spaghetti code
* structured programming
* message passing
* actor-based
* hybrid OO
* functional (again)

## Ecosystem
* some ecosystems are based on just one/two language(s)
* typical example
    - web browsers + JS (or TS)
* transpilers have to be used for other languages

## Difficulty to master it
* "number of developers doubles every five years"
    - i.e. in typical team > 50% of developers are juniors
* and they need to fight with tooling, CI/CD, databases too
* -> the easier the language is to grok, the better

## Conclusion
* there's no silver bullet
    - and very probably never be one

## It is impossible to have one language to rule them all
* vast syntax
* full of historical baggage after some time
* complicated (and buggy!) compiler
* huge manuals
* less people to master it
* problematic in large companies
* mix of low-level and high-level constructs

## Some examples of (too) complicated languages
* PL/I
    - complicated
    - incomplete
    - buggy compilers
* Algol 68
    - 3 forms of program representation!
* C++
    - incomplete compilers for a long time
    - incomprehensible error messages
 
## Counterstrike
* Go
   - designed specifically with junior developers in mind
* Python
   - w/o type specifiers and other modern specialities

## Case study - top 5 languages used in Red Hat

* C
* Python
* Java
* Go
* JavaScript

## Related presentations

* [Top 5 languages used in Red Hat](top5languages.md)
* [Go programming language](go.md)
* [Rust programming language](rust.md)
* [Python programming language](python.md)
