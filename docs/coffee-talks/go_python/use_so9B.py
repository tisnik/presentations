import ctypes

so9 = ctypes.CDLL("./so9.so")

values = [1, 2, 3, 4, 5]

IntArray = ctypes.c_int * len(values)
array = IntArray(*values)

so9.sum.restype =  ctypes.c_int64

print(so9.sum(array, 4))
