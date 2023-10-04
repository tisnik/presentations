from pyrsistent import s

set1 = s(1, 2, 3)
set2 = set1.add(4)

print(set1)
print(type(set1))

print(set2)
print(type(set2))
