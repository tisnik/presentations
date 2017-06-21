#!/usr/bin/env python3
import ctypes

libtest4 = ctypes.CDLL("target/debug/libtest4.so")


class Complex(ctypes.Structure):
    _fields_ = [("real", ctypes.c_float), ("imag", ctypes.c_float)]

    def __str__(self):
        return "Complex: %f + i%f" % (self.real, self.imag)


libtest4.add_complex.argtypes = (Complex, Complex)
libtest4.add_complex.restype = Complex

libtest4.add_complex_mut.argtypes = (ctypes.POINTER(Complex), Complex)
libtest4.add_complex_mut.restype = None

c1 = Complex(1.0, 2.0)
c2 = Complex(3.0, 4.0)

c3 = libtest4.add_complex(c1, c2)

print(c1)
print(c2)
print(c3)

libtest4.add_complex_mut(ctypes.byref(c1), c2)
print(c1)
libtest4.add_complex_mut(ctypes.byref(c1), c2)
print(c1)
