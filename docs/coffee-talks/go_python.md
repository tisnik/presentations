# Calling Go from Pythonn

## Two different worlds

* Python has support for FFI, cffi, ctypes etc.
* It is possible to compile Go library to .so/.dll
   - integration seems easy
* But
   - in fact the integration is based on common ground: C
   - different data types
   - totally different data structures
   - GC on both sides!
* Let's try more convenien approaches first

## Howto integrate Go with C

* Go library

```go
package main

import "C"
import "fmt"

//export hello
func hello() {
	fmt.Println("Hello, world!")
}

func main() {}
```

* Compile and build a library

```
go build -buildmode=c-shared so1.go
```

* Loading Go library from C

```c
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#include "so1.h"

int main()
{
    void *library;
    void (*hello)();

    library = dlopen("./so1.so", RTLD_LAZY);
    if (library != NULL) {
        printf("dynamic library loaded: %p\n", library);
    } else {
        puts("unable to load dynamic library");
        return 1;
    }

    hello = dlsym(library, "hello");

    if (hello != NULL) {
        printf("address for 'hello' retrieved: %p\n", (void*)hello);
        puts("Calling 'hello'...");
        hello();
        puts("...called");
    } else {
        puts("unable to retrieve address for 'hello'");
    }


    if (library != NULL) {
        int err = dlclose(library);
        if (err != 0) {
            puts("unable to close dynamic library");
            return 1;
        } else {
            puts("dynamic library closed");
        }
    }

    return EXIT_SUCCESS;
}
```

* Compile and build

```
gcc -ansi use_so1.c -ldl
```

## Now use Python instead of C

* System-wide library (or LD_LIBRARY_PATH)

```python
import ctypes

so1 = ctypes.CDLL("so1.so")

so1.hello()
```

* Local library

```python
import ctypes

so1 = ctypes.CDLL("./so1.so")

so1.hello()
```

### `main` and `init` functions possible

```go
package main

import "C"
import "fmt"

//export hello
func hello() {
	fmt.Println("Hello, world!")
}

func init() {
	fmt.Println("init")
}

func main() {
	hello()
}
```

## Go function with parameters and return value

```go
package main

import "C"

//export add
func add(x, y int) int {
	return x + y
}

func main() {}
```

* Call from Python

```python
import ctypes

so3 = ctypes.CDLL("./so3.so")

a = 1
b = 2

c = so3.add(a, b)
print(c)
```

```python
import ctypes

so3 = ctypes.CDLL("./so3.so")

a = 1.2
b = 3.4

c = so3.add(a, b)
print(c)
```

```python
import ctypes

so3 = ctypes.CDLL("./so3.so")

a = 1
b = 10000000000000000

c = so3.add(a, b)
print(c)
```

## System-independent data types

```go
package main

import "C"

import "fmt"

//export add
func add(x, y int64) int64 {
	result := x + y
	fmt.Printf("Called add(%d, %d) with result %d\n", x, y, result)
	return result
}

func main() {}
```

```python
import ctypes

so4 = ctypes.CDLL("./so4.so")

a = 1
b = 2

c = so4.add(a, b)
print(c)
```

```python
import ctypes

so4 = ctypes.CDLL("./so4.so")

a = 2**31-1
b = 1

c = so4.add(a, b)
print(c)
```

```python
import ctypes

so4 = ctypes.CDLL("./so4.so")

a = 2**31-1
b = 1

so4.add.restype = ctypes.c_int64

c = so4.add(a, b)
print(c)
```

## Passing strings to Go

```go
package main

import "C"

import "fmt"

//export hello
func hello(name string) int {
	fmt.Printf("Hello %s\n", name)
	return len(name)
}

func main() {}
```

```python
import ctypes

so5 = ctypes.CDLL("./so5.so")

l = so5.hello("World!")
print(l)
```

## Type `*C.char`

```go
package main

import "C"

import "fmt"

//export hello
func hello(name *C.char) int {
	goName := C.GoString(name)
	fmt.Printf("Hello %s\n", goName)
	return len(goName)
}

func main() {}
```

```python
import ctypes

so6 = ctypes.CDLL("./so6.so")

l = so6.hello("World!")
print(l)
```

```python
import ctypes

so6 = ctypes.CDLL("./so6.so")

l = so6.hello("World!".encode("utf-8"))
print(l)
```

```python
import ctypes

so6 = ctypes.CDLL("./so6.so")

l = so6.hello("ěščř ЩжΛλ".encode("utf-8"))
print(l)
```
