import ctypes

so9 = ctypes.CDLL("./so9.so")

values = [1, "Foo", True, 4, None]

IntArray = ctypes.c_int * len(values)
array = IntArray(*values)

so9.sum.restype = ctypes.c_int64

print(so9.sum(array, 4))
