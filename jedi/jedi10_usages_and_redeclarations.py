#!/usr/bin/env python3

import jedi

src = """
def x():
    return 1

print(x())

a = x()
b = x() + x()

def x():
    return 2

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


script = print_usages(src, 5, 7, "example.py")

print()

script = print_usages(src, 13, 7, "example.py")

print()

script = print_usages(src, 2, 5, "example.py")
