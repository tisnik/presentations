package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

func main() {
	var a interface{} = nil
	var b map[string]string = nil
	c := "foo bar baz"

	aEDN, err := edn.Marshal(a)
	fmt.Println(string(aEDN))
	fmt.Println(err)

	fmt.Println()

	bEDN, err := edn.Marshal(b)
	fmt.Println(string(bEDN))
	fmt.Println(err)

	fmt.Println()

	cEDN, err := edn.Marshal(c)
	fmt.Println(string(cEDN))
	fmt.Println(err)
}
