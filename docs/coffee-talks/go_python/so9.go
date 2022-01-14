package main

import "C"
import "unsafe"

//export sum
func sum(values *C.int, length int) int64 {
	var sum int64 = 0
	slice := unsafe.Slice(values, length)
	for _, value := range slice {
		sum += int64(value)
	}
	return sum
}

func main() {}
