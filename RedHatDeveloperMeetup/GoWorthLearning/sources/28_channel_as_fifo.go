package main

import (
	"fmt"
)

func main() {
	channel := make(chan rune, 3)
	channel <- 'A'
	channel <- 'B'
	channel <- 'C'

	for i := 0; i < 3; i++ {
		fmt.Printf("%c ", <-channel)
	}
}
