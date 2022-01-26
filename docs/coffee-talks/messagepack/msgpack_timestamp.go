package main

import (
	"log"
	"os"
	"time"

	"github.com/ugorji/go/codec"
)

const filename = "/tmp/timestamp.bin"

func main() {
	// vytvořit soubor s binárními daty
	fout, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0600)
	if err != nil {
		log.Fatal(err)
	}
	defer fout.Close()

	log.Print("Output file created")

	// handler
	var handler codec.MsgpackHandle

	// důležité - serializace časového razítka ve správném datovém formátu
	handler.WriteExt = true

	// objekt realizující zakódování dat
	encoder := codec.NewEncoder(fout, &handler)

	log.Print("Encoder created")

	t := time.Now()
	log.Print(t)

	// zakódování dat
	err = encoder.Encode(t)
	if err != nil {
		log.Fatal(err)
	}

	log.Print("Done")
}
