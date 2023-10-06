#
# Persistentní množiny
#

from pyrsistent import s

set1 = s(1, 2, 3)
set2 = s(2, 3, 4)

print(set1)
print(set2)

print("sjednoceni", set1 | set2)
print("prunik", set1 & set2)
print("rozdil", set1 - set2)
print("rozdil", set2 - set1)
