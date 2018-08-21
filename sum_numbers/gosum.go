package main

// #cgo pkg-config: python-3.6
// #define Py_LIMITED_API
// #include <Python.h>
import "C"

func makeRange(minimum, maximum int) []int {
	slice := make([]int, maximum-minimum)
	for i := range slice {
		slice[i] = minimum + i
	}
	return slice
}

//export SumSlice
func SumSlice(slice []int) (total int) {

	for _, value := range slice {
		total += value
	}
	return

}

//export SumSlicePy
func SumSlicePy(sequence *C.PyObject) (total C.long) {

	sequenceLen := int(C.PySequence_Length(sequence))

	for i := 0; i < sequenceLen; i++ {
		element := C.PySequence_GetItem(sequence, C.Py_ssize_t(i))
		val := C.PyLong_AsLong(element)
		total += val
	}
	return
}

func main() {}
