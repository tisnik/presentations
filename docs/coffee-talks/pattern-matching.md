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

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    if response == "a":
        return "Abort"
    elif response == "r":
        return "Retry"
    elif response == "f":
        return "Fail"
    else:
        return "Wrong response"


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_1.py)

### Usage of map

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    commands = {
            "a": "Abort",
            "r": "Retry",
            "f": "Fail"
            }

    return commands.get(response, "Wrong response")


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_2.py)

### Match-case structure

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a":
            return "Abort"
        case "r":
            return "Retry"
        case "f":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_3.py)

### Sets for multiple inputs

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    if response in {"a", "A"}:
        return "Abort"
    elif response in {"r", "R"}:
        return "Retry"
    elif response in {"f", "F"}:
        return "Fail"
    else:
        return "Wrong response"


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_4.py)

### Or in patterns

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_5.py)

### Value capture

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _ as x:
            return f"Wrong response {x}"


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_6.py)

### Value capture - no "response" variable

```python
print("Not ready reading drive A")


def abort_retry_fail():

    match input("Abort, Retry, Fail? "):
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _ as x:
            return f"Wrong response {x}"


print(abort_retry_fail())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/abort_retry_fail_7.py)

### Fibonacci sequence generator

```python
def fib(value):
    match value:
        case 0:
            return 0
        case 1:
            return 1
        case n if n>1:
            return fib(n-1) + fib(n-2)
        case _ as wrong:
            raise ValueError("Wrong input", wrong)


for n in range(0, 11):
    print(n, fib(n))

fib(-1)
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/fib.py)

### Factorial - basic variant

```python
def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x:
            return x * factorial(x-1)


for i in range(0, 10):
    print(i, factorial(i))
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/factorial1.py)

### Condition in case branch

```python
def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/factorial2.py)

### Type checker

```python
def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

try:
    print(factorial(3.14))
except Exception as e:
    print(e)

try:
    print(factorial("hello"))
except Exception as e:
    print(e)
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/factorial3.py)

### Or-branch

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

try:
    print(factorial(3.14))
except Exception as e:
    print(e)

try:
    print(factorial("hello"))
except Exception as e:
    print(e)
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/factorial4.py)

### Tuple-based pattern

```python
def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0):
            print(f"Real number {real}")
        case (0, imag):
            print(f"Imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((0,1))
test_number((1,1))
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/complex1.py)

### Tuple-based pattern with conditions

```python
def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0) if real>0:
            print(f"Positive real number {real}")
        case (real, 0):
            print(f"Negative real number {real}")
        case (0, imag) if imag<0:
            print(f"Negative imaginary number {imag}")
        case (0, imag):
            print(f"Negative imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((-1,0))
test_number((0,1))
test_number((0,-1))
test_number((1,1))
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/complex2.py)

### Multiple words commands

```python
def perform_command():
    response = input("> ")

    match response:
        case "quit":
            return "Quit"
        case "list employees":
            return "List employees"
        case "list departments":
            return "List departments"
        case "list rooms":
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/multiword_commands_1.py)

### List-matcher

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", "employees"]:
            return "List employees"
        case ["list", "departments"]:
            return "List departments"
        case ["list", "rooms"]:
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/multiword_commands_2.py)

### Value capture (subject)

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", "employees"]:
            return "List employees"
        case ["list", "departments"]:
            return "List departments"
        case ["list", "rooms"]:
            return "List rooms"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/multiword_commands_3.py)

### Nested match-case

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", obj]:
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
                case _:
                    return "Invalid object type: employees, departments, or rooms expected"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/multiword_commands_4.py)

### Nested match-case + set-like condition

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", ("employees" | "departments" | "rooms") as obj]:
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/multiword_commands_5.py)

### Object-based pattern

```python
class Complex():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"Complex number {self.real}+i{self.imag} represented as object"


def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0) if real>0:
            print(f"Positive real number {real}")
        case (real, 0):
            print(f"Negative real number {real}")
        case (0, imag) if imag<0:
            print(f"Negative imaginary number {imag}")
        case (0, imag):
            print(f"Negative imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case Complex():
            print(value)
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((-1,0))
test_number((0,1))
test_number((0,-1))
test_number((1,1))

test_number(Complex(0,0))
test_number(Complex(1,0))
test_number(Complex(-1,0))
test_number(Complex(0,1))
test_number(Complex(0,-1))
test_number(Complex(1,1))
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/object1.py)

### Object-based pattern with multiple classes

```python
from fractions import Fraction


class Complex():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"Complex number {self.real}+i{self.imag} represented as object"


def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0) if real>0:
            print(f"Positive real number {real}")
        case (real, 0):
            print(f"Negative real number {real}")
        case (0, imag) if imag<0:
            print(f"Negative imaginary number {imag}")
        case (0, imag):
            print(f"Negative imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case Complex(real=0, imag=0):
            print(f"Zero complex represented as object")
        case Complex():
            print(value)
        case Fraction():
            print(f"Fraction {value}")
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((-1,0))
test_number((0,1))
test_number((0,-1))
test_number((1,1))

test_number(Complex(0,0))
test_number(Complex(1,0))
test_number(Complex(-1,0))
test_number(Complex(0,1))
test_number(Complex(0,-1))
test_number(Complex(1,1))

test_number(Fraction(0,1))
test_number(Fraction(1,1))
test_number(Fraction(1,2))
test_number(Fraction(1,3))
```

[Source code](https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching/pattern-matching/object2.py)

## WDYT?

* It's good that Python evolve?
* It is not good as Python is no longer simple language?
