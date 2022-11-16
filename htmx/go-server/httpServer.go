package main

import (
	"fmt"
	"log"
	"net/http"
)

func indexPageHandler(writer http.ResponseWriter, request *http.Request) {
	http.ServeFile(writer, request, "basic_example1.htm")
}

func htmxHandler(writer http.ResponseWriter, request *http.Request) {
	http.ServeFile(writer, request, "htmx.min.js")
}

func answerHandler(writer http.ResponseWriter, request *http.Request) {
	writer.Header().Set("Content-Type", "application/html")
	writer.WriteHeader(http.StatusOK)
	fmt.Fprint(writer, `<h1>42</h1>`)
}

func startHttpServer(address string) {
	log.Printf("Starting server on address %s", address)

	http.HandleFunc("/", indexPageHandler)
	http.HandleFunc("/htmx.min.js", htmxHandler)
	http.HandleFunc("/answer", answerHandler)
	http.ListenAndServe(address, nil)
}

func main() {
	startHttpServer(":8080")
}
