# Knihovny Numpy a matplotlib
#
# Třináctý demonstrační příklad:
# - vykreslení průběhu funkce sinc
# - při vykreslování se použijí "schodky"

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.2, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5 * x) / x
y2 = 1 / x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color="red", label="obalka sinc", drawstyle="default")
plt.plot(x, y3, color="red", label="obalka sinc", drawstyle="default")
plt.plot(x, y, color="blue", label="sinc(x)", drawstyle="steps")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
