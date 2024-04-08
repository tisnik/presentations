from toolz.itertoolz import partition

with open("results.txt") as f:
    lines = f.read().split("\n")

results = partition(6, lines)

for result in results:
    print(",".join(result))
