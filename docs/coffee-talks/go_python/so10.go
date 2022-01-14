package main

import "C"
import "unsafe"

//export average
func average(values *C.double, length int) float64 {
	if length == 0 {
		return -1
	}

	var sum float64 = 0
	slice := unsafe.Slice(values, length)
	for _, value := range slice {
		sum += float64(value)
	}
	return sum / float64(length)
}

func main() {}
