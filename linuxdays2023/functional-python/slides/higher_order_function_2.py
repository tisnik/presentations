#
# Funkce vyššího řádu akceptující jinou funkci
#

def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def less_than(x, y):
    return x < y


def get_operator(symbol):
    operators = {
            "+": add,
            "*": mul,
            "<": less_than,
    }
    return operators[symbol]


def calc(operator, x, y):
    return operator(x, y)


z = calc(get_operator("+"), 10, 20)
print(z)

z = calc(get_operator("*"), 10, 20)
print(z)

z = calc(get_operator("<"), 10, 20)
print(z)
