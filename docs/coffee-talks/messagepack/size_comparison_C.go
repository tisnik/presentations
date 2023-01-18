package main

import (
	"bytes"
	"encoding/gob"
	"encoding/json"
	"fmt"
	"gopkg.in/mgo.v2/bson"
	"os"

	"github.com/ugorji/go/codec"
)

type Map map[string]string

func encodeMapIntoBSON(m Map) ([]byte, error) {
	bsonOutput, err := bson.Marshal(m)

	if err != nil {
		return bsonOutput, err
	}
	return bsonOutput, nil
}

func encodeMapIntoJSON(m Map) ([]byte, error) {
	jsonOutput, err := json.Marshal(m)

	if err != nil {
		return jsonOutput, err
	}
	return jsonOutput, nil
}

func encodeMapIntoIndentedJSON(m Map) ([]byte, error) {
	jsonOutput, err := json.MarshalIndent(m, "", "    ")

	if err != nil {
		return jsonOutput, err
	}
	return jsonOutput, nil
}

func encodeMapIntoGob(m Map) ([]byte, error) {
	var buffer bytes.Buffer
	encoder := gob.NewEncoder(&buffer)

	err := encoder.Encode(m)
	if err != nil {
		return buffer.Bytes(), err
	}
	return buffer.Bytes(), nil
}

func encodeMapIntoMsgPack(m Map) ([]byte, error) {
	var buffer bytes.Buffer

	// handler
	var handler codec.MsgpackHandle

	// objekt realizující zakódování dat
	encoder := codec.NewEncoder(&buffer, &handler)

	// zakódování dat
	err := encoder.Encode(m)
	if err != nil {
		return buffer.Bytes(), err
	}
	return buffer.Bytes(), nil
}

func saveMap(encodedMap []byte, filename string) {
	err := os.WriteFile(filename, encodedMap, 0o644)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Stored into file", filename)
	}
}

func printBufferInfo(buffer []byte) {
	fmt.Println("\nBuffer with encoded map: ", len(buffer))
}

func main() {
	var m Map = make(map[string]string)
	m["foo"] = "text"
	m["bar"] = "test"
	m["baz"] = "Příliš žluťoučký kůň"
	m["longer key"] = "Příliš žluťoučký kůň"

	for i := 0; i < 256; i++ {
		key := fmt.Sprintf("key: %02x", i)
		value := fmt.Sprintf("value: %d", i)
		m[key] = value
	}

	encodedMap, err := encodeMapIntoJSON(m)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedMap)
	saveMap(encodedMap, "/tmp/map1.json")

	encodedMap, err = encodeMapIntoIndentedJSON(m)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedMap)
	saveMap(encodedMap, "/tmp/map2.json")

	encodedMap, err = encodeMapIntoBSON(m)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedMap)
	saveMap(encodedMap, "/tmp/map1.bson")

	encodedMap, err = encodeMapIntoGob(m)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedMap)
	saveMap(encodedMap, "/tmp/map1.gob")

	encodedMap, err = encodeMapIntoMsgPack(m)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedMap)
	saveMap(encodedMap, "/tmp/map1.bin")
}
