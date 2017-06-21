#!/usr/bin/env python3
import ctypes

testlib2 = ctypes.CDLL("libtest2.so")

result = testlib2.add_integers(1, 2)
print("1 + 2 = {}".format(result))

result = testlib2.add_integers(1.5, 2)
print("1.5 + 2 = {}".format(result))
