package main

import "fmt"

func main() {
	x := 10
	y := 20

	fmt.Println("Old x=", x)

	if x < y {
		x = y
		fmt.Println("New x=", x)
	}

	fmt.Println("Now x=", x)
}
