class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


print(A.x, B.x, C.x)
