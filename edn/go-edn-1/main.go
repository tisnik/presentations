package main

import (
	"fmt"
	"olympos.io/encoding/edn"
)

// User1 je uživatelsky definovaná datová struktura s privátními atributy
type User1 struct {
	id      uint32
	name    string
	surname string
}

// User2 je uživatelsky definovaná datová struktura s viditelnými atributy
type User2 struct {
	ID      uint32
	Name    string
	Surname string
}

func main() {
	user1 := User1{
		1,
		"Pepek",
		"Vyskoč"}

	user2 := User2{
		1,
		"Pepek",
		"Vyskoč"}

	fmt.Println("user1")
	user1EDN, err := edn.Marshal(user1)
	fmt.Println(string(user1EDN))
	fmt.Println(err)
	fmt.Println()

	user1PrettyEDN, err := edn.MarshalPPrint(user1, nil)
	fmt.Println(string(user1PrettyEDN))
	fmt.Println(err)
	fmt.Println()

	fmt.Println("user2")
	user2EDN, err := edn.Marshal(user2)
	fmt.Println(string(user2EDN))
	fmt.Println(err)
	fmt.Println()

	user2PrettyEDN, err := edn.MarshalPPrint(user2, nil)
	fmt.Println(string(user2PrettyEDN))
	fmt.Println(err)
	fmt.Println()
}
