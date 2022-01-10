import ctypes
import time

so7 = ctypes.CDLL("./so7.so")

t1 = ("ěščř ЩжΛλ"*10000).encode("utf-8")
t2 = ("<foobar>"*10000).encode("utf-8")

so7.concat.restype = ctypes.c_char_p

for i in range(100000):
    t = so7.concat(t1, t2)
    print(len(t))
    time.sleep(0.001)
