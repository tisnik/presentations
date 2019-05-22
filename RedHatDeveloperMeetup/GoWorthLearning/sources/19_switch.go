package main

import "fmt"

func main() {
	switch i := 1; i {
	case 1:
		fmt.Println(i, "= 1")
	case 2:
		fmt.Println(i, "= 2")
	default:
		fmt.Println(i, "didn't match any rule")
	}
}
