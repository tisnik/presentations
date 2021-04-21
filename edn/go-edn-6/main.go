package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"olympos.io/encoding/edn"
)

func main() {
	inputEdnAsBytes, err := ioutil.ReadFile("user.edn")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Input (bytes):")
	fmt.Println(inputEdnAsBytes)

	fmt.Println("\nInput (string):")
	fmt.Println(string(inputEdnAsBytes))

	user := map[interface{}]interface{}{}
	edn.Unmarshal(inputEdnAsBytes, &user)

	fmt.Println("\nOutput:")
	fmt.Println(user)

	fmt.Println("\nFields:")
	for key, value := range user {
		fmt.Printf("%v\t%v\n", key, value)
	}
}
