from functools import reduce


def multiply(x, y):
    return x * y


x = range(1, 11)
print(x)

y = reduce(multiply, x)
print(y)
