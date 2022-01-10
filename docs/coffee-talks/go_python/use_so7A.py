import ctypes

so7 = ctypes.CDLL("./so7.so")

t1 = "ěščř ЩжΛλ".encode("utf-8")
t2 = "<foobar>".encode("utf-8")

so7.concat.restype = ctypes.c_char_p

t = so7.concat(t1, t2)
print(t)
