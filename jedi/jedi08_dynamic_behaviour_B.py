#!/usr/bin/env python3

import jedi

src = """
def x():
    return 1

def y():
    return 2

z = lambda: 3

if random.random() < 0.3:
    f = x
else:
    if random.random() < 0.3:
        f = y
    else:
        f = z

print(f())
"""


def print_definitions(source, line, column, module):
    print("-" * 40)

    script = jedi.Script(source, line, column, module)

    goto_definitions = script.goto_definitions()

    if not goto_definitions:
        print("not found")
        return

    for definition in goto_definitions:
        print(
            "{type} {name} in {module}.py:{line}".format(
                type=definition.type,
                name=definition.full_name,
                module=definition.module_name,
                line=definition.line,
            )
        )


lines = src.count("\n")
script = print_definitions(src, lines, 7, "example.py")
