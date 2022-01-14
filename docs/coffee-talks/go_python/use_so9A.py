import ctypes

so9 = ctypes.CDLL("./so9.so")

IntArray = ctypes.c_int * 4
array = IntArray(1, 2, 3, 4)

so9.sum.restype =  ctypes.c_int64

print(so9.sum(array, 4))
