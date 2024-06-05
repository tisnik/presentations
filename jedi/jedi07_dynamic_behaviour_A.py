#!/usr/bin/env python3

import jedi

src = """
if random.random() < 0.5:
    def x():
        return 1
else:
    def x():
        return 2

print(x())
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


script = print_definitions(src, 9, 7, "example.py")
