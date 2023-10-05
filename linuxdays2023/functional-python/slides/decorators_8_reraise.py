from funcy import reraise

class MathError(Exception):
    def __init__(self, message):
        self.message = message


@reraise(errors=Exception, into=MathError("neděl nulou!"))
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))
