package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

func main() {
	var b8 byte = 0x42
	var a uint8 = 10
	var b uint16 = 1000
	var c uint32 = 10000
	var d uint32 = 1000000

	b8EDN, err := edn.Marshal(b8)
	fmt.Println(string(b8EDN))
	fmt.Println(err)

	aEDN, err := edn.Marshal(a)
	fmt.Println(string(aEDN))
	fmt.Println(err)

	bEDN, err := edn.Marshal(b)
	fmt.Println(string(bEDN))
	fmt.Println(err)

	cEDN, err := edn.Marshal(c)
	fmt.Println(string(cEDN))
	fmt.Println(err)

	dEDN, err := edn.Marshal(d)
	fmt.Println(string(dEDN))
	fmt.Println(err)
}
