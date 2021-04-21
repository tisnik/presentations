package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

func main() {
	var a complex64 = -1.5 + 0i
	var b complex64 = 1.5 + 1000i
	var c complex64 = 1e30 + 1e30i
	var d complex64 = 1i

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
