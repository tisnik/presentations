package main

import (
	"log"
	"os"

	"github.com/ugorji/go/codec"
)

const filename = "/tmp/longer_string.bin"

const message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod"

func main() {
	// vytvořit soubor s binárními daty
	fout, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0o600)
	if err != nil {
		log.Fatal(err)
	}
	defer fout.Close()

	log.Print("Output file created")

	// handler
	var handler codec.MsgpackHandle

	// objekt realizující zakódování dat
	encoder := codec.NewEncoder(fout, &handler)

	log.Print("Encoder created")

	// zakódování dat
	err = encoder.Encode(message)
	if err != nil {
		log.Fatal(err)
	}

	log.Print("Done")
}
