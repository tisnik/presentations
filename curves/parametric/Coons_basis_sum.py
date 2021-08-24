"""Bázové polynomy Coonsovy kubiky."""

import numpy as np
import pandas as pd
from tabulate import tabulate

# hodnoty parametru t
t = np.arange(0, 1.01, 0.10)

# Coonsovy polynomy
C = [(1-t)**3,
     3*t**3 - 6*t**2 + 4,
     -3*t**3 + 3*t**2 + 3*t + 1,
     t**3]

# vytvoření datového rámce pro uložení hodnot polynomů
df = pd.DataFrame(index=t, columns=["c0,3", "c1,3", "c2,3", "c3,3", "sum"])

# inicializace jednotlivých sloupců datového rámce
df["c0,3"] = C[0]/6
df["c1,3"] = C[1]/6
df["c2,3"] = C[2]/6
df["c3,3"] = C[3]/6

# součet hodnot polynomů
df["sum"] = (C[0]+C[1]+C[2]+C[3])/6

# vytištění obsahu datového rámce
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
