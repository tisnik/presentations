package main

import "C"

//export concat
func concat(text1, text2 *C.char) *C.char {
	t1 := C.GoString(text1)
	t2 := C.GoString(text2)

	result := t1 + t2
	return C.CString(result)
}

func main() {}
