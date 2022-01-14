import ctypes
import time

so8 = ctypes.CDLL("./so8.so")

t1 = ("ěščř ЩжΛλ"*10000).encode("utf-8")
t2 = ("<foobar>"*10000).encode("utf-8")

so8.concat.restype = ctypes.POINTER(ctypes.c_char)

for i in range(100000):
    ptr = so8.concat(t1, t2)
    val = ctypes.cast(ptr, ctypes.c_char_p).value
    print(len(val))
    time.sleep(0.001)
