# Knihovny Numpy a matplotlib
#
# Jedenáctý demonstrační příklad:
# - vykreslení průběhů několika funkcí
# - do polárního grafu

import numpy as np

import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 4 * np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 3 * np.abs(theta - 2 * np.pi)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce
# v polárním grafu
ax.plot(theta, radius2, "b", label="f1")

# vykreslit průběh druhé funkce
# v polárním grafu
ax.fill(theta, radius1, "yellow", alpha=0.3, label="f1")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()
