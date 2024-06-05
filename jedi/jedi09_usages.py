#!/usr/bin/env python3

import jedi

src = """
def x():
    return 1

a = x()
b = x() + x()

print(x())
"""


def print_usages(source, line, column, module):
    script = jedi.Script(source, line, column, module)

    usages = script.usages()

    if not usages:
        print("not found")
        return

    for usage in usages:
        print(
            "{type} {name} in {module}.py:{line}".format(
                type=usage.type,
                name=usage.full_name,
                module=usage.module_name,
                line=usage.line,
            )
        )


script = print_usages(src, 8, 7, "example.py")

print()

script = print_usages(src, 2, 5, "example.py")
