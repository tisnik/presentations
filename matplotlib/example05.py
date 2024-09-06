# Knihovny Numpy a matplotlib
#
# Pátý demonstrační příklad:
# - vykreslení průběhů funkcí sin a sinc
#   do jediného grafu
#   s vyplněním plochy pod průběhu

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(3 * x) / (x + 1)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.fill(x, y1, "red", x, y2, "yellow", alpha=0.3)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()
