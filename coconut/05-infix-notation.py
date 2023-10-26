print((isinstance)("hello", str))

@_coconut_tco
def factorial(n):
    if n <= 1:
        return 1
    else:
        return _coconut_tail_call(reduce, _coconut.operator.mul, range(1, n + 1))

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(factorial(10))

for k in range(5):
    print(choose(4, k))

print()

for k in range(5):
    print((choose)(4, k))

def nad(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print()

for k in range(5):
    print((nad)(4, k))

