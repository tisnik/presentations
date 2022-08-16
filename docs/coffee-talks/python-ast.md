# Python AST

## Journey from source code to bytecode

* Source code
* Lexer
* Parser
* Compiler
* Bytecode

## Lexer

* Input
    - source code
* Output
    - sequence of tokens
 
## Parser

* Input
    - sequence of tokens
* Output
    - abstract syntax tree (AST)


## Compiler

* Input
    - abstract syntax tree (AST)
* Output
    - bytecode

## Decompiler

* Input
    - bytecode
* Output
    - readable sequence of instructions

## Set of transformations

* From one linear structure into another one
* But it is not that straightforward
* Lexer
* Parser
* Compiler

# So...

* All the steps can be called from Python itself!
* An unique opportunity to check and learn what's going on
* Transpilers
* Optimizers
* Linters
* ...

## Lexer

* Transforms source file into linear sequence of tokens


```python
```

## Parser

* Transforms linear sequence of tokens into AST


```python
```

## Compiler

* Transforms AST into linear sequence of bytecode instructions


```python
```

## Decompiler

* Emits readable version of Python bytecode


```python
```

## Links
