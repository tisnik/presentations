"""Bázové polynomy Bézierovy křivky stupně 5."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Bezier_quintic_basis_sum.html
#

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.linspace(0, 1, 11)

# Bernsteinovy polynomy pro Bézierovu křivku stupně 5
B = [
    1 * (1 - t) ** 5,
    5 * t * (1 - t) ** 4,
    10 * t ** 2 * (1 - t) ** 3,
    10 * t ** 3 * (1 - t) ** 2,
    5 * t ** 4 * (1 - t),
    1 * t ** 5,
]

# vytvoření datového rámce pro uložení hodnot Bernsteinových polynomů
df = pd.DataFrame(
    index=t, columns=["b0,5", "b1,5", "b2,5", "b3,5", "b4,5", "b5,5", "sum"]
)

# inicializace jednotlivých sloupců datového rámce
df["b0,5"] = B[0]
df["b1,5"] = B[1]
df["b2,5"] = B[2]
df["b3,5"] = B[3]
df["b4,5"] = B[4]
df["b5,5"] = B[5]

# součet hodnot Bernsteinových polynomů
df["sum"] = B[0] + B[1] + B[2] + B[3] + B[4] + B[5]

# vytištění obsahu datového rámce
print(tabulate(df, headers="keys", tablefmt="psql"))
