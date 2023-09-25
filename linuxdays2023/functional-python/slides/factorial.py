n = range(0, 11)

factorials = map(lambda n: reduce(lambda a, b: a*b, range(1, n+1), 1), n)

print(list(factorials))
