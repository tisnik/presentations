#!/usr/bin/env python3

import jedi

src = """
anybody=True
answer="42"
an"""

script = jedi.Script(src, 4, len("an"), "")

completions = script.completions()

for completion in completions:
    print(completion.complete)

print()

for completion in completions:
    print(completion.name)
