def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


for n in range(0, 11):
    print("{n}! = {f}".format(n=n, f=factorial(n)))

print(factorial(999))
# print(factorial(1000))
