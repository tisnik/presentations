def factorial(n, acc=1):
    if n < 2:
        return acc
    else:
        return factorial(n - 1, acc * n)


for n in range(0, 11):
    print("{n}! = {f}".format(n=n, f=factorial(n)))

print(factorial(999))
# print(factorial(1000))
