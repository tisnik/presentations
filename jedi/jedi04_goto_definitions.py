#!/usr/bin/env python3

import jedi

src = """
def x():
    return 42

print(x())
print(y())
"""

script = jedi.Script(src, 5, 7, "example.py")

goto_definitions = script.goto_definitions()
print(goto_definitions)

print("-" * 40)

script = jedi.Script(src, 6, 7, "example.py")

goto_definitions = script.goto_definitions()
print(goto_definitions)
