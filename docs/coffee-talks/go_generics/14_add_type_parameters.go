// Type approximations introduced then...

package main

import "fmt"

type numeric interface {
	~int | ~float64 | ~complex128
}

func add[T numeric](x T, y T) T {
	return x + y
}

type myInt int

type myFloat float64

type myComplex complex128

func main() {
	var x myInt = 42
	var y myFloat = 3.14
	var z myComplex = 1 + 2i

	fmt.Println(add(x, x))
	fmt.Println(add(y, y))
	fmt.Println(add(z, z))
}
