#!/usr/bin/env python3

import jedi

src = '''
class anumber:
    """Docstring for a class."""
    pass


if random.random() < 0.5:
    def answer():
        """1st variant of answer function."""
        return "42"
elif random.random() < 0.5:
    def answer():
        """2nd variant of answer function."""
        return 42
else:
    def answer():
        """3rd variant of answer function."""
        return [42]


def anagrams(word):
    """Very primitive anagram generator."""
    if len(word) < 2:
        return word
    else:
        tmp = []
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1:]):
                tmp.append(j+letter)
    return tmp

ann = lambda x,y: x+y
anybody=True
print(answer())'''


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
script = jedi.Script(src, lines + 1, len("print("), "test.py")

definitions = script.goto_definitions()

print_definitions(definitions)
