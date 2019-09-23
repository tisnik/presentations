package main

import "fmt"

func main() {
	if i := 10; i < 9 {
		fmt.Println(i, "< 9")
	} else {
		fmt.Println(i, "< 9 is false")
	}
}
