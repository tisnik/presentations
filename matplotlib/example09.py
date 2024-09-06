# Knihovny Numpy a matplotlib
#
# Devátý demonstrační příklad:
# - základní polární graf

import numpy as np

import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# vzdálenost od středu
radius = np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh funkce
# v polárním grafu
ax.plot(theta, radius)

# zobrazení grafu
plt.show()
