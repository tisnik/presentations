# Knihovny Numpy a matplotlib
#
# Osmý demonstrační příklad:
# - vykreslení průběhů funkcí sin a cos
# - nastavení mřížky
# - nastavení rozsahů na obou osách
# - přidání popisku přímo do grafu

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r-", label="cos")

# přidání legendy
plt.legend(loc="lower left")

# nastavení rozsahů na obou osách
plt.axis([-1, 8, -1.5, 1.5])

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# vložit první popisek do grafu
plt.annotate(
    "maximální hodnota sin(x)",
    xy=(np.pi / 2, 1.0),
    xytext=(1, 1.3),
    arrowprops=dict(arrowstyle="->"),
)

# vložit druhý popisek do grafu
plt.annotate(
    "minimální hodnota cos(x)",
    xy=(np.pi, -1.0),
    xytext=(2, -1.3),
    arrowprops=dict(arrowstyle="->"),
)

# zobrazení grafu
plt.show()
