import ctypes
import ctypes.util

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.free.argtypes = (ctypes.c_void_p,)

so8 = ctypes.CDLL("./so8.so")

t1 = "ěščř ЩжΛλ".encode("utf-8")
t2 = "<foobar>".encode("utf-8")

so8.concat.restype = ctypes.POINTER(ctypes.c_char)

ptr = so8.concat(t1, t2)
val = ctypes.cast(ptr, ctypes.c_char_p).value
print(val.decode("utf-8"))
libc.free(ptr)
