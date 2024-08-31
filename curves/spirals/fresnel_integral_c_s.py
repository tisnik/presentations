import math

import numpy as np

import matplotlib.pyplot as plt

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


# výpočet Fresnelova integrálu C(x)
def fresnel_c(x):
    result = 0
    for t in np.arange(0, x, step):
        result += math.cos(t ** 2)
    return result * step


# vektorizace předchozích funkcí
fresnel_s_v = np.vectorize(fresnel_s)
fresnel_c_v = np.vectorize(fresnel_c)

# aplikace vektorizovaných funkcí na všechny x-ové hodnoty
y_s = fresnel_s_v(x)
y_c = fresnel_c_v(x)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Fresnelův integrál S(x) a C(x)", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y_s, "r-")

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y_c, "b-")

# uložení grafu do rastrového obrázku
plt.savefig("fresnel_c_s.png")

# zobrazení grafu
plt.show()
