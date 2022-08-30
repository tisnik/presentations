# Pattern matching in Python 3.10

* Better than `switch-case` construct

## Derived from other languages

* SNOBOL
* AWK
* ML (Caml, OCaml, F#)
* Rust

## Semi-flexible

* Not all patterns are possible
    - like `"literal" + x + "literal"
    - probably in next Python version?

## Examples

### Classic approach

@ pattern-matching/abort_retry_fail_1.py

### Usage of map

@ pattern-matching/abort_retry_fail_2.py

### Match-case structure

@ pattern-matching/abort_retry_fail_3.py

### Sets for multiple inputs

@ pattern-matching/abort_retry_fail_4.py

### Or in patterns

@ pattern-matching/abort_retry_fail_5.py

### Value capture

@ pattern-matching/abort_retry_fail_6.py

### Value capture - no "response" variable

@ pattern-matching/abort_retry_fail_7.py

### Fibonacci sequence generator

@ pattern-matching/fib.py

### Factorial - basic variant

@ pattern-matching/factorial1.py

### Condition in case branch

@ pattern-matching/factorial2.py

### Type checker

@ pattern-matching/factorial3.py

### Or-branch

@ pattern-matching/factorial4.py

### Tuple-based pattern

@ pattern-matching/complex1.py

### Tuple-based pattern with conditions

@ pattern-matching/complex2.py

### Multiple words commands

@ pattern-matching/multiword_commands_1.py

### List-matcher

@ pattern-matching/multiword_commands_2.py

### Value capture (subject)

@ pattern-matching/multiword_commands_3.py

### Nested match-case

@ pattern-matching/multiword_commands_4.py

### Nested match-case + set-like condition

@ pattern-matching/multiword_commands_5.py

### Object-based pattern

@ pattern-matching/object1.py

### Object-based pattern with multiple classes

@ pattern-matching/object2.py

## WDYT?

* It's good that Python evolve?
* It is not good as Python is no longer simple language?
