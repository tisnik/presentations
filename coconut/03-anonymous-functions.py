print(list(map(lambda x: x * 2, [1, 2, 3])))

print(fmap(lambda x: x * 2, [1, 2, 3]))

print(reduce(lambda acc, x: acc * x, range(1, 10)))

print(list(map(lambda x, y, z: [x, y, z], [1, 2, 3], [4, 5, 6], [7, 8, 9])))

print(reduce(lambda acc, x: acc * x, range(1, 10)))

print(fmap(lambda x: x * 2, range(10)))

print(list(takewhile(lambda x: x < 10, range(100))))

print(list(dropwhile(lambda x: x < 10, range(100))))

print(list(takewhile(lambda x: x < 10, (count()))))

print(list(takewhile(lambda x: x < 10, (count(0)))))

print(list(takewhile(lambda x: x < 10, (count(0, 2)))))

