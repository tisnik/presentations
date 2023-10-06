#
# Částečně vyhodnocená funkce
#

from functools import partial


def mul(x, y):
    return x * y


print(mul(6, 7))

print()

doubler = partial(mul, 2)


for i in range(11):
    print(i, doubler(i))
