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

* Tokenized expression

```python
(1 + 2) * 3
```

* Tokenization

```python
import tokenize

with tokenize.open("expression.py") as fin:
    token_generator = tokenize.generate_tokens(fin.readline)
    for token in token_generator:
        print("{:2}  {:2}  {}".format(token.type, token.exact_type, token))
```

* Output

```
54   7  TokenInfo(type=54 (OP), string='(', start=(1, 0), end=(1, 1), line='(1 + 2) * 3\n')
 2   2  TokenInfo(type=2 (NUMBER), string='1', start=(1, 1), end=(1, 2), line='(1 + 2) * 3\n')
54  14  TokenInfo(type=54 (OP), string='+', start=(1, 3), end=(1, 4), line='(1 + 2) * 3\n')
 2   2  TokenInfo(type=2 (NUMBER), string='2', start=(1, 5), end=(1, 6), line='(1 + 2) * 3\n')
54   8  TokenInfo(type=54 (OP), string=')', start=(1, 6), end=(1, 7), line='(1 + 2) * 3\n')
54  16  TokenInfo(type=54 (OP), string='*', start=(1, 8), end=(1, 9), line='(1 + 2) * 3\n')
 2   2  TokenInfo(type=2 (NUMBER), string='3', start=(1, 10), end=(1, 11), line='(1 + 2) * 3\n')
 4   4  TokenInfo(type=4 (NEWLINE), string='\n', start=(1, 11), end=(1, 12), line='(1 + 2) * 3\n')
 0   0  TokenInfo(type=0 (ENDMARKER), string='', start=(2, 0), end=(2, 0), line='')
```

## Tokenization of code with blocks

* This is *dirty* trick!

* Tokenized expression

```python
if True:
    if False:
        if False and True:
            print("impossible")
        else:
            print("possible")
    else:
        pass
else:
    pass
```

* Tokenization

```python
import tokenize

with tokenize.open("ifs.py") as fin:
    token_generator = tokenize.generate_tokens(fin.readline)
    for token in token_generator:
        print(token)
```

* Output

```
TokenInfo(type=1  (NAME),      string='if',           start=(1, 0),  end=(1, 2),  line='if True:\n')
TokenInfo(type=1  (NAME),      string='True',         start=(1, 3),  end=(1, 7),  line='if True:\n')
TokenInfo(type=54 (OP),        string=':',            start=(1, 7),  end=(1, 8),  line='if True:\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(1, 8),  end=(1, 9),  line='if True:\n')
TokenInfo(type=5  (INDENT),    string='    ',         start=(2, 0),  end=(2, 4),  line='    if False:\n')
TokenInfo(type=1  (NAME),      string='if',           start=(2, 4),  end=(2, 6),  line='    if False:\n')
TokenInfo(type=1  (NAME),      string='False',        start=(2, 7),  end=(2, 12), line='    if False:\n')
TokenInfo(type=54 (OP),        string=':',            start=(2, 12), end=(2, 13), line='    if False:\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(2, 13), end=(2, 14), line='    if False:\n')
TokenInfo(type=5  (INDENT),    string='        ',     start=(3, 0),  end=(3, 8),  line='        if False and True:\n')
TokenInfo(type=1  (NAME),      string='if',           start=(3, 8),  end=(3, 10), line='        if False and True:\n')
TokenInfo(type=1  (NAME),      string='False',        start=(3, 11), end=(3, 16), line='        if False and True:\n')
TokenInfo(type=1  (NAME),      string='and',          start=(3, 17), end=(3, 20), line='        if False and True:\n')
TokenInfo(type=1  (NAME),      string='True',         start=(3, 21), end=(3, 25), line='        if False and True:\n')
TokenInfo(type=54 (OP),        string=':',            start=(3, 25), end=(3, 26), line='        if False and True:\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(3, 26), end=(3, 27), line='        if False and True:\n')
TokenInfo(type=5  (INDENT),    string='            ', start=(4, 0),  end=(4, 12), line='            print("impossible")\n')
TokenInfo(type=1  (NAME),      string='print',        start=(4, 12), end=(4, 17), line='            print("impossible")\n')
TokenInfo(type=54 (OP),        string='(',            start=(4, 17), end=(4, 18), line='            print("impossible")\n')
TokenInfo(type=3  (STRING),    string='"impossible"', start=(4, 18), end=(4, 30), line='            print("impossible")\n')
TokenInfo(type=54 (OP),        string=')',            start=(4, 30), end=(4, 31), line='            print("impossible")\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(4, 31), end=(4, 32), line='            print("impossible")\n')
TokenInfo(type=6  (DEDENT),    string='',             start=(5, 8),  end=(5, 8),  line='        else:\n')
TokenInfo(type=1  (NAME),      string='else',         start=(5, 8),  end=(5, 12), line='        else:\n')
TokenInfo(type=54 (OP),        string=':',            start=(5, 12), end=(5, 13), line='        else:\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(5, 13), end=(5, 14), line='        else:\n')
TokenInfo(type=5  (INDENT),    string='            ', start=(6, 0),  end=(6, 12), line='            print("possible")\n')
TokenInfo(type=1  (NAME),      string='print',        start=(6, 12), end=(6, 17), line='            print("possible")\n')
TokenInfo(type=54 (OP),        string='(',            start=(6, 17), end=(6, 18), line='            print("possible")\n')
TokenInfo(type=3  (STRING),    string='"possible"',   start=(6, 18), end=(6, 28), line='            print("possible")\n')
TokenInfo(type=54 (OP),        string=')',            start=(6, 28), end=(6, 29), line='            print("possible")\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(6, 29), end=(6, 30), line='            print("possible")\n')
TokenInfo(type=6  (DEDENT),    string='',             start=(7, 4),  end=(7, 4),  line='    else:\n')
TokenInfo(type=6  (DEDENT),    string='',             start=(7, 4),  end=(7, 4),  line='    else:\n')
TokenInfo(type=1  (NAME),      string='else',         start=(7, 4),  end=(7, 8),  line='    else:\n')
TokenInfo(type=54 (OP),        string=':',            start=(7, 8),  end=(7, 9),  line='    else:\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(7, 9),  end=(7, 10), line='    else:\n')
TokenInfo(type=5  (INDENT),    string='        ',     start=(8, 0),  end=(8, 8),  line='        pass\n')
TokenInfo(type=1  (NAME),      string='pass',         start=(8, 8),  end=(8, 12), line='        pass\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(8, 12), end=(8, 13), line='        pass\n')
TokenInfo(type=6  (DEDENT),    string='',             start=(9, 0),  end=(9, 0),  line='else:\n')
TokenInfo(type=6  (DEDENT),    string='',             start=(9, 0),  end=(9, 0),  line='else:\n')
TokenInfo(type=1  (NAME),      string='else',         start=(9, 0),  end=(9, 4),  line='else:\n')
TokenInfo(type=54 (OP),        string=':',            start=(9, 4),  end=(9, 5),  line='else:\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(9, 5),  end=(9, 6),  line='else:\n')
TokenInfo(type=5  (INDENT),    string='    ',         start=(10, 0), end=(10, 4), line='    pass\n')
TokenInfo(type=1  (NAME),      string='pass',         start=(10, 4), end=(10, 8), line='    pass\n')
TokenInfo(type=4  (NEWLINE),   string='\n',           start=(10, 8), end=(10, 9), line='    pass\n')
TokenInfo(type=6  (DEDENT),    string='',             start=(11, 0), end=(11, 0), line='')
TokenInfo(type=0  (ENDMARKER), string='',             start=(11, 0), end=(11, 0), line='')
```

