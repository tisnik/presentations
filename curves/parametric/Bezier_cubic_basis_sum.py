"""Bázové polynomy Bézierovy kubiky."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Bezier_cubic_basis_sum.html
#

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.linspace(0, 1, 11)

# Bernsteinovy polynomy pro Bézierovu kubiku
B = [1 * (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t ** 2 * (1 - t), 1 * t ** 3]

# vytvoření datového rámce pro uložení hodnot Bernsteinových polynomů
df = pd.DataFrame(index=t, columns=["b0,3", "b1,3", "b2,3", "b3,3", "sum"])

# inicializace jednotlivých sloupců datového rámce
df["b0,3"] = B[0]
df["b1,3"] = B[1]
df["b2,3"] = B[2]
df["b3,3"] = B[3]

# součet hodnot Bernsteinových polynomů
df["sum"] = B[0] + B[1] + B[2] + B[3]

# vytištění obsahu datového rámce
print(tabulate(df, headers="keys", tablefmt="psql"))
