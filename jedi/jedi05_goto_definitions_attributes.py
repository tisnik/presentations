#!/usr/bin/env python3

import jedi

src = """
def x():
    return 42

def y():
    return 42

print(x())  # line 8
print(y())  # line 9
print(z())  # line 10

w = lambda: 42

print(w())  # line 14
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


script = print_definitions(src, 8, 7, "example.py")
script = print_definitions(src, 9, 7, "example.py")
script = print_definitions(src, 10, 7, "example.py")
script = print_definitions(src, 14, 7, "example.py")
