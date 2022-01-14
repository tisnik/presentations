import ctypes

so10 = ctypes.CDLL("./so10.so")

def c_array(values):
    ArrayType = ctypes.c_double * len(values)
    return ArrayType(*values)

so10.average.restype =  ctypes.c_double

v1 = []
print(so10.average(c_array(v1), len(v1)))

v2 = [1]
print(so10.average(c_array(v2), len(v2)))

v3 = [1, 2]
print(so10.average(c_array(v3), len(v3)))

v4 = [1, 2, 3, 4]
print(so10.average(c_array(v4), len(v4)))
