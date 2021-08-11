"""Cassiniho ovál zadaný implicitní funkcí."""

import numpy as np
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-2, 2, 150)
y = np.linspace(-2, 2, 150)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# koeficienty Cassiniho oválu
a = 1.0
c1 = 0.90
c2 = 1.10

frame = 1
for c in np.linspace(c1, c2, 25):

    # implicitní funkce Cassiniho oválu
    z = (x**2 + y ** 2) ** 2 - 2*c*(x**2 - y**2) - (a**4 - c**4)

    # hodnota, která se má zvýraznit na isoploše
    levels = [0]

    # rozměry grafu při uložení: 640x480 pixelů
    fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

    # titulek grafu
    fig.suptitle('Cassiniho ovál', fontsize=15)

    # vykreslení implicitní funkce
    ax.contour(x, y, z, levels)

    # zobrazit mřížku
    ax.grid(True)

    # zachovat poměr stran
    ax.axis('scaled')

    # popisek os
    plt.xlabel('Osa x')
    plt.ylabel('Osa y')

    # uložení grafu do rastrového obrázku
    plt.savefig("cassini_anim_{:02}.png".format(frame))

    # další snímek
    frame += 1
