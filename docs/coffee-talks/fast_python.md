## Fast Python?

[https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-gcc.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-gcc.html)

### Where's the problem?

```python
def add_two_numbers(x, y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

### Howto solve it?

* AOT compiler
   - Cython
* JIT compiler
   - Numba

### Cython

* Superset of Python
* Compiled language
    - in fact it is transpiller to C
    - .pyx -> .c -> .so -> launch.py
* Explicit data types are optional
* `nogil`
* Calling native functions


#### Compile to C

```python
cdef add_two_numbers(x, y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

#### Explicit parameter types

```python
cdef add_two_numbers(int x, int y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

### Explicit return type

```python
cdef int add_two_numbers(int x, int y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

### Disable GIL-related locks

```python
cdef int add_two_numbers(int x, int y) nogil:
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

### Use C standard function

```python
from libc.stdio cimport printf


cdef int add_two_numbers(int x, int y) nogil:
    printf("%i\n", x)
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

### Numba

* JIT for Python

#### Decorator

```python
from numba import jit

@jit
def funkce1():
    pass
```

#### Simpler and faster `print`

* Only numbers and strings
* no file or sep argument

#### Force JIT

```python
@jit(nopython=True)
```

## Some comparisons

* ANSI C: ANSI C variant (no Python)
* Cython #1: basic variant
* Cython #2: type hints 
* Cython #3: optimizations + `nogil`
* Numba #1: original file
* Numba #2: `@jit` annotation
* Numba #3: native `print` function
* Numba #4: native `print` function + @jit(nopython=True)

![images/benchmark_1.png](images/benchmark_1.png)
![images/benchmark_2.png](images/benchmark_2.png)

