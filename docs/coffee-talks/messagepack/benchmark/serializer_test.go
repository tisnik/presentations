package main

import (
	"fmt"

	"testing"
)

func createMap(n int) Map {
	var m Map = make(map[string]string)
	m["foo"] = "text"
	m["bar"] = "test"
	m["baz"] = "Příliš žluťoučký kůň"
	m["longer key"] = "Příliš žluťoučký kůň"

	for i := 0; i < n; i++ {
		key := fmt.Sprintf("key: %02x", i)
		value := fmt.Sprintf("value: %d", i)
		m[key] = value
	}
	return m
}

func benchmark(b *testing.B, n int, f func(m Map) ([]byte, error)) {
	m := createMap(n)
	for i := 0; i < b.N; i++ {
		f(m)
	}
}

func BenchmarkBSON1(b *testing.B) {
	benchmark(b, 1, encodeMapIntoBSON)
}

func BenchmarkBSON100(b *testing.B) {
	benchmark(b, 100, encodeMapIntoBSON)
}

func BenchmarkBSON1000(b *testing.B) {
	benchmark(b, 1000, encodeMapIntoBSON)
}

func BenchmarkJSON1(b *testing.B) {
	benchmark(b, 1, encodeMapIntoJSON)
}

func BenchmarkJSON100(b *testing.B) {
	benchmark(b, 100, encodeMapIntoJSON)
}

func BenchmarkJSON1000(b *testing.B) {
	benchmark(b, 1000, encodeMapIntoJSON)
}

func BenchmarkIndentedJSON1(b *testing.B) {
	benchmark(b, 1, encodeMapIntoIndentedJSON)
}

func BenchmarkIndentedJSON100(b *testing.B) {
	benchmark(b, 100, encodeMapIntoIndentedJSON)
}

func BenchmarkIndentedJSON1000(b *testing.B) {
	benchmark(b, 1000, encodeMapIntoIndentedJSON)
}

func BenchmarkGob1(b *testing.B) {
	benchmark(b, 1, encodeMapIntoGob)
}

func BenchmarkGob100(b *testing.B) {
	benchmark(b, 100, encodeMapIntoGob)
}

func BenchmarkGob1000(b *testing.B) {
	benchmark(b, 1000, encodeMapIntoGob)
}

func BenchmarkMsgPack1(b *testing.B) {
	benchmark(b, 1, encodeMapIntoMsgPack)
}

func BenchmarkMsgPack100(b *testing.B) {
	benchmark(b, 100, encodeMapIntoMsgPack)
}

func BenchmarkMsgPack1000(b *testing.B) {
	benchmark(b, 1000, encodeMapIntoMsgPack)
}
