import ctypes

so11 = ctypes.CDLL("./so11.so")

so11.length.restype =  ctypes.c_double

class Vector(ctypes.Structure):
    _fields_ = [("X", ctypes.c_double),
                ("Y", ctypes.c_double)]

v = Vector(1.0, 1.0)

print(so11.length(v))
