# Knihovny Numpy a matplotlib
#
# Osmnáctý demonstrační příklad:
# - změna stylu koláčových grafů

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

# vytáhnutí výřezů
explode = (0.0, 0.0, 0.15)

# barvy
colors = ("yellow", "#60ff60", "red")

# vytvoření koláčového grafu
patches, texts, autotexts = ax.pie(
    fracs, explode=explode, colors=colors, labels=labels, autopct="%1.1f%%", shadow=True
)

# změna stylu písma
proptease = fm.FontProperties()
proptease.set_size("xx-large")
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

# zobrazení grafu
plt.show()
