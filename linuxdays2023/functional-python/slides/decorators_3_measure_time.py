from funcy import decorator
import time


@decorator
def measure_time(func):
    t = time.time()
    res = func()
    print("Function took " + str(time.time() - t) + " seconds to run")
    return res


@measure_time
def tested_function(n):
    print(f"Sleeping for {n} seconds")
    time.sleep(n)


tested_function(1)
tested_function(2)
