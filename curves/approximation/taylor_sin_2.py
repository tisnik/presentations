"""Výpočet aproximace hodnoty funkce pomocí Taylorovy řady."""

import numpy as np
import matplotlib.pyplot as plt


def taylor_series(x, order):
    """Výpočet aproximace hodnoty funkce pomocí Taylorovy řady."""
    a = x
    sum = a
    for i in range(1, order):
        a *= -1 * x**2 / ((2 * i) * (2 * i + 1))
        sum += a
    return sum
 
 
# průběh nezávislé proměnné x
# (hodnoty na x-ové ose)
x = np.linspace(-20, 20, 500)
 
# funkce kterou aproximujeme Taylorovou řadou
y = np.sin(x)
 
# vykreslení původní funkce
plt.plot(x, y, label='sin(x)')

# příprava pro vlastní výpočet
ys = np.vectorize(taylor_series)
 
# aproximace Taylorovou řadou
N = 2

# výpočet s převodem na typ numpy.array
approx = ys(x, N)

# vykreslení aproximace funkce
plt.plot(x, approx, label='order {o}'.format(o=N))
 
# limity na ose y
plt.ylim([-3, 3])
 
# legenda grafu
plt.legend()
 
# uložení grafu do rastrového obrázku
plt.savefig("taylor_sin_2.png")

# zobrazení grafu
plt.show()
