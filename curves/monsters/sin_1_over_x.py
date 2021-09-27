"""Průběh funkce y=sin 1/x."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru x
x = np.linspace(0, 2, 500)

# výpočet bodů ležících na křivce vytvořené funkcí
y = np.sin(1/x)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('y=sin 1/x', fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# uložení grafu do rastrového obrázku
plt.savefig("sin_1_over_x.png")

# zobrazení grafu
plt.show()
