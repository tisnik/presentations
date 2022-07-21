"""Bázové polynomy Catmul-Romovy spline."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Catmul-Rom_basis_sum.html
#

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.linspace(0, 1, 11)

# koeficient Catmul-Romovy spline
tau = 0.5

# bázové polynomy
Q = [
    -tau * t + 2 * tau * t ** 2 - tau * t ** 3,
    1 + (tau - 3) * t ** 2 + (2 - tau) * t ** 3,
    tau * t + (3 - 2 * tau) * t ** 2 + (tau - 2) * t ** 3,
    -tau * t ** 2 + tau * t ** 3,
]

# vytvoření datového rámce pro uložení hodnot polynomů
df = pd.DataFrame(index=t, columns=["q0", "q1", "q2", "q3", "sum"])

# inicializace jednotlivých sloupců datového rámce
df["q0"] = Q[0]
df["q1"] = Q[1]
df["q2"] = Q[2]
df["q3"] = Q[3]

# součet hodnot polynomů
df["sum"] = Q[0] + Q[1] + Q[2] + Q[3]

# vytištění obsahu datového rámce
print(tabulate(df, headers="keys", tablefmt="psql"))
