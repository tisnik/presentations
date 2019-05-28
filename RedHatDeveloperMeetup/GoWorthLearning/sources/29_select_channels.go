package main

import (
	"fmt"
	"time"
)

func worker(channel chan int, worker int) {
	fmt.Printf("Worker %d started\n", worker)
	time.Sleep(1 * time.Second)
	channel <- 1
	fmt.Printf("Worker %d finished\n", worker)
}

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	go worker(ch1, 1)
	go worker(ch2, 2)

	select {
	case <-ch1:
		fmt.Println("Data from channel 1")
	case <-ch2:
		fmt.Println("Data from channel 2")
	case <-time.After(2 * time.Second):
		fmt.Println("Timeout!")
	}
}
