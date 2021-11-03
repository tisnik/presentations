"""Bázové polynomy Bézierovy kvartiky."""

#
# Použito v článku:
#
# Parametrické křivky používané v designu i při tvorbě animací
# https://www.root.cz/clanky/parametricke-krivky-pouzivane-v-designu-i-pri-tvorbe-animaci/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Bezier_quartic_basis_sum.html
#

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.linspace(0, 1, 11)

# Bernsteinovy polynomy pro Bézierovu kvartiku
B = [1 * (1-t)**4,
     4 * t * (1-t)**3,
     6 * t**2 * (1-t)**2,
     4 * t**3 * (1-t),
     1 * t**4]

# vytvoření datového rámce pro uložení hodnot Bernsteinových polynomů
df = pd.DataFrame(index=t, columns=["b0,4", "b1,4", "b2,4", "b3,4", "b4,4", "sum"])

# inicializace jednotlivých sloupců datového rámce
df["b0,4"] = B[0]
df["b1,4"] = B[1]
df["b2,4"] = B[2]
df["b3,4"] = B[3]
df["b4,4"] = B[4]

# součet hodnot Bernsteinových polynomů
df["sum"] = B[0]+B[1]+B[2]+B[3]+B[4]

# vytištění obsahu datového rámce
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
