"""Bázové polynomy Bézierovy kvadriky."""

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.arange(0, 1.01, 0.10)

# Bernsteinovy polynomy pro Bézierovu kvadriku
B = [1 * (1-t)**2,
     2 * t * (1-t),
     1 * t**2]

# vytvoření datového rámce pro uložení hodnot Bernsteinových polynomů
df = pd.DataFrame(index=t, columns=["b0,2", "b1,2", "b2,2", "sum"])

# inicializace jednotlivých sloupců datového rámce
df["b0,2"] = B[0]
df["b1,2"] = B[1]
df["b2,2"] = B[2]

# součet hodnot Bernsteinových polynomů
df["sum"] = B[0]+B[1]+B[2]

# vytištění obsahu datového rámce
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))