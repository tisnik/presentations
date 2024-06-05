#!/usr/bin/env python3

import jedi

src = '''
class anumber:
    """Docstring for a class."""
    pass

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
answer="42"
an'''


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
script = jedi.Script(src, lines + 1, len("an"), "test.py")

completions = script.completions()

for completion in completions:
    print(completion.name)
    print("-" * 40)
    definitions = completion.follow_definition()
    print_definitions(definitions)
    print(completion.docstring())
    print("\n" * 3)
