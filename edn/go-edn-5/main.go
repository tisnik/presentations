package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"olympos.io/encoding/edn"
)

// User je uživatelsky definovaná datová struktura s viditelnými atributy
type User struct {
	ID      uint32 `edn:"id"`
	Name    string `edn:"user-name"`
	Surname string `edn:"surname"`
}

func main() {
	inputEdnAsBytes, err := ioutil.ReadFile("user.edn")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Input (bytes):")
	fmt.Println(inputEdnAsBytes)

	fmt.Println("\nInput (string):")
	fmt.Println(string(inputEdnAsBytes))

	var user User
	edn.Unmarshal(inputEdnAsBytes, &user)

	fmt.Println("\nOutput:")
	fmt.Println(user)

	fmt.Println("\nFields:")
	fmt.Printf("ID:      %d\n", user.ID)
	fmt.Printf("Name:    %s\n", user.Name)
	fmt.Printf("Surname: %s\n", user.Surname)
}
