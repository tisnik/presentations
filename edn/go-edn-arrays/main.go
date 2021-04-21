package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

func main() {
	var a1 [10]byte
	var a2 [10]int32
	a3 := [10]int32{1, 10, 2, 9, 3, 8, 4, 7, 5, 6}
	a4 := []string{"www", "root", "cz"}
	a5 := []interface{}{1, "root", 3.1415, true, []int{1, 2, 3, 4}}

	matice := [4][3]float32{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
		{0, -1, 0},
	}

	a1EDN, err := edn.MarshalPPrint(a1, nil)
	fmt.Println(string(a1EDN))
	fmt.Println(err)
	fmt.Println()

	a2EDN, err := edn.MarshalPPrint(a2, nil)
	fmt.Println(string(a2EDN))
	fmt.Println(err)
	fmt.Println()

	a3EDN, err := edn.MarshalPPrint(a3, nil)
	fmt.Println(string(a3EDN))
	fmt.Println(err)
	fmt.Println()

	a4EDN, err := edn.MarshalPPrint(a4, nil)
	fmt.Println(string(a4EDN))
	fmt.Println(err)
	fmt.Println()

	a5EDN, err := edn.MarshalPPrint(a5, nil)
	fmt.Println(string(a5EDN))
	fmt.Println(err)
	fmt.Println()

	maticeEDN, err := edn.MarshalPPrint(matice, nil)
	fmt.Println(string(maticeEDN))
}
