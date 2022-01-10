import ctypes

so2 = ctypes.CDLL("./so2.so")

so2.hello()
