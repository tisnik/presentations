package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

// User3 je uživatelsky definovaná datová struktura s viditelnými atributy
type User3 struct {
	ID      uint32 `edn:"id"`
	Name    string `edn:"user-name"`
	Surname string `edn:"surname"`
}

func main() {
	user3 := User3{
		1,
		"Pepek",
		"Vyskoč"}

	fmt.Println("user3")
	user3EDN, err := edn.Marshal(user3)
	fmt.Println(string(user3EDN))
	fmt.Println(err)
	fmt.Println()

	user3PrettyEDN, err := edn.MarshalPPrint(user3, nil)
	fmt.Println(string(user3PrettyEDN))
	fmt.Println(err)
	fmt.Println()
}
