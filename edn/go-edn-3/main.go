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
	var users = [3]User3{
		User3{
			ID:      1,
			Name:    "Pepek",
			Surname: "Vyskoč"},
		User3{
			ID:      2,
			Name:    "Pepek",
			Surname: "Vyskoč"},
		User3{
			ID:      3,
			Name:    "Josef",
			Surname: "Vyskočil"},
	}

	fmt.Println("users")
	usersEDN, _ := edn.Marshal(users)
	fmt.Println(string(usersEDN))
	fmt.Println()

	usersPrettyEDN, _ := edn.MarshalPPrint(users, nil)
	fmt.Println(string(usersPrettyEDN))
	fmt.Println()
}
