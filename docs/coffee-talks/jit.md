# Just In Time compilers

## Three possible modes how to run code

* AOT (Ahead Of Time) compilation
    - a "classic" compiler like in C and Go
* interpretation
    - usually based on bytecode interpretation
    - see our previous presentations about lexer, tokenizer, and compiler in Python
* JIT (Just In Time) compilation
    - compilation during execution (run time)
    - "dynamic" compilation
    - usually preceded by bytecode interpretation

## JIT idea is old

* LISP (McCarthy) 1960
* Smalltalk 1983
* Self
* Later abandoned and replaced by Java
    - James Gosling 1993

## Why Just In Time compilation?

* Combines the speed of compiled code with the flexibility of interpretation
* At cost of overhead of an interpreter and the additional overhead of compilation
* JIT code offers far better performance than interpreters
* In some cases offer better performance than static compilation
    - some optimizations are only feasible at run-time

## JIT types

## Links

* [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
