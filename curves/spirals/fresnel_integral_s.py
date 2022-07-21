import numpy as np
import matplotlib.pyplot as plt
import math

#
# Použito v článku:
#
# Křivky v přírodě i v počítačové grafice – svět spirál (dokončení)
# https://www.root.cz/clanky/krivky-v-prirode-i-v-pocitacove-grafice-svet-spiral-dokonceni/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#

# počet hodnot na x-ové ose
points = 300

# integrační krok
step = 0.001

# hodnoty na x-ové ose
x = np.linspace(0, 5, points)


# výpočet Fresnelova integrálu S(x)
def fresnel_s(x):
    result = 0
    for t in np.arange(0, x, step):
        result += math.sin(t ** 2)
    return result * step


# vektorizace předchozí funkce
fresnel_s_v = np.vectorize(fresnel_s)

# aplikace vektorizované funkce na všechny x-ové hodnoty
y = fresnel_s_v(x)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Fresnelův integrál S(x)", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("fresnel_s.png")

# zobrazení grafu
plt.show()
