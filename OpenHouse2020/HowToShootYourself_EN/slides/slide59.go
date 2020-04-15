package main

import (
	"fmt"
	"time"
)

func main() {
	var values []int = []int{1, 2, 3, 4, 5}

	for _, val := range values {
		v := val
		go func() {
			fmt.Println(v)
		}()
	}

	time.Sleep(5 * time.Second)
}
