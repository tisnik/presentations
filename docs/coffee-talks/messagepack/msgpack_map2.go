package main

import (
	"log"
	"os"

	"github.com/ugorji/go/codec"
)

const filename = "/tmp/map2.bin"

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

	var m map[string]interface{} = make(map[string]interface{})
	m["foo"] = 1
	m["bar"] = 2
	m["baz"] = 1000000
	m["wee"] = "test"
	m["array"] = []int{1, 2, 3}
	m["map"] = map[string]string{
		"one": "jedna",
		"two": "dve",
	}

	// zakódování dat
	err = encoder.Encode(m)
	if err != nil {
		log.Panic(err)
	}

	log.Print("Done")
}
