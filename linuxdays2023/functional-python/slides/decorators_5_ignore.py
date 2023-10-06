#
# Dekorátor @ignore
#

from funcy import ignore

@ignore(errors=ZeroDivisionError, default=-1)
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))
