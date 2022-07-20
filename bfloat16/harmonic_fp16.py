import numpy as np

h1 = np.float16(0)
h2 = np.float16(0)

n = 1

while True:
    h2 = h1 + np.float16(1) / np.float16(n)
    print(h1, h2, h2 - h1, n)
    if h1 == h2:
        break
    h1 = h2
    n += 1
