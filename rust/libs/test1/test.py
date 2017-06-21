#!/usr/bin/env python3
import ctypes

testlib1 = ctypes.CDLL("target/debug/libtest1.so")

result = testlib1.add_integers(1, 2)
print("1 + 2 = {}".format(result))

result = testlib1.add_integers(1.5, 2)
print("1.5 + 2 = {}".format(result))
