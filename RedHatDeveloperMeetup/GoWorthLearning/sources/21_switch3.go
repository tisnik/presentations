package main

import "fmt"

func main() {
	i := 5
	switch {
	case i < 5:
		fmt.Println(i, "< 5")
	case i > 5:
		fmt.Println(i, "> 5")
	default:
		fmt.Println(i, "is not less nor more than 5")
	}
}
