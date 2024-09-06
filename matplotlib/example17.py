# Knihovny Numpy a matplotlib
#
# Sedmnáctý demonstrační příklad:
# - koláčový graf

from matplotlib import font_manager as fm
from matplotlib import pyplot as plt

# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=50)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů
labels = ["Perl", "Python", "Ruby"]

# šířky jednotlivých výřezů
fracs = [90, 150, 70]

# vytvoření koláčového grafu
ax.pie(fracs, labels=labels, autopct="%1.1f%%", shadow=True)

# zobrazení grafu
plt.show()