## Parser

* Transforms linear sequence of tokens into AST

* Parsed expression

```python
(1 + 2) * 3
```

* Code to parse expression

```python
import ast

tree = ast.parse("1+2*3")

print(ast.dump(tree))
```

* Unreadable output

```
Module(body=[Expr(value=BinOp(left=Constant(value=1, kind=None), op=Add(), right=BinOp(left=Constant(value=2, kind=None), op=Mult(), right=Constant(value=3, kind=None))))], type_ignores=[])
```

* Python 3.10 is better

```python
import ast

tree = ast.parse("1+2*3")

print(ast.dump(tree, indent=4))
```

* Readable output

```
```

* Visualization

## AST for more complicated example

* Code to be parsed

```python
# original code
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Using_array_lookup
def primes2(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit ** 0.5 + 1.5)):  # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


print(primes2(100))
```

* Parsing

```python
import ast

with open("primes.py") as fin:
    code = fin.read()
    tree = ast.parse(code)

print(ast.dump(tree))
```

* Python 3.10

```python
import ast

with open("primes.py") as fin:
    code = fin.read()
    tree = ast.parse(code)

print(ast.dump(tree, indent=4))
```

* Visualization


## Visitor pattern

```python
import ast


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 1

    def visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node2string(node))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


def node2string(node):
    t = type(node)
    if t == ast.Constant:
        return "Constant: {}".format(node.value)
    elif t == ast.Expr:
        return "Expression:"
    elif t == ast.BinOp:
        return "Binary operation"
    elif t == ast.Add:
        return "Operator: +"
    elif t == ast.Sub:
        return "Operator: -"
    elif t == ast.Mult:
        return "Operator: *"
    elif t == ast.Div:
        return "Operator: /"
    return ""


tree = ast.parse("1+2*(1-3/4)+5")

visitor = Visitor()
visitor.visit(tree)
```

* Output

```
     Expression:
       Binary operation
         Binary operation
           Constant: 1
           Operator: +
           Binary operation
             Constant: 2
             Operator: *
             Binary operation
               Constant: 1
               Operator: -
               Binary operation
                 Constant: 3
                 Operator: /
                 Constant: 4
         Operator: +
         Constant: 5
```

## Compiler

* Transforms AST into linear sequence of bytecode instructions


```python
import ast


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 1

    def visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node)
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


tree = ast.parse("print(1+2*(1-3/4)+5)", mode="exec")

visitor = Visitor()
visitor.visit(tree)

print("Executing")

exec(compile(tree, filename="<ast>", mode="exec"))

print("Done")
```

## Decompiler

* Emits readable version of Python bytecode


```python
import ast
import dis


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 1

    def visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node)
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


tree = ast.parse("print(a+b*(c-d/e)+f)", mode="exec")

visitor = Visitor()
visitor.visit(tree)

print("Compiling")

compiled = compile(tree, filename="<ast>", mode="exec")

print("Decompiling")

dis.dis(compiled)

print("Done")
```

* Generated output

```
Decompiling
  1           0 LOAD_NAME                0 (print)
              2 LOAD_NAME                1 (a)
              4 LOAD_NAME                2 (b)
              6 LOAD_NAME                3 (c)
              8 LOAD_NAME                4 (d)
             10 LOAD_NAME                5 (e)
             12 BINARY_TRUE_DIVIDE
             14 BINARY_SUBTRACT
             16 BINARY_MULTIPLY
             18 BINARY_ADD
             20 LOAD_NAME                6 (f)
             22 BINARY_ADD
             24 CALL_FUNCTION            1
             26 POP_TOP
             28 LOAD_CONST               0 (None)
             30 RETURN_VALUE
Done
```

## Links
