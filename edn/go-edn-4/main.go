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
	m1 := make(map[string]User3)

	m1["user-id-1"] = User3{
		ID:      1,
		Name:    "Pepek",
		Surname: "Vyskoč"}

	m1["user-id-3"] = User3{
		ID:      2,
		Name:    "Josef",
		Surname: "Vyskočil"}

	fmt.Println("users map")
	usersMapEDN, _ := edn.Marshal(m1)
	fmt.Println(string(usersMapEDN))
	fmt.Println()
	usersPrettyEDN, _ := edn.MarshalPPrint(m1, nil)
	fmt.Println(string(usersPrettyEDN))
	fmt.Println()
}
