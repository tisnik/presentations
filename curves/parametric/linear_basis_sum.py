"""Bázové polynomy lineární interpolace."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/linear_basis_sum.html
#

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.linspace(0, 1, 11)

# Bernsteinovy polynomy pro lineární interpolaci
B = [1 * (1 - t), 1 * t]

# vytvoření datového rámce pro uložení hodnot Bernsteinových polynomů
df = pd.DataFrame(index=t, columns=["b0,1", "b1,1", "sum"])

# inicializace jednotlivých sloupců datového rámce
df["b0,1"] = B[0]
df["b1,1"] = B[1]

# součet hodnot Bernsteinových polynomů
df["sum"] = B[0] + B[1]

# vytištění obsahu datového rámce
print(tabulate(df, headers="keys", tablefmt="psql"))
