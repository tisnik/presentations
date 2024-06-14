#!/usr/bin/env python2

import ctypes

libtest6 = ctypes.CDLL("target/debug/libtest6.so")

libtest6.generate_stars.argtypes = (ctypes.c_uint8,)
libtest6.generate_stars.restype = ctypes.c_void_p
libtest6.free_string.argtypes = (ctypes.c_void_p,)


def generate_stars(count):
    pointer = libtest6.generate_stars(count)
    try:
        return ctypes.cast(pointer, ctypes.c_char_p).value.decode("utf-8")
    finally:
        libtest6.free_string(pointer)


print(generate_stars(42))
