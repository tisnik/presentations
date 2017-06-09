# Knihovny Numpy a matplotlib
#
# Druhý demonstrační příklad:
# - vykreslení průběhu funkce sin
# - uložení grafu do různých typů souboru

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x)")

# vykreslení a uložení grafu do různých typů souborů
plt.savefig("example02.png")
plt.savefig("example02.pdf")
plt.savefig("example02.eps")
plt.savefig("example02.ps")
plt.savefig("example02.svg")

# zobrazení grafu
plt.show()
