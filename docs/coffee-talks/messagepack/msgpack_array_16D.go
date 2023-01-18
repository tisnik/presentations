package main

import (
	"log"
	"os"

	"github.com/ugorji/go/codec"
)

const filename = "/tmp/array16D.bin"

func main() {
	// vytvořit soubor s binárními daty
	fout, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0o600)
	if err != nil {
		log.Panic(err)
	}
	defer fout.Close()

	log.Print("Output file created")

	// handler
	var handler codec.MsgpackHandle

	// objekt realizující zakódování dat
	encoder := codec.NewEncoder(fout, &handler)

	log.Print("Encoder created")

	var values []interface{}

	values = append(values, 1)
	values = append(values, 100000)
	values = append(values, "test")
	values = append(values, []int{1, 2, 3})
	values = append(values, map[string]string{
		"one": "jedna",
		"two": "dve",
	})

	// zakódování dat
	err = encoder.Encode(values)
	if err != nil {
		log.Panic(err)
	}

	log.Print("Done")
}
