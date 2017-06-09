# Knihovny Numpy a matplotlib
#
# Třetí demonstrační příklad:
# - vykreslení průběhů funkcí sin a cos
#   do jediného grafu

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
plt.plot(x, y1, x, y2)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# zobrazení grafu
plt.show()
