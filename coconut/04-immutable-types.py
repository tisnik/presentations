class complex(_coconut.collections.namedtuple("complex", "real imag")):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __abs__(self):
        return (self.real**2 + self.imag**2)**1 / 2

    @_coconut_tco
    def __neg__(self):
        return _coconut_tail_call((complex), *map(_coconut_minus, (self.real, self.imag)))

    @_coconut_tco
    def __add__(self, other):
        return _coconut_tail_call(complex, self.real + other.real, self.imag + other.imag)


c1 = complex(1.0, 2.0)

print(-c1)

print(c1)

print(abs(c1))

(print)((abs)(c1))

c2 = complex(100.0, 50.0)

print(c1 + c2)

print(c1 + c1)

