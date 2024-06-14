#!/usr/bin/env python2

import ctypes

libtest7 = ctypes.CDLL("target/debug/libtest7.so")

libtest7.sum.argtypes = (ctypes.POINTER(ctypes.c_uint32), ctypes.c_size_t)
libtest7.sum.restype = ctypes.c_int32


def sum(numbers):
    buf_type = ctypes.c_uint32 * len(numbers)
    buf = buf_type(*numbers)
    return libtest7.sum(buf, len(numbers))


print(sum([1, 2, 3, 4]))

print(sum(range(11)))
