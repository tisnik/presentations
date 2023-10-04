from time import time
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 300

for i in range(20):
    if i % 5 == 0:
        fib.cache_clear()
    print(fib.cache_info())
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
