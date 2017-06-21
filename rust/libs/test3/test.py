#!/usr/bin/env python3
import ctypes

libtest3 = ctypes.CDLL("target/debug/libtest3.so")


class Complex(ctypes.Structure):
    _fields_ = [("real", ctypes.c_float), ("imag", ctypes.c_float)]

    def __str__(self):
        return "Complex: %f + i%f" % (self.real, self.imag)


libtest3.add_complex.argtypes = (Complex, Complex)
libtest3.add_complex.restype = Complex

c1 = Complex(1.0, 2.0)
c2 = Complex(3.0, 4.0)

c3 = libtest3.add_complex(c1, c2)

print(c1)
print(c2)
print(c3)
