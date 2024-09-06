# Knihovny Numpy a matplotlib
#
# Šestý demonstrační příklad:
# - vykreslení průběhů čtyř různých funkcí
#   do jediného grafu
#   s vyplněním plochy pod průběhu
# - kombinace různých stylů vykreslení

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.001, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(5 * x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(5 * x) / (x + 1 / 2)

# hodnoty na y-ové ose: třetí čtvrtá funkce
y3 = 1 / (x + 1 / 2)
y4 = -y3

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.fill(x, y1, "yellow", alpha=0.3, label="sin x")
plt.fill(x, y2, "r.", alpha=1.0, label="sinc 5x")
plt.plot(x, y3, "g--", label="obalka sinc")
plt.plot(x, y4, "g--", label="obalka sinc")

# přidání legendy
plt.legend(loc="upper right")

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()
