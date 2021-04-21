package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

func main() {
	var a int8 = -10
	var b int16 = -1000
	var c int32 = -10000
	var d int32 = -1000000

	var r1 rune = 'a'
	var r2 rune = '\x40'
	var r3 rune = '\n'
	var r4 rune = '\u03BB'

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

	fmt.Println()

	r1EDN, err := edn.Marshal(r1)
	fmt.Println(string(r1EDN))
	fmt.Println(err)

	r2EDN, err := edn.Marshal(r2)
	fmt.Println(string(r2EDN))
	fmt.Println(err)

	r3EDN, err := edn.Marshal(r3)
	fmt.Println(string(r3EDN))
	fmt.Println(err)

	r4EDN, err := edn.Marshal(r4)
	fmt.Println(string(r4EDN))
	fmt.Println(err)
}
