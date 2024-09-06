# Knihovny Numpy a matplotlib
#
# Desátý demonstrační příklad:
# - vykreslení průběhů několika funkcí
# - do polárního grafu

import numpy as np

import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 2 * np.abs(theta - np.pi)

# třetí funkce: vzdálenost od středu
radius3 = 2 * np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce
# v polárním grafu
ax.plot(theta, radius1, "r.", label="f1")

# vykreslit průběh druhé funkce
# v polárním grafu
ax.plot(theta, radius2, "g", label="f2")

# vykreslit průběh třetí funkce
# v polárním grafu
ax.plot(theta, radius3, "b--", label="f3")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()
