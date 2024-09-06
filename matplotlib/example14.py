# Knihovny Numpy a matplotlib
#
# Čtrnáctý demonstrační příklad:
# - jednoduchý sloupcový graf

import numpy as np

import matplotlib.pyplot as plt

# historické ceny ropy
cena_ropy = [
    46.68,
    44.68,
    46.90,
    47.15,
    44.59,
    44.00,
    44.63,
    45.92,
    44.15,
    45.94,
    46.05,
    46.75,
    46.25,
    45.41,
    49.20,
    45.22,
    42.56,
    38.60,
    39.31,
    38.24,
    40.45,
    41.32,
    40.80,
    42.62,
    41.87,
    42.50,
    42.23,
    43.30,
    43.08,
    44.96,
    43.87,
    44.66,
    45.15,
    47.12,
    48.52,
    48.79,
    47.98,
    47.39,
    48.14,
    48.45,
]

# počet prvků
N = len(cena_ropy)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 1.00

# sloupcový graf
plt.bar(indexes, cena_ropy, width, color="yellow", edgecolor="black", label="Cena ropy")

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
