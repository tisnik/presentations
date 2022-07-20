import numpy as np

h1 = np.float32(0)
h2 = np.float32(0)

n = 1

while True:
    h2 = h1 + np.float32(1) / np.float32(n)
    if n % 1000 == 0:
        print(h1, h2, h2 - h1, n)
    if h1 == h2:
        break
    h1 = h2
    n += 1

print(h1, h2, n)
