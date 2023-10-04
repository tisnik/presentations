from pyrsistent import v

vector1 = v(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(vector1)
print(type(vector1))

print(vector1[3:7:2])
print(vector1[3::2])
print(vector1[:7:2])
print(vector1[::2])
