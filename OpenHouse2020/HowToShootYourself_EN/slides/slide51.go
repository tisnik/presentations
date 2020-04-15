package main

import "fmt"

func main() {
	x := 10
	y := 20

	if x < y {
		x := y
	}

	fmt.Println(x, y)
}
