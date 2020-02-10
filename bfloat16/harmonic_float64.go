package main

import "fmt"

func main() {
	var n uint64 = 1
	var h1 float64 = 0.0
	var h2 float64 = 0.0

	for true {
		h2 = h1 + 1.0/float64(n)
		if n%10000000 == 0 {
			fmt.Printf("%f %f %20.18f %d\n", h1, h2, h2-h1, n)
		}
		if h1 == h2 {
			break
		}
		h1 = h2
		n++
	}
	fmt.Printf("Done:\n%f %f %d\n", h1, h2, n)
}
