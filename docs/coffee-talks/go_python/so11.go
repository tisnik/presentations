package main

import "math"
import "fmt"

/*
struct Vector {
    double X;
    double Y;
};
*/
import "C"

//export length
func length(v C.struct_Vector) C.double {
	r := C.double(math.Sqrt(float64(v.X*v.X) + float64(v.Y*v.Y)))
	fmt.Printf("%f %f %f\n", float64(v.X), float64(v.Y), r)
	return r
}

func main() {}
