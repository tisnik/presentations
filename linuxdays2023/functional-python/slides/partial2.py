from functools import partial


def mul(x=1, y=1, z=1, w=1):
    return x * y * z * w


f1 = mul
f2 = partial(mul, x=2)
f3 = partial(mul, y=2)
f4 = partial(mul, y=2, z=2)
f5 = partial(mul, x=2, y=2, z=2)
f6 = partial(mul, x=2, y=2, z=2, w=2)
