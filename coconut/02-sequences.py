print(map(lambda x: x * 2, [1, 2, 3, 4]))

print(fmap(lambda x: x * 2, [1, 2, 3, 4]))

print(map(lambda x: x * 2, (1, 2, 3, 4)))

print(fmap(lambda x: x * 2, (1, 2, 3, 4)))

print(map(lambda x: x * 2, range(10)))

print(fmap(lambda x: x * 2, range(10)))

print(reduce(lambda acc, x: acc * x, range(1, 10)))

print(list(takewhile(lambda x: x < 10, range(100))))

print(list(dropwhile(lambda x: x < 10, range(100))))

print(list(takewhile(lambda x: x < 10, (count()))))

print(list(takewhile(lambda x: x < 10, (count(0)))))

print(list(takewhile(lambda x: x < 10, (count(0, 2)))))

