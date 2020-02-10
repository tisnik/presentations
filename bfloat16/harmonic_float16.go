package main

import (
	"fmt"
	"github.com/x448/float16"
)

func main() {
	var n uint64 = 1
	h1 := float16.Fromfloat32(0.0)
	h2 := float16.Fromfloat32(0.0)

	for true {
		h2 = float16.Fromfloat32(h1.Float32() + 1.0/float32(n))
		fmt.Printf("%-11s %-11s %10.8f %d\n", h1.String(), h2.String(), h2.Float32()-h1.Float32(), n)
		if h1 == h2 {
			break
		}
		h1 = h2
		n++
	}
	fmt.Printf("Done:\n%s %s %d\n", h1.String(), h2.String(), n)
}
