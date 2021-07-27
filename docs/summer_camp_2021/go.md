# Go programming language

* Pavel Tišnovský, Red Hat
    - `ptisnovs@redhat.com`
* Presentation:
    - [https://tisnik.github.io/presentations/summer_camp_2021/go.html](https://tisnik.github.io/presentations/summer_camp_2021/go.html)
* Presentation source:
    - [https://github.com/tisnik/presentations/blob/master/docs/summer_camp_2021/go.md](https://github.com/tisnik/presentations/blob/master/summer_camp_2021talks/go.md)

![images/golang_logo.jpg](images/golang_logo.jpg)

---

## Introduction

- Launched in November 2009 by Google
- Rob Pike, Ken Thompson, Robert Griesemer
- More readable replacement for C/C++/Java/...
- statically typed, compiled, garbage collected
- built-in concurrency
- server-side web (PHP, Node.js, Python)
- cloud technologies (docker, kubernetes)

## Resources
- [Go language course](https://github.com/RedHatOfficial/GoCourse)
- [Tour of Go](https://tour.golang.org/welcome/1)
- [Effective Go](https://golang.org/doc/effective_go.html)
- [Go Doc](https://godoc.org/)

## Development interface
- Vim;-)
- Visual Studio Code + go lang support [[https://code.visualstudio.com/docs/setup/linux]]

## Packages and Imports
- Program building blocks ("libraries")
- Imported by other programs
- Package name is the last element of the import path
- Standard packages: [[https://golang.org/pkg/]]

```go
package main

import "fmt"
```

## Hello world

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello world")
}
```

* Unicode support

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Привет, мир")
}
```

## go-fmt

```go
package main; import "fmt"
func main(
) { fmt.Println("Hello world") }
```

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello world")
}
```

## Syntax
- Evolved from C
- Declarations in postfix
- Exported symbols begin with Capital letter
- https://blog.golang.org/gos-declaration-syntax

```c
int a;
int *p;
int *(*f)(int *);
```

```go
a int
p *int
f func(*int) *int
```

## Functions

## Multiple return values

## Named return values
