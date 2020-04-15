package main

import "fmt"

func main() {
	var values []*int

	for i := 0; i < 10; i++ {
		i := i
		values = append(values, &i)
	}

	fmt.Println("Value", "Address")

	for i := 0; i < len(values); i++ {
		fmt.Println(*values[i], values[i])
	}
}
