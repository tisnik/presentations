#!/usr/bin/env python3

import jedi

src = '''
class C1:
    def foo(self):
        """Function foo defined in class C1."""
        return 1

class C2:
    def foo(self):
        """Function foo defined in class C2."""
        return 2

class C3:
    def foo(self):
        """Function foo defined in class C3."""
        return 2

if True:
    obj = C1()
elif True:
    obj = C2()
else:
    obj = C3()
obj.fo'''


def print_definitions(definitions):
    if not definitions:
        print("not found")
        return

    for definition in definitions:
        print(
            "{type} {name} in {module}.py:{line}".format(
                type=definition.type,
                name=definition.full_name,
                module=definition.module_name,
                line=definition.line,
            )
        )


lines = src.count("\n")
script = jedi.Script(src, lines + 1, len("obj.fo"), "test.py")

completions = script.completions()

for completion in completions:
    print(completion.name)
    print("-" * 40)
    definitions = completion.follow_definition()
    print_definitions(definitions)
    print(completion.docstring())
    print("\n" * 3)
