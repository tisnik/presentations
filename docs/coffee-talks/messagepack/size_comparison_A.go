package main

import (
	"bytes"
	"encoding/gob"
	"encoding/json"
	"encoding/xml"
	"fmt"
	"gopkg.in/mgo.v2/bson"
	"io/ioutil"

	"github.com/ugorji/go/codec"
)

// Vector represents type of data to be serialized into various formats
type Vector []float64

func encodeVectorIntoBSON(vector Vector) ([]byte, error) {
	bsonOutput, err := bson.Marshal(vector)

	if err != nil {
		return bsonOutput, err
	}
	return bsonOutput, nil
}

func encodeVectorIntoJSON(vector Vector) ([]byte, error) {
	jsonOutput, err := json.Marshal(vector)

	if err != nil {
		return jsonOutput, err
	}
	return jsonOutput, nil
}

func encodeVectorIntoIndentedJSON(vector Vector) ([]byte, error) {
	jsonOutput, err := json.MarshalIndent(vector, "", "    ")

	if err != nil {
		return jsonOutput, err
	}
	return jsonOutput, nil
}

func encodeVectorIntoXML(vector Vector) ([]byte, error) {
	xmlOutput, err := xml.Marshal(vector)

	if err != nil {
		return xmlOutput, err
	}
	return xmlOutput, nil
}

func encodeVectorIntoIndentedXML(vector Vector) ([]byte, error) {
	xmlOutput, err := xml.MarshalIndent(vector, "", "    ")

	if err != nil {
		return xmlOutput, err
	}
	return xmlOutput, nil
}

func encodeVectorIntoGob(vector Vector) ([]byte, error) {
	var buffer bytes.Buffer
	encoder := gob.NewEncoder(&buffer)

	err := encoder.Encode(vector)
	if err != nil {
		return buffer.Bytes(), err
	}
	return buffer.Bytes(), nil
}

func encodeVectorIntoMsgPack(vector Vector) ([]byte, error) {
	var buffer bytes.Buffer

	// handler
	var handler codec.MsgpackHandle

	// objekt realizující zakódování dat
	encoder := codec.NewEncoder(&buffer, &handler)

	// zakódování dat
	err := encoder.Encode(vector)
	if err != nil {
		return buffer.Bytes(), err
	}
	return buffer.Bytes(), nil
}

func saveVector(encodedVector []byte, filename string) {
	err := ioutil.WriteFile(filename, encodedVector, 0644)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Stored into file", filename)
	}
}

func printBufferInfo(buffer []byte) {
	fmt.Println("\nBuffer with encoded vector: ", len(buffer))
}

func main() {
	var array [1000]float64

	for i := 0; i < len(array); i++ {
		if i == 0 {
			array[i] = 1.0
		} else {
			array[i] = 1.0 / float64(i)
		}
	}

	var vector Vector = array[:]

	encodedVector, err := encodeVectorIntoXML(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector1.xml")

	encodedVector, err = encodeVectorIntoIndentedXML(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector2.xml")

	encodedVector, err = encodeVectorIntoJSON(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector1.json")

	encodedVector, err = encodeVectorIntoIndentedJSON(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector2.json")

	encodedVector, err = encodeVectorIntoBSON(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector1.bson")

	encodedVector, err = encodeVectorIntoGob(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector1.gob")

	encodedVector, err = encodeVectorIntoMsgPack(vector)
	if err != nil {
		fmt.Println(err)
		return
	}
	printBufferInfo(encodedVector)
	saveVector(encodedVector, "/tmp/vector1.bin")

}
