package main

import "fmt"

func main() {
	var i int = 5

	if i < 8 {
		fmt.Println(i, "< 8")
	}

	if j := 10; j < 11 {
		fmt.Println(j, "< 11")
	}
}
